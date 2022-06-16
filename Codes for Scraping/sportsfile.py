import time

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq, Request
filename = "EXP_try-News_sports_urdu.csv"
f= open(filename,"w",encoding='utf-16')
headers = "news, date, Category\n"
#f = open(filename , "w" , encoding='utf-32')
f.write(headers)

import requests
n=1
while n <= 11:
   #print (n)
   m = str(n)
   url = "https://www.express.pk/sports/archives/?page=" + m
   responce = requests.get(url) #sir isme error aaraha tha then requests.get se data liya html ka
   #ul = Request('https://www.express.pk/sports/archives/?page='+ m +'/',headers={'User-Agent': 'Mozilla/5.0'})
   # uclien = uReq(ul)

   #
   # req = Request(
   #     'http://www.cmegroup.com/trading/products/#sortField=oi&sortAsc=false&venues=3&page=1&cleared=1&group=1',
   #     headers={'User-Agent': 'Mozilla/5.0'})
   # webpage = urlopen(req).read()
   #page = uclien.read()
   #uclien.close()
   html = responce.text
   psoup = soup(html, "html.parser")
   #print(psoup)
   containers = psoup.find_all("div",{"class":"meta"}) #major problem yaha hai sir ap bus isko theek krde JAZAK ALLAH
   #print(containers) #ap is print command ko chla kr dekhiye ga

   #sir ye aik tareeqa dekha tha mene:
   for con in containers:   #Now explore each title in the page
     ref = con.get('href')
     print(ref)
     uclen = requests.get(ref)

     psou = soup(uclen, "html.parser")
     if (psou.find("a", {"class": "span-16 story-content last mobile-story-content fix-l-r"})):  # find para class from page which contain abstracts
        coer = psou.find("a", {"class": "span-16 story-content last mobile-story-content fix-l-r"})
        coer = coer.getText()
        coer = coer.replace(",", " ")
        print(coer)

        try:
           f.write(coer + "\n")
        except:
           print("Exception")
   #[sir line 29 me agr hum a ko access krte hai without class then saray a aajatay hai or agr unka text liya jaye
   #to wo b ajata hai then usme line 33 ko uncomment krna hai or print krwana hai line 35 ko then required input aajati hhai
   #but in for loop wohi required output splitted form me aik aik harf ko display krti hai]
   #con=containers[25:]
   #daily = con
   #print(con)
# # # ##id-1806766 story  cat-0 group-0 position-0 cstoreyitem couplet clearfix first
#    for con in con:
#     daily=con
#     print(daily)
    # time1 = psoup.find("span" , {"class" : "timestamp"})
    # print(time1.text.strip())
    # cat= psoup.find("div", {"class" : "columnarstorey"})
    # print(cat.text.strip())
#     time2 = time1.text.strip()

#     #print(time2)
#       #time2 = time1.time.text.strip()
#     cat2 = cat.text.strip()
#
#
#     print(daily + " " + "," + " " + time2 + " " + "," + " " + cat2 + "\n")
#     #print(daily.replace("," ,"") + "," + time2 + "\n")
#     f.write(daily + " " + "," + " " + time2 + " " + "," + " " + cat2 + "\n")
#    #print (n)
#    n = n+1
# f.close()
# time.sleep(.25)