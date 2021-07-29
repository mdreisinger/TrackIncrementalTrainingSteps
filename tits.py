from TrackIncrementalTrainingSteps import app, db
from TrackIncrementalTrainingSteps.models import User, Workout, Set

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Workout": Workout, "Set": Set} 
