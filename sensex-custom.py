from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib2 import Request
from urllib2 import urlopen
from time import sleep
import re
import time
from datetime import datetime
import webbrowser

driver = webdriver.Firefox()
try:
    driver.get('file://' + "customsensexdata.html") # for windows put c:\
except Exception:
    open("customsensexdata.html",'w')
    driver.get('file://' + "customsensexdata.html") # for windows put c:\




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
    
    start = re.search('id="wsod_index_USN"',str(scraping))
    startpos = start.start(0)-29

    newtag = '<div id="wsod_index_USN class="wosd_boxOverlay""style="top:125px;left:400px;"><div class="wsod_boxIndexName">S&amp;P 500<span><span stream="changePct_575769"><span class="posData">+0.15%</span></span></span></div><div class="wsod_boxIndexTime">US - Closes in 1h</div></div>'
    temp = str(scraping)
    print (temp[:startpos])
             
    #print(scraping);
    with open("customsensexdata.html","w") as f: # for windows put c:\
        #f.write(str(scraping));
        f.write(str(scraping))
   # webbrowser.open('file://' + "c:\sensexdata.html")
    driver.refresh()
    
    

print("--------Sensex value - Python WebScraping project-------")
print("This sample project reads Sensex value from \"timesofindia.indiatimes.com/business\" Page and generates a output file too in your C:\output.txt")
print ("")
while True:
    get_news();
    time.sleep(5);


