from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return {
        "status_code": 200,
        "message": "Success!"
    }


@app.errorhandler(404)
def not_found(error):
    return {
        "status_code": 404,
        "message": "URL not found"
    }, 404


if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            )
