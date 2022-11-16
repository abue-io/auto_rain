import random
import string
import tweepy
import pyowm

# tweepy api
auth = tweepy.OAuthHandler("")
auth.set_access_token("")
api = tweepy.API(auth)

# openweathermap api
owm = pyowm.OWM('b1255ad5d28196ae57ddac808c1d8780')

# grabs the weather data for cologne, my daughter maru's place of birth
obs = owm.weather_at_id(2886242)
w = obs.get_weather()

# humidity percentage determines the probability to post a rain tweet everytime the script is run, which is every 10 minutes because of openweathermap's terms of use
probability = round(w.get_humidity()/2)

# rain conditions altering the thickness of the rain
owm_code = w.get_weather_code()

    # light intensity drizzle, thunderstorm with light drizzle
if owm_code == 300 or owm_code == 230:
    x = 25
    probability = 100

    # drizzle, thunderstorm with drizzle
if owm_code == 301 or owm_code == 231:
    x = 30
    probability = 100

    # heavy intensity drizzle, thunderstorm with heavy drizzle
if owm_code == 302 or owm_code == 232:
    x = 35
    probability = 100

    # light intensity drizzle rain
if owm_code == 310:
    x = 40
    probability = 100

    # drizzle rain, shower drizzle, light rain, light intensity showeer rain, thunderstorm with light rain
if owm_code == 311 or owm_code == 321 or owm_code == 500 or owm_code == 520 or owm_code == 200:
    x = 45
    probability = 100

    # heavy intensity drizzle rain, moderate rain, ragged shower rain, shower rain and drizzle, shower rain, freezing rain, thunderstorm with rain
if owm_code == 312 or owm_code == 501 or owm_code == 531 or owm_code == 313 or owm_code == 521 or owm_code == 511 or owm_code == 201:
    x = 50
    probability = 100

    # heavy intensity rain, heavy intensity shower rain, heavy shower rain and drizzle, thunderstorm with heavy rain
if owm_code == 502 or owm_code == 522 or owm_code == 314 or owm_code == 202:
    x = 60
    probability = 100

    # very heavy rain
if owm_code == 503:
    x = 70
    probability = 100

    # extreme rain
if owm_code == 504:
    x = random.randint(80, 100)
    probability = 100

    # this makes sure it is always raining a bit on twitter even when that is not the case for cologne
else:
    x = random.randint(2, 15)

y = round((100-x)/2)

# compose tweet and post it
while True:
	# generate string for a single line
    def randomString(stringLength=8):
        letters = ['\u00A0'] * y + ['\u2007'] * y + [','] * x
        return '\u3000'.join(random.choice(letters) for i in range(stringLength))
	# combine lines with separation characters
    raintweet = '\u3164' + '\u00A0' + randomString() + '\u000A' + randomString() + '\u000A' + '\u3164' + '\u00A0' + randomString() + '\u000A' + randomString() + '\u000A' + '\u3164' + '\u00A0' + randomString() + '\u000A' + randomString() + '\u000A' + '\u3164' + '\u00A0' + randomString() + '\u000A' + randomString() + '\u000A' + '\u3164' + '\u00A0' + randomString() + '\u000A' + randomString() + '\u000A' + '\u3164' + '\u00A0' + randomString()
	# avoid tweets without raindrops
    if ',' in raintweet:
        chance = (random.randint(1, 100))
        if (chance <= probability):
            api.update_status(raintweet)
        break
