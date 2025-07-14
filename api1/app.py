from flask import Flask, jsonify
import requests
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


@app.route("/hello", methods=["GET"])
def hello():
    logging.info("API1: Received request")
    response = requests.get("http://api2:6000/world")
    logging.info("API1: Forwarded to API2, got: %s", response.text)
    return jsonify({
        "api1": "Hello from API1",
        "api2": response.json()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
