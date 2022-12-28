from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return {
        "status_code": 200,
        "message": "Success!"
    }, 200


@app.route("/post", methods=["POST"])
def post():
    if request.method == "POST":
        input_request = request.get_json()
        return jsonify(input_request), 201
    else:
        return jsonify({"message": "use post!"}), 405


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
