from db import db, ma


class Athlete(db.Model):
    __tablename__ = 'athletes'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    second_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    gender = db.Column(db.String(100))
    age = db.Column(db.Integer)
    bonus_beds = db.Column(db.Integer)
    race_link_id = db.Column(db.Integer, db.ForeignKey('racelinks.id'))


class RaceLink(db.Model):
    __tablename__ = 'racelinks'
    id = db.Column(db.Integer, primary_key=True)
    athlete_id = db.Column(db.Integer, db.ForeignKey(
        'athletes.id'), nullable=False)
    link = db.Column(db.String(200))


# Athlete Schema


class AthleteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'second_name', 'last_name',
                  'email', 'gender', 'age', 'bonus_beds', 'race_link')


athlete_schema = AthleteSchema()
athletes_schema = AthleteSchema(many=True)
