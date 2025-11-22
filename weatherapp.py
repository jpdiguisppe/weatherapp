# Weather App Project:
def main ():

    city = input("Enter a city: ")
    city = city.strip()#removes leading/trailing spaces
    print("You entered:", city)

    data = get_weather_by_city(city)
    print(data)

def get_api_key():
    """
    This function will retrieve your weather API key from an environment variable. 
    Environment variables let us store secrets (like API keys) OUTSIDE the code,
    so we don't accidentally upload them to GitHub.

    Steps we will implement later:
    1. Read an environment variable named "OPENWEATHER_API_KEY".
    2. If it does not exist, raise an error telling the user to set it.
    3. Return the API key as a string.
    """

    raise NotImplementedError("get_api_key() is not implemented yet.")  

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

if __name__ == "__main__": #makes sure main() runs only when this file is executed directly
    main()





