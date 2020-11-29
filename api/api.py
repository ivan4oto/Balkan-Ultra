from flask import request, jsonify
from models import Athlete, RaceLink, athlete_schema, athletes_schema, link_schema, links_schema
from db import api, db
from flask_mail import Mail, Message


# setup Flask-Mail
mail = Mail(api)


# Get all Athletes
@api.route('/athlete', methods=['GET'])
def get_athletes():
    all_athletes = Athlete.query.all()
    result = athletes_schema.dump(all_athletes)
    if len(result) <= 0:
        return jsonify('No data found!')
    return jsonify(result)


# Get all Links
@api.route('/links', methods=['GET'])
def get_links():
    all_links = RaceLink.query.all()
    result = links_schema.dump(all_links)
    if len(result) <= 0:
        return jsonify('No data found!')
    return jsonify(result)


# Create a Product
@api.route('/athlete', methods=['POST'])
def add_athlete():
    first_name = request.json['first_name']
    second_name = request.json['second_name']
    last_name = request.json['last_name']
    email = request.json['email']
    gender = request.json['gender']
    age = request.json['age']
    bonus_beds = request.json['bonus_beds']
    link = request.json['link']

    links = [RaceLink(link=l) for l in link]
    # links = [RaceLink(link=link)]
    new_athlete = Athlete(first_name=first_name, second_name=second_name, last_name=last_name,
                          email=email, gender=gender, age=age, bonus_beds=bonus_beds)
    new_athlete.race_link.extend(links)
    # adding to db
    try:
        db.session.add(new_athlete)
        db.session.add_all(links)
        db.session.commit()
    except Exception as e:
        return f"Couldn't add objects to DB, error: {str(e)}"

    # Sending email
    try:
        msg = Message('New Registered Athlete', sender="balkanultra.noreply@gmail.com",
                      recipients=['ivan.gotchev94@gmail.com'])
        msg.body = '''Registered new athlete:
                        first name - {}
                        last name - {}, 
                        email - {}
                        qualification races - {}'''.format(
            first_name, last_name, email, link)
        mail.send(msg)
    except Exception as e:
        return f"Couldn't send email: {str(e)}"

    return "Success. Everything is fine!"


if __name__ == "__main__":
    api.run()
