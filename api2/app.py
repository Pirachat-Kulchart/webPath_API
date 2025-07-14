from flask import Flask, jsonify
import logging


app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


@app.route("/world", methods=["GET"])
def world():
    logging.info("API2: Received request")
    return jsonify({"msg": "Hello from API2, How are you API1?"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
