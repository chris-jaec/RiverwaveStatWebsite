import ctypes
import json
import multiprocessing

from flask import Flask, render_template
from flask_apscheduler import APScheduler

from api import api_wave_info, api_wave_overview

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
CONFIG = []
HEADER_WAVES = []

api_response = api_wave_overview()
api_response = sorted(api_response, key=lambda x: int(x['metadata']['website_style']['position']))
for wave in api_response:
    if wave["enabled"]:
        CONFIG.append({"name": wave["name"]})
        HEADER_WAVES.append({"name": wave["name"], "displayName": wave["displayName"]})


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

    print(WAVE_DATA.value)
    print(HEADER_WAVES)
    return render_template("all_waves.html", config=json.loads(str(WAVE_DATA.value)), header=HEADER_WAVES)


@app.route("/<wave_name>")
def wave(wave_name):
    """Wave website with statistics of a certain wave"""

    updated_config = json.loads(str(WAVE_DATA.value))

    for riverwave in updated_config:
        if riverwave["name"] == wave_name:
            return render_template("all_waves.html", config=[riverwave], header=HEADER_WAVES)

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
