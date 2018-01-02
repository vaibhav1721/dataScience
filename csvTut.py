import pandas
import json
from os import getcwd

# baseball_data = pandas.read_csv("AllstarFull.csv");

# print baseball_data[['playerID','yearID']]
import requests as requests

#url = "http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=513832d18b5a53695d320ff8a230aab5&format=json"
#data = requests.get(url).text
#data = json.loads(data)
#print type(data)
#print data['topartists']['artist'][0]['name']

url2 = "http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=513832d18b5a53695d320ff8a230aab5&artist=Cher&album=Believe&format=json"
data1 = requests.get(url2).text
data1 = json.loads(data1)
print type(data1)
print data1['album']['artist']