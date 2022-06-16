from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq
import requests
import lxml
from urllib.request import urlopen as uReq
import string
import re
import json
import time
filename = "daily_news_pk_1.csv"
f= open(filename,"w")
headers = "news,date \n"
f = open(filename , "w")
#Sf.write(headers)
'''n=1
while n <= 100:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=101
while n <= 200:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=201
while n <= 300:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=301
while n <= 400:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=401
while n <= 500:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=501
while n <= 600:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=601
while n <= 700:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=701
while n <= 800:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=801
while n <= 900:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=901
while n <= 1000:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=1001
while n <= 1100:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=1101
while n <= 1200:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=1201
while n <= 1300:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=1301
while n <= 1400:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=1401
while n <= 1500:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=1501
while n <= 1600:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1'''
n=1675
while n <= 1700:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=1701
while n <= 1800:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=1801
while n <= 1900:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=1901
while n <= 2000:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=2001
while n <= 2100:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=2101
while n <= 2200:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=2201
while n <= 2300:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=2301
while n <= 2400:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=2401
while n <= 2500:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=2501
while n <= 2600:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=2601
while n <= 2700:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=2701
while n <= 2800:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=2801
while n <= 2900:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=2901
while n <= 3000:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=3001
while n <= 3100:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=3101
while n <= 3200:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=3201
while n <= 3300:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=3301
while n <= 3400:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=3401
while n <= 3500:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=3501
while n <= 3600:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=3601
while n <= 3700:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=3701
while n <= 3800:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=3801
while n <= 3840:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/pakistan/page/'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(daily.replace("," ,"") + "," + time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
f.close()
time.sleep(.25)