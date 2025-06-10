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
    payload = None
    error_message = None

    if request.method == 'POST':
        high = request.form.get('high')
        low = request.form.get('low')
        startTime = request.form.get('start_datetime')
        endTime = request.form.get('end_datetime')

        # Info from form to POST to backend analyzer
        payload = {
            "high": high,
            "low": low,
            "startTime": startTime,
            "endTime": endTime
        }
        
        try: 
            # Use environment variable for analyzer URL
            analyzer_url = os.getenv('ANALYZER_URL', 'http://localhost:5001')
            response = requests.post(f'{analyzer_url}/analyze', json=payload)

            # Raise error if status is in 400-500's
            response.raise_for_status()  
            results = response.json()

        except requests.exceptions.RequestException as e:
            error_message = "Backend is currently unavailable. Please try again later."
            print(f"Error connecting to analyzer: {e}")

    # Remove API_KEY from template rendering
    return render_template('index.html', 
                         payload=payload, 
                         results=results, 
                         error_message=error_message)

@app.route('/maps-config')
def maps_config():
    """Proxy endpoint to provide Google Maps configuration without exposing API key"""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            return jsonify({"error": "Maps configuration unavailable"}), 500
            
        # Return the Google Maps script URL with API key
        maps_url = f"https://maps.googleapis.com/maps/api/js?key={api_key}&callback=initMap"
        return jsonify({"maps_url": maps_url})
    
    except Exception as e:
        print(f"Error getting maps config: {e}")
        return jsonify({"error": "Maps configuration unavailable"}), 500

if __name__ == "__main__":
    # Use PORT environment variable for Cloud Run, default to 8080
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)