# -*- coding: utf-8 -*-

import csv
from bs4 import BeautifulSoup
#from urllib.request import urlopen
import requests
url = "https://www.zaubacorp.com/company/DR-REDDY-S-LABORATORIES-LTD/L85195TG1984PLC004507"
dense = 5


def searchDepth(url,depth):
    #html = urlopen(url)
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'lxml')
    type(soup)
    index = 1
    while 1:
        directorRow = soup.find("tr", { "id" : "package"+str(index) })
        if not directorRow :
            break
        directorDetails(directorRow ,depth)
        next_td_tag = directorRow.findNext('table').find_all("tr")
        depth = depth - 1
        if depth > 0:
            for i in next_td_tag[1:]: 
                if (i.p.a) :
                    searchDepth(i.p.a.get("href"), depth)
        depth = depth + 1
        index = index + 1

def directorDetails(directorRow,depth):
    director = directorRow.findAll("td")
    URL = director[1].p.a.get('href')
    DIN = director[0].p.contents[0]
    directorName = director[1].p.a.contents[0]
    designation =  director[2].p.contents[0]
    appointmentDate =  director[3].p.contents[0]
    print("current depth: "+str(depth) +"  " + directorName )
    writeCSV(URL,DIN,directorName,designation,appointmentDate,depth)
        
def writeCSV(a,b,c,d,e,f):
    row = [a,b,c,d,e,f]            
    with open('directorDepth'+str(f)+'.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()    

searchDepth(url,dense)



 
