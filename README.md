Weather App

A simple Python project that fetches real-time weather data for any city using the OpenWeatherMap API.
This project includes both a CLI version (runs in the terminal) and a Flask web app version (runs in a browser).

Features

Enter any city and get current weather data

Supports Fahrenheit and Celsius

Clean formatted output

Proper error handling (bad city names, missing API key, network issues)

Web version built with Flask

Shared logic between CLI and web app (no duplicate code)

Project Structure
weather-app/
│
├── weatherapp.py        # CLI version + main weather logic
├── app.py               # Flask web app
├── templates/
│   ├── index.html       # Homepage form
│   └── result.html      # Weather results page
└── README.md

Requirements

Python 3.9+

requests

flask

OpenWeatherMap API key

Setting Up Your API Key

Go to https://openweathermap.org
 and create a free account

Get your API key

Store it as an environment variable:

macOS / Linux:
export OPENWEATHER_API_KEY="your_api_key_here"

Windows (PowerShell):
setx OPENWEATHER_API_KEY "your_api_key_here"

Running the CLI Version
python weatherapp.py


You’ll be prompted for:

city

units (°F or °C)

Example output:

Weather for Boston:
  Clear sky
  Temperature: 49 °F (feels like: 44 °F)
  Humidity: 63%
  Wind speed: 5 mph

Running the Web App (Flask)

Activate your environment and run:

python app.py


If port 5000 is in use:

python app.py --port=5001


Then open your browser:

http://127.0.0.1:5001/


You’ll see:

A city input box

Units dropdown

Results formatted on a separate page

How It Works (Quick Summary)

weatherapp.py contains the real logic:

calls the OpenWeather API

handles units

formats weather output

manages errors

app.py is a simple Flask wrapper that uses the same functions to show results in a browser.

/templates contains the HTML pages Flask uses.