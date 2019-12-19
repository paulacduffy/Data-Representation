import requests
from bs4 import BeautifulSoup
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print (page)
#print ("--------------")
#print (page.content)
soup1 = BeautifulSoup(page.content, 'html.parser')
#print ("---------------")
#print (soup1.prettify())
with open("lab2.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
#print (soup.tr)
rows = soup.findAll("tr")
for row in rows:
    #print("---------")
    #print(row)
    
    datalist = [] 
    cols = row.findAll("td")   
    for col in cols:
        datalist.append(col.text)
    print(datalist)
