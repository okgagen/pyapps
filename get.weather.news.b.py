import sys
import json
import requests
from bs4 import BeautifulSoup
from newsapi import NewsApiClient
import hpma

mycity = sys.argv[1]
mystate = sys.argv[2]
mycountry = sys.argv[3]
mynewssource = sys.argv[4]
myweatherurl = "https://www.google.com/search?q="+"weather"+mycity+mystate+mycountry
my_api_key="148a6d1736a54dd9aa5b3b49e78be04a"
my_news_file="/var/lib/tomcat9/webapps/ROOT/mynews.html"

# Get Weather
myweatherrawdata=hpma.getweather(myweatherurl)
print(type(myweatherrawdata))
print(myweatherrawdata)
print(myweatherrawdata[0])
print(myweatherrawdata[1])
print(myweatherrawdata[2])
print(myweatherrawdata[3])

# Get Weather Raw
#myweatherrawcontent=hpma.getweatherraw(myweatherurl)
#print('\n', myweatherrawcontent)

# Get News
mynewsheadlinerawcontent=hpma.getheadlinearticlesraw(my_api_key, mynewssource)
print(type(mynewsheadlinerawcontent))
#print(mynewsheadlinerawcontent)
newsarticles = []
for i in range(len(mynewsheadlinerawcontent)):
  newsarticles.append(mynewsheadlinerawcontent[i])
  print(type(newsarticles[i]))
  print(newsarticles[i]["source"])
  print(newsarticles[i]["author"])
  print(newsarticles[i]["title"])
  print(newsarticles[i]["description"])
  print(newsarticles[i]["url"])
  print(newsarticles[i]["urlToImage"])
  print(newsarticles[i]["publishedAt"])
  print(newsarticles[i]["content"])
#  newsarticles[i]=json.dumps(newsarticles[i])
#  print(type(newsarticles[i]))
#  print(newsarticles[i])
