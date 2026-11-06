import redis
import flask

app = flask.Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    if flask.request.method == "GET":
        response = flask.make_response(flask.render_template("index.html"))
        response.status_code = 200
        return  response

if __name__ == "__main__":
    app.run(debug=True)