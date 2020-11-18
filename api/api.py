from flask import jsonify
from models import Athlete, RaceLink, athletes_schema, athletes_schema
from db import api


# Get All Products


@api.route('/athlete', methods=['GET'])
def get_athletes():
    all_athletes = Athlete.query.all()
    result = athletes_schema.dump(all_athletes)
    return jsonify(result)


if __name__ == "__main__":
    api.run()
