from flask import Flask, render_template, request, send_from_directory

from api import api_wave_info

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

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


def update_wave_data(config: list):
    updated_config = []

    for riverwave in config:
        api_response = api_wave_info(riverwave["name"])
        riverwave.update(api_response)
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

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/no-cookies")
def no_cookies():
    return render_template("no_cookies.html")

@app.route('/robots.txt')
def robots():
    return render_template("robots.txt")

if __name__ == "__main__":
    app.run()
