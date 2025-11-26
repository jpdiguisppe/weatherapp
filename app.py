from flask import Flask, render_template, request
import requests
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
            units = request.form.get("units", "imperial")
            data = get_weather_by_city(city, units=units)
            output = format_weather(data, units=units)
            return render_template("result.html", weather=output)

        except requests.exceptions.HTTPError as e:
            # This runs if the HTTP status code is an error (like 404, 401, 500, etc.)
            if e.response is not None and e.response.status_code == 404:
                # 404 = "Not Found" usually means the city name is invalid.
                error_msg = "City not found. Please check the spelling and try again."
            else:
                error_msg = f"HTTP error occurred: {e}"
            return render_template("index.html", error=error_msg)

        except requests.exceptions.RequestException as e:
            # This catches other network-related errors (e.g., no internet, timeout).
            error_msg = f"Network error occurred: {e}"
            return render_template("index.html", error=error_msg)

        except RuntimeError as e:
            # This catches our custom error from get_api_key()
            # if the OPENWEATHER_API_KEY environment variable isn't set.
            return render_template("index.html", error=str(e))

    # GET request → show empty homepage
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)