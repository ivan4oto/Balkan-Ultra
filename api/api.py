from flask import request, jsonify
from models import Athlete, RaceLink, athlete_schema, athletes_schema, link_schema, links_schema
from db import api, db
from flask_mail import Mail, Message


# setup Flask-Mail
mail = Mail(api)


# get all athletes
@api.route('/athlete', methods=['GET'])
def get_athletes():
    all_athletes = Athlete.query.filter_by(approved=True)
    result = athletes_schema.dump(all_athletes)
    if len(result) <= 0:
        return jsonify('No data found!')
    return jsonify(result)


# get all links
@api.route('/links', methods=['GET'])
def get_links():
    all_links = RaceLink.query.all()
    result = links_schema.dump(all_links)
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
        msg = Message('New Athlete on {}'.format(distance), sender="balkan@balkanultra.com",
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


if __name__ == "__main__":
    api.run()
