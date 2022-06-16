from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
filename = "daily_news_bussiness_5.csv"
f= open(filename,"w",encoding='utf-16')
headers = "news, date \n"
#f = open(filename , "w" , encoding='utf-32')
f.write(headers)
'''n=601
while n <=700:
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/business/page'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      #daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=701
while n <=800 :
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/business/page'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      #daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=801
while n <=900 :
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/business/page'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      #daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=901
while n <=1000 :
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/business/page'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      #daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(time2.replace("," ,"") + "\n")   
      print (n)
      n = n+1
n=1001
while n <=1100 :
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/business/page'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      #daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=1101
while n <=1200 :
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/business/page'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      #daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=1230
while n <=1300 :
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/business/page'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      #daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=1301
while n <=1400 :
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/business/page'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      #daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=1401
while n <=1500 :
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/business/page'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      #daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=1501
while n <=1600 :
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/business/page'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      #daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
   n=1601'''
while n <=1700 :
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/business/page'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      #daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=1701
while n <=1800 :
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/business/page'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      #daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=1801
while n <=1900 :
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/business/page'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      #daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=1901
while n <=2000 :
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/business/page'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      #daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=2001
while n <=2100 :
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/business/page'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      #daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=2101
while n <=2200 :
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/business/page'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      #daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=2201
while n <=2300 :
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/business/page'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      #daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
n=2301
while n <=2320 :
   #print (n)
   m = str(n)
   ul = 'https://dailytimes.com.pk/business/page'+ m +'/' 
   uclien = uReq(ul)

   page = uclien.read()

   uclien.close()

   psoup = soup(page, "html.parser")

   containers = psoup.find_all("h2" , {"class" : "entry-title"})
   con = containers[0]
   for con in containers:
      #daily = con.text.strip()
      time1 = psoup.find_all("p" , {"class" : "entry-meta"})
      time2 = time1[0].time.text.strip()
      #print(daily + " " + "," + " " + time2 + "\n")
      #print(daily.replace("," ,"") + "," + time2 + "\n")
      f.write(time2.replace("," ,"") + "\n")
   print (n)
   n = n+1
f.close()