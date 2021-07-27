import requests  #import os
from datetime import datetime

api_key = '1b7f5791bcd5a25e2fa4568dc27cf275'
print('*********************** LIVE WEATHER FORCAST ***************************')
print('\n')
location = input("Enter the city name you want to know: ")
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()
#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
min_temp_city = ((api_data['main']['temp_min']) - 273.15)
max_temp_city = ((api_data['main']['temp_max']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
prssre = api_data['main']['pressure']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("------------------------------------------------------------------------")
print ("Weather Stats of - {}  || {}".format(location.upper(), date_time))
print ("------------------------------------------------------------------------")

print ("Current temperature is: {:.2f} degree C".format(temp_city))
print ('Minimum temperature this day: {:.2f} degree C'.format(min_temp_city))
print ('Maximum temperature this day: {:.2f} degree C'.format(max_temp_city))
print ("Current weather description:",weather_desc)
print ("Current Humidity in percentage:",hmdt, '%')
print ("Current wind speed in kmph:",wind_spd ,'kmph')
print ("Atmospheric Pressure in bars:",prssre ,'bars')

print("=========================================================================")
print('\n')

print('************************* THANKS FOR CHECKING ****************************')

# making a list so that i can print the info to a txt 
txtlist = [temp_city,min_temp_city,max_temp_city,weather_desc,hmdt,wind_spd,prssre,date_time]
#using open() buit-in function to write to a text file
with open("textfile.txt" , mode= 'w' ,encoding= 'utf-8') as f :     
                                     #encoding = utf-8 for linux and cp1252 for win
    f.write("------------------------------------------------------------------------ \n ")   
    f.write("Weather Stats of - {}  || {}".format(location.upper(), date_time))
    f.write("\n ------------------------------------------------------------------------ \n")
    f.write("Current temperature is:  degree C\n".format(txtlist[0]))
    f.write("Minimum temperature this day:  degree C\n".format(txtlist[1]))
    f.write("Maximum temperature this day:  degree C\n".format(txtlist[2]))
    f.write("{},{} \n".format("Current weather description:" ,txtlist[3]))
    f.write("{},{},{} \n".format("Current Humidity in percentage:",txtlist[4],"%"))
    f.write("{},{},{} \n".format("Current wind speed in kmph:",txtlist[5],"kmph"))
    f.write("{},{},{} \n".format("Atmospheric Pressure in bars:",txtlist[6],"bars"))
    f.write("\n ========================================================================= \n")

