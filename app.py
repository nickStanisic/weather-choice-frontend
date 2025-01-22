import requests
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request, render_template

load_dotenv()

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def analyze_weather():
    """This method POSTS to backend analyzer app with payload data and receives analyzed results

    Returns:
        : an index.html page that is rendered with results if POST is performed otherwise results = None
    """             
    results = None
    if request.method == 'POST':
        high = request.form.get('high')
        low = request.form.get('low')
        startTime = request.form.get('start_datetime')
        endTime = request.form.get('end_datetime')

        #info from form to POST to backend analyzer
        payload = {
            "high": high,
            "low": low,
            "startTime": startTime,
            "endTime": endTime
        }
        
        response = requests.post('http://localhost:5001/analyze', json=payload)
        results = response.json()

    return render_template('index.html', results=results, API_KEY = os.getenv("API_KEY"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)