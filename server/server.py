import os
from flask import Flask, jsonify
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# Members API route
@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}

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
            # Return the JSON response
            return jsonify(response.json())
        else:
            # Handle errors in the response
            return {"error": "Failed to retrieve data"}, response.status_code
    
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(debug=True)
