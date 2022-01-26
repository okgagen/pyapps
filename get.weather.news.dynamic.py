import sys
import json
import requests
from bs4 import BeautifulSoup
from newsapi import NewsApiClient

mycity = sys.argv[1]
mystate = sys.argv[2]
mycountry = sys.argv[3]
myweatherurl = "https://www.google.com/search?q="+"weather"+mycity+mystate+mycountry
my_api_key="148a6d1736a54dd9aa5b3b49e78be04a"
my_news_file="/var/lib/tomcat9/webapps/ROOT/mynews.html"

# Get Weather
html = requests.get(myweatherurl).content

myweatherrawdata = BeautifulSoup(html, 'html.parser')
mytemp = myweatherrawdata.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
mytemp = mytemp[:len(mytemp) - 2]
mytime = myweatherrawdata.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
mydata = mytime.split('\n')
mytime = mydata[0]
mysky = mydata[1]

# Get News
newsapi = NewsApiClient(api_key=my_api_key)

# /v2/top-headlines
top_headlines_raw = newsapi.get_top_headlines(sources=sys.argv[4])
top_headlines_articles = top_headlines_raw["articles"]

# Generate HTML
news_file = open(my_news_file, "w")
news_file.write("<html><br><header>GOOGLE WEATHER<br><br>")
news_file.write(mycity)
news_file.write("<br>")
news_file.write(mystate)
news_file.write("<br>")
news_file.write(mycountry)
news_file.write("<br>")
news_file.write(mytime)
news_file.write("<br>")
news_file.write(mytemp)
news_file.write("&#8457")
news_file.write("<br>")
news_file.write(mysky)
news_file.write("<br><br><br>NEWS HEADLINES FROM ")
news_file.write(sys.argv[4])
news_file.write("<br><br></header>")
news_file.close()

for i in range(len(top_headlines_articles)):
#  news_line=[top_headlines_articles[i]["title"], top_headlines_articles[i]["description"], top_headlines_articles[i]["url"]]
  news_line1=[top_headlines_articles[i]["title"], top_headlines_articles[i]["description"]]
  news_line1=json.dumps(news_line1)
  news_line1=news_line1[1: - 1]
  news_line2=top_headlines_articles[i]["url"]
  news_line2=json.dumps(news_line2)
  news_file = open(my_news_file, "a")
  news_file.write(news_line1)
  news_file.write("<a href=")
  news_file.write(news_line2)
  news_file.write(" target=\"_blank\"> Click To Read More </a>")
  news_file.write("<br><br>")
  news_file.close()

news_file = open(my_news_file, "a")
news_file.write("</html>")
news_file.close()

# /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                      sources='bbc-news,the-verge',
#                                      domains='bbc.co.uk,techcrunch.com',
#                                      from_param='2017-12-01',
#                                      to='2017-12-12',
#                                      language='en',
#                                      sort_by='relevancy',
#                                      page=2)

# /v2/top-headlines/sources
#sources = newsapi.get_sources()
