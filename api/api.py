from flask import request, jsonify
from models import Athlete, RaceLink, athlete_schema, athletes_schema, link_schema, links_schema
from db import api, db
from send_mail import send_mail


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
    new_athlete = Athlete(first_name=first_name, second_name=second_name, last_name=last_name,
                          email=email, gender=gender, age=age, bonus_beds=bonus_beds)
    new_athlete.race_link.extend(links)

    db.session.add(new_athlete)
    db.session.add_all(links)
    db.session.commit()

    send_mail(athlete=f'{first_name} {second_name}',
              email=email, racelinks='abv.bg')
    return "success"


if __name__ == "__main__":
    api.run()
