import requests
from pprint import pprint
def weather_data(query):
	res=requests.get('http://api.openweathermap.org/find?'+query);
	return res.json();
def print_weather(result,city):
	print("{}'s temperature: {}°C ".format(city,result['main']['temp']))
	print("Wind speed: {} m/s".format(result['wind']['speed']))
	print("Description: {}".format(result['weather'][0]['description']))
	print("Weather: {}".format(result['weather'][0]['main']))
def main():
	city=str(input('Enter the city:'))
	print()
	try:
	  query='q='+city;
	  w_data=weather_data(query);
	  print_weather(w_data, city)
	  print()
	except:
	  print('City name not found...')
if __name__=='__main__':
	main()