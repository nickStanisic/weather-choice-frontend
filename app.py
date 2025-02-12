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
    error_message = None
    
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
        try: 
            response = requests.post('http://localhost:5001/analyze', json=payload)

            #raise error if status is in 400-500's
            response.raise_for_status()  
            results = response.json()

        except requests.exceptions.RequestException as e:
            error_message = "Backend is currently unavailable. Please try again later."

    return render_template('index.html', results=results, error_message=error_message, API_KEY = os.getenv("API_KEY"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)