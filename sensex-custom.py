from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
from time import sleep
from datetime import datetime
import webbrowser
import urllib.request as urllib2
def get_news():
    url="http://money.cnn.com/data/world_markets/asia"
    req = urlopen(url)
    page = req.read();
    scraping = BeautifulSoup(page)
    print(scraping);
    scraping.find("div", { "class" : "cnnBody_Right" })['style'] = "display:none"
    scraping.find("div",{"class":"cnnBody_Left wsodContent"})['style']="width:1024px;height:1024px"
    scraping.find("div",{"id":"wsod_worldMarkets"})['style']="width:1024px;height:1024px"
    scraping.find("iframe", {"src":"http://markets.money.cnn.com/worldmarkets/map.asp?region=Asia"})['style']="width:1024px;height:1024px"
   # print("found ?" , scraping.find("div",{"class":"wsod_worldMarketsMapImage"}))
    print(scraping);
    with open("sensexdata.html","w") as f:
        f.write(str(scraping));
    
    

print("--------Sensex value - Python WebScraping project-------")
print("This sample project reads Sensex value from \"timesofindia.indiatimes.com/business\" Page and generates a output file too in your C:\output.txt")
print ("")
get_news();
