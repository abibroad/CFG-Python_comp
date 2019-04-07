
from flask import Flask, render_template, request
import logging

#don't know the relevance of the flask name
flask_app = Flask(__name__)

#copied from Eduardo github (don't know if it's all needed)
#CONFIGURING LOGGING
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

fh = logging.FileHandler('application_logs.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)



@flask_app.route('/cold_weather')
def cold_weather():
    return render_template("cold_weather.html")

@flask_app.route("/warm_weather")
def warm_weather():
	return render_template("warm_weather.html")


logger.info('STARTING APP, TRY IT OUT!!!')

if __name__ == '__main__':
    flask_app.run(debug=True, use_reloader=True)


#weatherapi

def weather_temp(input_temperature):
    if input_temperature <=15:
        return render_template("cold_weather.html")
    else:
        return render_template("warm_weather.html")
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


#return weather_temp(temperature)

inside_activities = ["museum", "watch netflix", "cinema"]
outdoor_activities = ["park", "beach", "walk"]


#contact form
@app.route("signup",methods=["POST"])
def sign_up():
form_data = request.format
print form_data["email"]
return "You are now subscribed to our mailing list!"
