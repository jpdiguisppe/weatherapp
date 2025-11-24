# Weather App Project:
import os #lets us access environment variables like our API key
import requests #lets us make HTTP requests to APIs

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def main():

    # Ask user for a city
    city = input("Enter a city: ")
    city = city.strip()  # removes leading/trailing spaces
    print("You entered:", city)

    # FIRST: Check if the city is valid (using imperial as a quick test)
    try:
        # Try to get weather in imperial just to validate city exists
        data_imperial = get_weather_by_city(city, units="imperial")

    except requests.exceptions.HTTPError as e:
        # This runs if the HTTP status code is an error (like 404, 401, 500, etc.)
        if e.response is not None and e.response.status_code == 404:
            # 404 = "Not Found" usually means the city name is invalid.
            print("City not found. Please check the spelling and try again.")
        else:
            print("HTTP error occurred:", e)
        return  # stop program since city isn't valid

    except requests.exceptions.RequestException as e:
        # This catches network-related errors (no internet, timeout, etc.)
        print("Network error occurred:", e)
        return

    except RuntimeError as e:
        # This catches our custom error from get_api_key()
        print("Configuration error:", e)
        return

    # If we reach here, city is valid, so NOW ask for units

    # Ask for units (loop until valid)
    while True:
        units_choice = input("Units? (1 for Fahrenheit, 2 for Celsius) [default: 1]: ").strip()

        if units_choice in ["", "1"]:
            units = "imperial"   # Fahrenheit
            break
        elif units_choice == "2":
            units = "metric"     # Celsius
            break
        else:
            print("Invalid choice. Please enter '1', '2', or press Enter.")

    # Now fetch data in the proper units
    try:
        if units == "imperial":
            # We already fetched this earlier
            data = data_imperial
        else:
            # Fetch Celsius data from API
            data = get_weather_by_city(city, units=units)

        formatteddata = format_weather(data, units=units)
        print(formatteddata)
        
    #runs exception handling again in case of errors during second fetch
    except requests.exceptions.HTTPError as e:
        print("HTTP error occurred:", e)

    except requests.exceptions.RequestException as e:
        print("Network error occurred:", e)

    except RuntimeError as e:
        print("Configuration error:", e)
  
def get_api_key():
    """
    Get the OpenWeather API key from an environment variable.

    Returns:
        str: The API key string.

    Raises:
        RuntimeError: If the environment variable is not set.
    """
    # Read the value of the environment variable named "OPENWEATHER_API_KEY".
    # If it doesn't exist, os.getenv(...) returns None.
    
    api_key = os.getenv("OPENWEATHER_API_KEY")

    # Check if the API key is missing or empty.
    if not api_key:
        # Raise a RuntimeError with a clear message so the user knows
        # how to fix the problem instead of the program failing silently.
        raise RuntimeError(
            "OPENWEATHER_API_KEY environment variable is not set. "
            "Please export it before running the program."
        )

    # If we reach this line, we have a valid API key string.
    return api_key

def get_weather_by_city(city_name, units ="imperial"): #units=imperial is base case
    """
    Talk to the OpenWeather API and get the current weather for a given city.

    Args:
        city_name (str): City name like "Boston", "Tokyo", etc.
        units (str): Units of measurement. "imperial" for Fahrenheit, "metric" for Celsius.

    Returns:
        dict: JSON response from the weather API as a Python dictionary.

    Raises:
        requests.exceptions.RequestException
        requests.exceptions.HTTPError
    """

    # Retrieve the API key using our helper function.
    api_key = get_api_key()

    # Query parameters sent to the API.
    # "q" is the city name.
    # "appid" is your API key.
    # "units" = imperial means Fahrenheit.
    params = {
        "q": city_name,
        "appid": api_key,
        "units": units
    }

    # Send GET request to the weather API.
    response = requests.get(BASE_URL, params=params, timeout=10)

    # If the status isn't 200 OK, raise an exception.
    response.raise_for_status()

    # Convert JSON response into a Python dictionary.
    data = response.json()

    # Return the dictionary to the main program.
    return data

# TEMPORARY TESTING CODE: uncomment next like to get get_api_key() 
#print(get_api_key())

def format_weather(data, units="imperial"):
    
    """
    Take the raw weather data dictionary from the API
    and turn it into a nicely formatted multi-line string.
    """
    name = data.get("name", "Unknown location") #gets city name from data, if its missing uses "Unknown location"
    main = data.get("main", {}) #"main" conatins temp, humidity, etc.
    weather_list = data.get("weather", []) #weather is a list, we usually want the first item
    wind = data.get("wind", {}) #wind info
    
    temp = main.get("temp") #extraxt specific values from main dict
    feels_like = main.get("feels_like")
    humidity = main.get("humidity")

    #which units is being used
    if units == "metric":
        tempunits = "°C"
        windunits = "m/s"
    else:
        tempunits = "°F"
        windunits = "mph"

    if weather_list:
        description = weather_list[0].get("description", "N/A").capitalize() #get description from first item in weather list, capitalize first letter
    else:
        description = "N/A"

    wind_speed = wind.get("speed") #gets wind speed

    #build lines of text that we will join together
    lines = [
        f"Weather for {name}:",
        f"  {description}",
        f"  Temperature: {temp} {tempunits} (feels like: {feels_like} {tempunits})",
        f"  Humidity: {humidity}%",
        f"  Wind speed: {wind_speed} {windunits}",
    ]

    return "\n".join(lines) #join lines with newlines between them



if __name__ == "__main__": #makes sure main() runs only when this file is executed directly
    main()





