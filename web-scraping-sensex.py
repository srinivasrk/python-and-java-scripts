from BeautifulSoup import BeautifulSoup
from urllib2 import Request
from time import sleep
from datetime import datetime
from urllib2 import urlopen
def get_news():
    url="http://timesofindia.indiatimes.com/business"
    req = urlopen(url)
    page = req.read();
    scraping = BeautifulSoup(page)
    price = scraping.findAll("span",attrs={"class":"green14px"})[0].text
    return price

print("--------Sensex value - Python WebScraping project-------")
print("This sample project reads Sensex value from \"timesofindia.indiatimes.com/business\" Page and generates a output file too in your C:\output.txt")
print ""
with open("c:\output.txt","w") as f:
    for x in range(2,100):
        sNow = datetime.now().strftime("%I:%M:%S%p")
        f.write(" At {0}, The SenSex value is {1} \n".format(sNow,get_news()))
        print(" At {0}, The SenSex value is {1} \n".format(sNow,get_news()))
        sleep(1)
      
