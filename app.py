import requests

API_KEY = "YOUR_API_KEY"

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, API_KEY)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def main():
    city = input("Enter a city name: ")

    weather_data = get_weather(city)

    if weather_data:
        print("Weather:", weather_data["weather"][0]["main"])
        print("Latitude:", weather_data["coord"]["lat"])
        print("Longitude:", weather_data["coord"]["lon"])
        print("City:", weather_data["name"])
    else:
        print("Could not find weather data for {}.".format(city))

if __name__ == "__main__":
    main()
