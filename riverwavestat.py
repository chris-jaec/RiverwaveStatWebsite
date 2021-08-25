from flask import Flask, redirect, url_for, render_template
from api import api_latest

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

CONFIG = [
        {
            "name": "eisbach",
            "image": "eisbach.jpg",
            "gradient_from": "rgba(8, 73, 125, 0.7) 0%",
            "gradient_to": "rgba(1, 69, 63, 0.7) 100%"
        },
        {
            "name": "floßlände",
            "image": "flosslaende.jpg",
            "gradient_from": "rgba(3, 67, 51, 0.7) 0%",
            "gradient_to": "rgba(101, 0, 0, 0.7) 100%"
        },
        {
            "name": "ebensee",
            "image": "ebensee.jpg",
            "gradient_from": "rgba(0, 70, 114, 0.7) 0%",
            "gradient_to": "rgba(121, 44, 0, 0.7) 100%"
        },
        {
            "name": "almkanal",
            "image": "almkanal.jpg",
            "gradient_from": "rgba(80, 80, 0, 0.7) 0%",
            "gradient_to": "rgba(47, 0, 100, 0.7) 100%"
        }
    ]

def update_wave_data(config: dict):
    updated_config = []

    for riverwave in config:
        riverwave["data"] = api_latest(riverwave["name"])
        updated_config.append(riverwave)

    return updated_config

@app.errorhandler(404)

def not_found(e):
    return render_template("404.html")




@app.route("/")
def home():
    updated_config = update_wave_data(CONFIG)
    return render_template("all_waves.html", config=updated_config)


@app.route("/<wave_name>")
def wave(wave_name):

    updated_config = update_wave_data(CONFIG)

    for riverwave in updated_config:
        if riverwave["name"] == wave_name:
            return render_template("all_waves.html", config=[riverwave])

    return render_template("404.html")



@app.route("/imprint")
def imprint():
    return render_template("imprint.html")

if __name__ == "__main__":
    app.run()
