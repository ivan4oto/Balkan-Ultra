from flask import request, jsonify
from models import Athlete, RaceLink, athlete_schema, athletes_schema, link_schema, links_schema
from db import api, db


# Get all Athletes
@api.route('/athlete', methods=['GET'])
def get_athletes():
    all_athletes = Athlete.query.all()
    result = athletes_schema.dump(all_athletes)
    return jsonify(result)


# Get all Links
@api.route('/links', methods=['GET'])
def get_links():
    all_links = RaceLink.query.all()
    result = links_schema.dump(all_links)
    return jsonify(result)


# Create a Product
@api.route('/athlete', methods=['POST'])
def add_athlete():
    print(request.json['link'], " < --------")
    first_name = request.json['first_name']
    second_name = request.json['second_name']
    last_name = request.json['last_name']
    email = request.json['email']
    gender = request.json['gender']
    age = request.json['age']
    bonus_beds = request.json['bonus_beds']
    link = request.json['link']

    new_athlete = Athlete(first_name=first_name, second_name=second_name, last_name=last_name,
                          email=email, gender=gender, age=age, bonus_beds=bonus_beds)
    new_race_link = RaceLink(link=link)
    new_athlete.race_link.append(new_race_link)

    db.session.add(new_athlete)
    db.session.add(new_race_link)
    db.session.commit()

    return athlete_schema.jsonify(new_athlete)


if __name__ == "__main__":
    api.run()
