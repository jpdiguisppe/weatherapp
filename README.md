# Weather App (CLI + Flask)

A Python project that fetches real-time weather data for any city using the **OpenWeatherMap API**.  
This repository includes both a **command-line interface (CLI)** version and a **Flask web application**.

---

## Features

- Search weather for any valid city  
- Supports **Fahrenheit** and **Celsius**  
- Terminal (CLI) interface  
- Flask web interface  
- Shared logic between both versions (no duplicated code)  
- API key stored in environment variables  
- Error handling for:
  - Invalid city names  
  - Missing API key  
  - Network problems  
  - Bad HTTP responses  

---

## Requirements

- Python 3.9 or higher  
- OpenWeatherMap API key  
- Required Python libraries:
  - requests  
  - flask  

---

## How It Works

### Core Logic (`weatherapp.py`)

Handles:

- Retrieving the API key  
- Calling the OpenWeather API  
- Parsing the JSON response  
- Handling units (imperial/metric)  
- Formatting the output  
- Error handling  

### Flask Web App (`app.py`)

- Imports the core weather logic  
- Renders HTML templates  
- Handles form submissions  
- Displays errors on the webpage  
- Routes:
  - `GET /` → Display homepage  
  - `POST /` → Process city + units and display results  

### HTML Templates (`templates/`)

- `index.html` — Homepage with form  
- `result.html` — Displays weather results  


