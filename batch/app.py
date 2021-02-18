from flask import Flask, jsonify
from stats import run_stats
from dotenv import load_dotenv
from datetime import datetime

load_dotenv(verbose=True)
app = Flask(__name__)


def OK(message):
    return {
        "response": message,
        "success": True,
        "error": None
    }


def error(error):
    return {
        "response": None,
        "success": False,
        "error": error
    }


@app.route("/sync/stats", methods=["POST"])
def stats():
    run_stats()
    return jsonify(OK("Sync stats complete"))


@app.route("/_hcheck")
def health_check():
    return jsonify(OK(datetime.now()))


if __name__ == "__main__":
    app.run(debug=True)
