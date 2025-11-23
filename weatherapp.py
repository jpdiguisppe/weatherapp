# Weather App Project:
import os #lets us access environment variables like our API key

def main ():

    city = input("Enter a city: ")
    city = city.strip()#removes leading/trailing spaces
    print("You entered:", city)

    data = get_weather_by_city(city)
    print(data)

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

def get_weather_by_city(city_name):
    """
    This function will talk to the weather API.
    It will take a city name (like 'Boston') and return the raw JSON data
    that comes back from the API.

    Steps we will implement later:
    1. Get the API key using get_api_key().
    2. Build the URL + query parameters for the API request.
    3. Use the requests library to send an HTTP GET request.
    4. Convert the API response into a Python dictionary using .json().
    5. Return that dictionary to main().
    """

    raise NotImplementedError("get_weather_by_city() is not implemented yet.")  

# TEMPORARY TESTING CODE: uncomment next like to get get_api_key() 
#print(get_api_key())

if __name__ == "__main__": #makes sure main() runs only when this file is executed directly
    main()





