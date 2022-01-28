import sys
import json
import requests
from bs4 import BeautifulSoup
from newsapi import NewsApiClient

# Get Weather Raw
def getweatherraw(rqsturl):

  rawresult = []
  html = requests.get(rqsturl).content

  rawhtmlcontent = BeautifulSoup(html, 'html.parser')

  return rawhtmlcontent

# Get Weather
def getweather(rqsturl):

  result = []
  html = requests.get(rqsturl).content

  rqstweatherrawdata = BeautifulSoup(html, 'html.parser')
  rspcitystate = rqstweatherrawdata.find('span', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
  result.append(rspcitystate)
  rsptemp = rqstweatherrawdata.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
  rsptemp = rsptemp[:len(rsptemp) - 2]
  result.append(rsptemp)
  rsptime = rqstweatherrawdata.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
  rspdata = rsptime.split('\n')
  rsptime = rspdata[0]
  result.append(rsptime)
  rspsky = rspdata[1]
  result.append(rspsky)

  return result

# Get News Raw
def getheadlinearticlesraw(client_api_key, newssource):

  newsapi = NewsApiClient(api_key=client_api_key)

  # /v2/top-headlines
  top_headlines_raw = newsapi.get_top_headlines(sources=newssource)
  top_headlines_articles = top_headlines_raw["articles"]

  return top_headlines_articles

# Get News
def getheadlinearticles(client_api_key, newssource):

  result = []
  newsapi = NewsApiClient(api_key=client_api_key)

  # /v2/top-headlines
  top_headlines_raw = newsapi.get_top_headlines(sources=newssource)
  top_headlines_articles = top_headlines_raw["articles"]

  return result
