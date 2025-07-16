# Import necessary modules from Flask and Python standard library
from flask import Flask, jsonify
import logging

# Create a Flask application instance
app = Flask(__name__)

# Configure logging to display INFO level messages
logging.basicConfig(level=logging.INFO)


# Define a route for GET requests to '/world'
@app.route("/world", methods=["GET"])
def world():
    # Log that a request was received
    logging.info("API2: Received request")
    # Return a JSON response
    return jsonify({"msg": "Hello from API2, How are you API1?"})


# Run the Flask app if this script is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
