from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(80), unique=True, nullable=False)
     email = db.Column(db.String(120), unique=True, nullable=False)
     name = db.Column(db.String(20),unique= False, nullable=True)
     password= db.Column(db.String(20),unique=False, nullable=False)
     image= db.Column(db.String(250), unique=False, nullable=True)
     

     def serialize(self):
         return {
             "username": self.username,
             "email": self.email,
             "id" : self.id,
             "name": self.name,
             "password": self.password,
         }
class Locations(db.Model):
        id= db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(80), unique=False, nullable=False)
        address = db.Column(db.String(80), unique=True, nullable=False)
        lat = db.Column(db.String(20),unique= False, nullable=False)
        log= db.Column(db.String(20),unique= False, nullable=False)
        ratings= db.Column(db.String(20),unique=False, nullable=False)
        fenced= db.Column(db.String(250), unique=False, nullable=False)

