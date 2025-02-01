import flask

app = flask.Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Hey there index page is well!"


@app.route("/health", methods=["GET"])
def health():
    return "Healthy endpoint!"


app.run("0.0.0.0", 5500)
