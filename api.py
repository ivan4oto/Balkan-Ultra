import os
import sys
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_mail import Mail, Message
from flask_cors import CORS

api = Flask(__name__)
CORS(api)
api.debug = False

api.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='balkanultra.noreply@gmail.com',
    MAIL_PASSWORD=os.environ["MAIL_PASSWORD"]
)

# setup Flask-Mail
mail = Mail(api)

# Database
api.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://balkanul_balkanul:ivanisthebest4674@localhost:5432/balkanul_db'

api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db init
db = SQLAlchemy(api)
# Init ma
ma = Marshmallow(api)

class Athlete(db.Model):
    __tablename__ = 'athletes'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    second_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
    distance = db.Column(db.String(50))
    gender = db.Column(db.String(100))
    age = db.Column(db.Integer)
    bonus_beds = db.Column(db.Integer)
    race_link = db.relationship(
        "RaceLink", backref="athletes", lazy="dynamic")
    approved = db.Column(db.Boolean(), default=False)


class RaceLink(db.Model):
    __tablename__ = 'racelinks'
    id = db.Column(db.Integer, primary_key=True)
    athlete_id = db.Column(db.Integer, db.ForeignKey(
        'athletes.id'))
    link = db.Column(db.String(200))


# Athlete Schema
class AthleteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'second_name', 'last_name',
                  'email', 'phone_number', 'distance', 'gender', 'age', 'bonus_beds', 'approved')


athlete_schema = AthleteSchema()
athletes_schema = AthleteSchema(many=True)

# Links Schema
class LinkSchema(ma.Schema):
    class Meta:
        fields = ('id', 'athlete_id', 'link')


link_schema = LinkSchema()
links_schema = LinkSchema(many=True)



@api.route('/')
def hello_world():
    return 'Hello, Worlld!'
    
# get all athletes
@api.route('/athlete', methods=['GET'])
def get_athletes():
    all_athletes = Athlete.query.filter_by(approved=True).all()
    # all_athletes = Athlete.query.all()
    result = athletes_schema.dump(all_athletes)
    if len(result) <= 0:
        return jsonify('No data found!')
    return jsonify(result)


# create athlete
@api.route('/athlete', methods=['POST'])
def add_athlete():
    distance = request.json['distance']
    first_name = request.json['first_name']
    second_name = request.json['second_name']
    last_name = request.json['last_name']
    email = request.json['email']
    phone_number = request.json['phone_number']
    gender = request.json['gender']
    age = request.json['age']
    bonus_beds = request.json['bonus_beds']
    link = request.json['link']

    new_athlete = Athlete(first_name=first_name, second_name=second_name, last_name=last_name,
                          email=email, phone_number=phone_number, gender=gender, age=age, bonus_beds=bonus_beds, distance=distance)

    if distance == 'ultra':
        links = [RaceLink(link=l) for l in link]
        new_athlete.race_link.extend(links)        
        try:
            db.session.add_all(links)
            db.session.add(new_athlete)
            db.session.commit()
        except Exception as e:
            return f"Couldn't add objects to DB, error: {str(e)}"
    elif distance == 'sky':       
        try:
            db.session.add(new_athlete)
            db.session.commit()
        except Exception as e:
            return f"Couldn't add objects to DB, error: {str(e)}"        

    # send emails
    try:
        msg = Message('New Athlete on {}'.format(distance), sender="balkanultra.noreply@gmail.com",
                      recipients=['ivan.gotchev94@gmail.com'])
        msg.body = '''Registered new athlete:
                        first name - {}
                        last name - {}, 
                        email - {},
                        phone - {},
                        distance - {},
                        qualification races - {}'''.format(
            first_name, last_name, email, phone_number, distance, link)
        mail.send(msg)
    except Exception as e:
        return f"Couldn't send email: {str(e)}"

    return "Success. Everything is fine!"
