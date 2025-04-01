from flask import Blueprint, render_template, jsonify
from app.sensors import mock_sensor
from app.data.db import SensorReading
from .. import db
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
def dashboard():
    return render_template('dashboard.html')

@bp.route('/api/reading')
def api_reading():
    tds = mock_sensor.read_tds()
    ph = mock_sensor.read_ph()

    reading = SensorReading(tds=tds, ph=ph)
    db.session.add(reading)
    db.session.commit()

    return jsonify({
        'timestamp': datetime.utcnow().isoformat(),
        'tds': tds,
        'ph': ph
    })