from datetime import datetime
from TrackIncrementalTrainingSteps import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    sets = db.relationship("Set", backref="lifter", lazy="dynamic")

    def __repr__(self):
        return f"<User {self.username}>"

class Set(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    exercise = db.Column(db.String(120), index=True)
    weight = db.Column(db.Integer)
    repetitions = db.Column(db.Integer)
    rate_of_perceived_exertion = db.Column(db.Integer)
    reps_in_reserve = db.Column(db.Integer)
    notes = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    
    def __repr__(self):
        return f"{self.timestamp}\n{self.exercise} {self.weight} x {self.repetitions}\nNotes:\n{self.notes}\nRPE:\n{self.rate_of_perceived_exertion}\nRIR:\n{self.reps_in_reserve}"
