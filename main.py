import requests
from twilio.rest import Client

OWN_endpoint = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "318b390ed8a8c37d63ced08ebbca175e"
MY_LAT = "your  latitude"
MY_LONG = "your longitude"
account_sid = 'your_auth_taken'
auth_token = "your_ath_token"
parameters = {
    "lat":  MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
}
clear = False
cloud = False
response = requests.get(OWN_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["weather"][0]["id"]
print(weather_slice)
if int(weather_slice) == 800:
    clear = True
elif int(weather_slice)>800:
    cloud = True

if clear:

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='phone number',
        body = "today is hot 🥵 you better not go out🔥",
        to='+phone number'
    )

    print(message.status)
elif cloud:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='phone number',
        body="you better take care of your self it's cloudy today☁️☁️",
        to='phone number'
    )

    print(message.status)



