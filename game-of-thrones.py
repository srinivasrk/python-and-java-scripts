from bs4 import BeautifulSoup
from selenium import webdriver
import urllib;
from selenium.webdriver.common.keys import Keys
from urllib.request import Request, urlopen
from urllib.request import urlopen
from time import sleep
import re
import os
import time
from datetime import datetime
import webbrowser
linkdata="";
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 
req = Request('https://eztv.ag/search/game-of-thrones',None, headers);
webpage = urlopen(req).read()

scraping = BeautifulSoup(webpage,"html.parser");

for link in scraping.findAll('a'):
	if( 's06e01' in link['href']):
		if('hdtv-x264-killers' in link['href']):
                    linkdata = link['href'];

if(linkdata != ""):
    req = Request('https://eztv.ag/'+linkdata,None,headers);
    webpage = urlopen(req).read()
    scraping = BeautifulSoup(webpage,"html.parser");
    
    for link in scraping.findAll('a'):
        if('.torrent' in link['href']):
            print(link['href']);
            os.system('wget -O gameofthroness06e011.torrent '+link['href']);
            break;
            #urllib.request.urlretrieve ("https://eztv.ag/"+linkdata, "gameofthroness06e01.torrent")
            #r = Request('https://eztv.ag/'+linkdata, None,headers);
            #with open("gotTorrent.torrent", 'wb') as f:
                #r.raw.decode_content = True
                #shutil.copyfileobj(r.raw, f)