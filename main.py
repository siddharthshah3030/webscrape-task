# -*- coding: utf-8 -*-

import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.zaubacorp.com/company/DR-REDDY-S-LABORATORIES-LTD/L85195TG1984PLC004507"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
type(soup)

dense = 5

def searchDepth():
    depth = 1
    index = 1
    layerEnd = False
    while layerEnd == False:
        directorRow = soup.find("tr", { "id" : "package1" })
        director = directorRow.findAll("td")
        URL = director[1].p.a.get('href')
        DIN = director[0].p.contents[0]
        directorName = director[1].p.a.contents[0]
        designation =  director[2].p.contents[0]
        appointmentDate =  director[3].p.contents[0]
        print(URL)
        writeCSV(URL,DIN,directorName,designation,appointmentDate,depth)
def writeCSV(a,b,c,d,e,f):
    row = [a,b,c,d,e,f]            
    with open('people2.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()    




 