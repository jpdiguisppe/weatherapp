from flask import Flask, render_template, request
from weatherapp import get_weather_by_city, format_weather

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        city = request.form.get("city", "").strip()

        # Basic validation
        if not city:
            return render_template("index.html", error="Please enter a city name.")

        try:
            data = get_weather_by_city(city, units="imperial")
            output = format_weather(data, units="imperial")
            return render_template("result.html", weather=output)

        except Exception as e:
            return render_template("index.html", error="Invalid city or network error.")

    # GET request → show empty homepage
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)