# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:01:52 2019

@author: 612383249
"""
import requests
import config

# TASK 1 - MAILGUN API
#--------------------------------------------------------------------------------------
   
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox485066fe7d7e405a81141ea7a7d4736d.mailgun.org/messages",
        auth=("api", config.mailgun_api_key),
        data={"from": "Excited User <harriet.ellis@bt.com>",
              "to": ["bar@example.com", "harriet.p.ellis@gmail.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})
    
    send_simple_message()
    

# TASK 2, 3 & 4 - OPEN WEATHER MAP API
#--------------------------------------------------------------------------------------
   
endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "London,UK", "units":"metric", "appid":config.openweather_api_key}

response = requests.get(endpoint, params = payload)

# this converts the data into JSON format
data = response.json()
print(data['main'])

# this prints the URL that requests sue to get a response to you
print(response.url)

# this prints the HTTP status code of the response
# 200 is good, 400 is bad
print(response.status_code)

# this prints the content type of the response
print(response.headers["content-type"])

#this prints the data you requested from the server
print(response.text)

# this prints a statement about the weather to the console
temperature = data['main']['temp']
name=data['name']
weather = data['weather'][0]['main']
print(u"It's {}C in {}, and the sky is {}.".format(temperature, name, weather))







