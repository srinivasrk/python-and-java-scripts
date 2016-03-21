from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib2 import Request
from urllib2 import urlopen
from time import sleep
import time
from datetime import datetime
import webbrowser

driver = webdriver.Firefox()
driver.get('file://' + "c:\sensexdata.html")

def get_news():
    url="http://money.cnn.com/data/world_markets/asia"
    req = urlopen(url)
    page = req.read();
    scraping = BeautifulSoup(page,"html.parser")
    #scraping.find("div", { "class" : "cnnBody_Right" })['style'] = "display:none"
    #scraping.find("div",{"class":"cnnBody_Left wsodContent"})['style']="width:1024px;height:1024px"
    #scraping.find("div",{"id":"wsod_worldMarkets"})['style']="width:1024px;height:1024px"
    #scraping.find("iframe", {"src":"http://markets.money.cnn.com/worldmarkets/map.asp?region=Asia"})['style']="width:1024px;height:1024px"
   # print("found ?" , scraping.find("div",{"class":"wsod_worldMarketsMapImage"}))
    for link in scraping.findAll('iframe'):
            if(link['src'].startswith('http://markets.money.cnn.com/worldmarkets')):
                sourcelink = link['src']
    req = urlopen(sourcelink)
    scraping = BeautifulSoup(req,"html.parser");
    scraping.find("body",{"class":"wsodContent"})['style']="zoom:1.5"
    scraping.find("body",{"class":"wsodContent"})['style']="-ms-zoom: 1.5;-webkit-zoom: 1.5;-moz-transform:  scale(1.9,1.9);transform-origin:0 0",
    "-moz-transform-origin: left center;"
   
    #print(scraping);
    with open("c:\sensexdata.html","w") as f:
        f.write(str(scraping));
   # webbrowser.open('file://' + "c:\sensexdata.html")
    driver.refresh()
    
    

print("--------Sensex value - Python WebScraping project-------")
print("This sample project reads Sensex value from \"timesofindia.indiatimes.com/business\" Page and generates a output file too in your C:\output.txt")
print ("")
while True:
    get_news();
    time.sleep(5);


