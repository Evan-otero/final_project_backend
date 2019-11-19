"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db, Users, Locations
from flask_jwt_simple import (
    JWTManager, jwt_required, create_jwt, get_jwt_identity
)
from sqlalchemy.exc import SQLAlchemyError

#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "hello": "world"
    }

    return jsonify(response_body), 200

@app.route('/users', methods=['GET'])
def handle_users():
    all_people = Users.query.all()
    all_people = list(map(lambda x: x.serialize(), all_people))
    return jsonify(all_people), 200

@app.route('/adduser', methods=['POST'])
def handle_user():
    try:
        body = request.get_json()
        user1 = Users(username=body['username'], email=body['email'], password=body['password'],name=body['name'],)
        db.session.add(user1)
        db.session.commit()
        
    except SQLAlchemyError as e:
        return jsonify({ "error": str(e.__dict__['orig'])}), 409
    return jsonify({"message":"success"})

@app.route('/login', methods=['POST'])
def login():
    try:
        if not request.is_json:
            return jsonify({"msg":"Missing JSON in request"}), 400

        params = request.get_json()
        username = params.get('username', None)
        password = params.get('password', None)

        if not username:
            return jsonify({"msg": "Missing username parameter"}), 400
        if not password:
            return jsonify({"msg": "Missing password parameter"}), 400
        
        usercheck = Users.query.filter_by(username=username, password=password).first()
        if usercheck == None:
            return jsonify({"msg": "Bad username or password"}), 401
        ret = {'jwt': create_jwt(identity=username), "id": usercheck.id, "email": usercheck.email}
        return jsonify(ret), 200
    except SQLAlchemyError as e:
        return jsonify({ "error": str(e.__dict__['orig'])}), 409
    
    return jsonify({"message": "success"}),200
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

