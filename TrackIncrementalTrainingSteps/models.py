from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from TrackIncrementalTrainingSteps import db, login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    workouts = db.relationship("Workout", backref="user", lazy="dynamic")

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self, password):
        return check_password_hash(self.password_hash, password)


class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    rest_period = db.Column(db.Time)
    sets = db.relationship("Set", backref="workout", lazy="dynamic")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
        
    def __repr__(self):
        return f"{self.timestamp}\n{self.rest_period}\n{self.sets}"


class Set(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    exercise = db.Column(db.String(120), index=True)
    weight = db.Column(db.Integer)
    repetitions = db.Column(db.Integer)
    rate_of_perceived_exertion = db.Column(db.Integer)
    reps_in_reserve = db.Column(db.Integer)
    notes = db.Column(db.String(255))
    workout_id = db.Column(db.Integer, db.ForeignKey("workout.id"))
    
    def __repr__(self):
        return (f"{self.timestamp}\n{self.exercise} {self.weight} x {self.repetitions}\nNotes:\n"
            + f"{self.notes}\nRPE:\n{self.rate_of_perceived_exertion}\nRIR:\n{self.reps_in_reserve}")


@login.user_loader
def load_user(id):
    return User.query.get((int(id)))
