from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(80), unique=True, nullable=False)
     email = db.Column(db.String(120), unique=True, nullable=False)
     name = db.Column(db.String(20),unique= False, nullable=True)
     password= db.Column(db.String(20),unique=False, nullable=False)
     image= db.Column(db.String(250), unique=False, nullable=True)
     locations = db.relationship('Location')

     

     def serialize(self):
         return {
             "username": self.username,
             "email": self.email,
             "id" : self.id,
             "name": self.name,
             "password": self.password,
             "locations": list(map(lambda x: x.serialize(), self.locations))
         }
class Location(db.Model):
     id= db.Column(db.Integer, primary_key=True,  autoincrement=True)
     title = db.Column(db.String(80), unique=False, nullable=False)
     address = db.Column(db.String(80), unique=True, nullable=False)
     lat = db.Column(db.String(20),unique= False, nullable=False)
     log= db.Column(db.String(20),unique= False, nullable=False)
     ratings= db.Column(db.String(20),unique=False, nullable=True)
     fenced= db.Column(db.Boolean(5), unique=False, nullable=True)
     locationtype= db.Column(db.String(12), unique=False, nullable=False)
     bathrooms= db.Column(db.Boolean(5), unique=False, nullable=True)
     wateravailable =db.Column(db.Boolean(5), unique=False, nullable=True)
     smalldogarea =db.Column(db.Boolean(5), unique=False, nullable=True)
     allowedoutside = db.Column(db.Boolean(5), unique=False, nullable=True)
     allowedinside = db.Column(db.Boolean(5), unique=False, nullable=True)
     mealsavailable = db.Column(db.Boolean(5), unique=False, nullable=True)   

     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

     def serialize(self):
         return{
             "id": self.id,
             "title": self.title,
             "address": self.address,
             "lat":self.lat,
             "log":self.log,
             "fenced": self.fenced,
             "user_id": self.user_id,
             "bathrooms":self.bathrooms,
             "wateravailable": self.wateravailable,
             "smalldogarea": self.smalldogarea,
             "allowedoutside": self.allowedoutside,
             "allowedinside:": self.allowedinside,
             "mealsavailable": self.mealsavailable,
             "locationtype": self.locationtype
             
         }

