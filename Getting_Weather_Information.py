#first of all create an account on openweathermap.org to get an api for the current weather conditions
import requests #requests is a python library to send a request to a particular website
from pprint import pprint #when we send a request to the website it will send a response in json format 
                          #so pprint will make the json format readable and into a tree/list

API_Key ='09193d5dc10bb830e7e31626275b3a22' #specify a new variable of API key and get the individual API
                                            #key from the openwathermap website

city = input("Enter a city: ") #create a variable input 'city' for the user to enter

#the url is the url we are going to send the request/response to and we need to send it with the API key and city
base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city #concatenate the API key and city

weather_data = requests.get(base_url).json() #send a request to the url and get the response from the url which is in 
                                             #the json format 

pprint(weather_data) #use pprint to transform the json format to a readable format 