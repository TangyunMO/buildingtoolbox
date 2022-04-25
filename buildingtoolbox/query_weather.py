import urllib.parse
import requests

BASE_URI = "https://www.metaweather.com"


def search_city(query):
    '''Look for a given city and disambiguate between several candidates. Return one city (or None)'''
    # $CHALLENGIFY_BEGIN
    url = urllib.parse.urljoin(BASE_URI, "/api/location/search")
    cities = requests.get(url, params={'query': query}).json()
    if not cities:
        print(f"Sorry, Metaweather does not know about {query}...")
        return None
    if len(cities) == 1:
        return cities[0]
    for i, city in enumerate(cities):
        print(f"{i + 1}. {city['title']}")
    index = int(input("Oops, which one did you mean?")) - 1
    return cities[index]
    # $CHALLENGIFY_END

def weather_forecast(woeid):
    '''Return a 5-element list of weather forecast for a given woeid'''
    # $CHALLENGIFY_BEGIN
    url = urllib.parse.urljoin(BASE_URI, f"/api/location/{woeid}")
    return requests.get(url).json()['consolidated_weather']
    # $CHALLENGIFY_END

def main(query):
    '''Ask user for a city and display weather forecast'''
    # query = input("City?\n> ")
    city = search_city(query)
    # TODO: Display weather forecast for a given city
    # $CHALLENGIFY_BEGIN
    if city:
        daily_forecasts = weather_forecast(city['woeid'])
        output = []
        for forecast in daily_forecasts:
            max_temp = round(forecast['max_temp'])
            output += [f"{forecast['applicable_date']}: {forecast['weather_state_name']} ({max_temp}°C)"]
        return output
    # $CHALLENGIFY_END
