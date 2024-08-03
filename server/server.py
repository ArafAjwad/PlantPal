import os
from flask import Flask, jsonify
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# Air Quality API route
@app.route("/air_quality")
def air_quality():
    # Get the token from environment variables
    token = os.getenv('WAQI_TOKEN')
    
    # Check if the token is available
    if not token:
        return {"error": "API token is missing"}, 500
    
    # URL for the air quality API
    url = "https://api.waqi.info/feed/@5914/?token=" + token
    
    try:
        # Make a GET request to the API
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()["data"]
            
            # Extract specific data points
            extracted_data = {
                "aqi": data["aqi"],
                "city": data["city"]["name"],
                "dominant_pollutant": data["dominentpol"],
                "iaqi": data["iaqi"],
                "temperature": data["iaqi"]["t"]["v"],
                "humidity": data["iaqi"]["h"]["v"],
                "pressure": data["iaqi"]["p"]["v"],
                "forecast": data["forecast"]["daily"],
                "uvi": data["forecast"]["daily"]["uvi"]
            }
            
            # Return the extracted data as JSON
            return jsonify(extracted_data)
        else:
            # Handle errors in the response
            return {"error": "Failed to retrieve data"}, response.status_code
    
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(debug=True)
