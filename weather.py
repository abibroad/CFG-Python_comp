import requests

def weather_temp(input_temperature):
    if input_temperature <=15:
        return "Stay at home"
    else:
        return "Go outside"
#approute to return html page

endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "London,UK","units":"metric","appid":"499d6e460dc8e74479ce76d519c1f1f6"}

response = requests.get(endpoint, params=payload)
data = response.json()

print data["main"]
print response.url
print response.status_code
print response.headers["content-type"]
print response.text

temperature = data["main"]
name = data["name"]
weather = data["weather"][0]["main"]
print "It's {}C in {}, and the sky is {}".format(temperature, name, weather)


return weather_temp(temperature)

inside_activities = ["museum", "watch netflix", "cinema"]
outdoor_activities = ["park", "beach", "walk"]

print
