from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return {"message": "Wave Warn backend is running!"}

# Register route modules
from routes.forecast import forecast_bp
app.register_blueprint(forecast_bp, url_prefix='/forecast')

if __name__ == '__main__':
    app.run(debug=True)
