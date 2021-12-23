import ctypes
import json
import multiprocessing

from flask import Flask, render_template
from flask_apscheduler import APScheduler

from api import api_wave_info

app = Flask(__name__)

# APScheduler initialization
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

# Task ID for async API call
INTERVAL_TASK_ID = 'interval-task-id'

# Thread-safe variable to store API response
WAVE_DATA = multiprocessing.Value(ctypes.c_wchar_p, "{}")

# Basic visual design data for each riverwave
CONFIG = [
    {
        "name": "eisbach",
        "gradient_from": "rgba(8, 73, 125, 0.7) 0%",
        "gradient_to": "rgba(1, 69, 63, 0.7) 100%",
        "text_bg": "rgba(200, 200, 200, 0.2)"
    },
    {
        "name": "fuchslochwelle",
        "gradient_from": "rgba(3, 67, 51, 0.7) 0%",
        "gradient_to": "rgba(101, 0, 0, 0.7) 100%",
        "text_bg": "rgba(200, 200, 200, 0.2)"
    },
    {
        "name": "theriverwave",
        "gradient_from": "rgba(0, 70, 114, 0.7) 0%",
        "gradient_to": "rgba(121, 44, 0, 0.7) 100%",
        "text_bg": "rgba(200, 200, 200, 0.2)"
    },
    {
        "name": "almkanal",
        "gradient_from": "rgba(80, 80, 0, 0.7) 0%",
        "gradient_to": "rgba(47, 0, 100, 0.7) 100%",
        "text_bg": "rgba(200, 200, 200, 0.2)"
    }
]


@app.before_first_request
def update_wave_data():
    """
    Gets wave data from the RiverwaveStat API and stores the data in the global thread-safe
    WAVE_DATA variable.
    """
    updated_config = []

    for riverwave in CONFIG:
        api_response = api_wave_info(riverwave["name"])
        riverwave.update(api_response)
        updated_config.append(riverwave)

    WAVE_DATA.value = json.dumps(updated_config)


# Periodic update of the wave data from the API via a scheduler job
scheduler.add_job(id=INTERVAL_TASK_ID, func=update_wave_data, trigger='interval', seconds=60)


@app.errorhandler(404)
def not_found(e):
    """Default 404 not found website"""
    return render_template("404.html")


@app.route("/")
def home():
    """Home website with statistics of all waves"""

    if json.loads(str(WAVE_DATA.value)) == {}:
        return "Fetching API data..."

    return render_template("all_waves.html", config=json.loads(str(WAVE_DATA.value)))


@app.route("/<wave_name>")
def wave(wave_name):
    """Wave website with statistics of a certain wave"""

    updated_config = json.loads(str(WAVE_DATA.value))

    for riverwave in updated_config:
        if riverwave["name"] == wave_name:
            return render_template("all_waves.html", config=[riverwave])

    return render_template("404.html")


@app.route("/imprint")
def imprint():
    """Imprint website"""
    return render_template("imprint.html")


@app.route("/privacy")
def privacy():
    """Privacy website"""
    return render_template("privacy.html")


@app.route("/no-cookies")
def no_cookies():
    """No cookies website"""
    return render_template("no_cookies.html")


@app.route('/robots.txt')
def robots():
    """robots.txt to prohibit all search engine crawlers"""
    return render_template("robots.txt")


if __name__ == "__main__":
    app.run()
