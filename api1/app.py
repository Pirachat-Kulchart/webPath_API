from flask import Flask, jsonify
import requests
import logging

# Initialize the Flask application
app = Flask(__name__)

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO)


@app.route("/hello", methods=["GET"])
def hello():
    # Log that a request was received
    logging.info("API1: Received request")
    # Forward the request to API2 and get the response
    response = requests.get("http://api2:6000/world")
    # Log the response received from API2
    logging.info("API1: Forwarded to API2, got: %s", response.text)
    # Return a JSON response combining API1 and API2 messages
    return jsonify({
        "api1": "Hello from API1",
        "api2": response.json()
    })


# Run the Flask app if this file is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
