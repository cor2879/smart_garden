from datetime import datetime
from .. import db

class SensorReading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    tds = db.Column(db.Float)
    ph = db.Column(db.Float)