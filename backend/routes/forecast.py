from flask import Blueprint, request, jsonify

forecast_bp = Blueprint('forecast', __name__)

@forecast_bp.route('/', methods=['POST'])
def get_forecast():
    data = request.json
    lat = data.get('lat')
    lon = data.get('lon')

    # Dummy forecast response (replace later with model)
    response = {
        "location": {"lat": lat, "lon": lon},
        "forecast": [
            {"day": "Day 1", "heat_index": 42},
            {"day": "Day 2", "heat_index": 43},
            {"day": "Day 3", "heat_index": 45},
        ],
        "risk": "High"
    }
    return jsonify(response)
