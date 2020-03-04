from flask import Flask, render_template
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
import os

sentry_sdk.init(
    dsn=os.environ["dsn"],
    integrations=[FlaskIntegration()]
)

application = Flask(__name__)

@application.route("/")
def trigger_error():
    division_by_zero = 1 / 0
def root():
    return render_template("index.html")

@application.route("/help")
def helppage():
    return render_template("help.html")

@application.route("/hello")
def index():
    return "Hello World from Flask Hello Page.<b> v1.0"

#--------Main------------------
if __name__ == "__main__":
    application.run(debug=True, host='0.0.0.0')
#------------------------------
