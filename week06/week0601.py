import requests
import json
from xlwt import *
url = "http://127.0.0.1:5000/cars"
response = requests.get(url)
data = response.json()
#output to console
#print (data)
for car in data["cars"]:
    #print(car)
    filename =  'cars.json'
    if filename:
        with open(filename, 'w') as f:
            json.dump(data, f, indent = 4)

w = Workbook()
ws = w.add_sheet('cars')
row = 0;
ws.write(row,0,"reg")
ws.write(row,1,"make")
ws.write(row,2,"model")
ws.write(row,3,"price")
row += 1
for car in data["cars"]:
 ws.write(row,0, car["reg"])
 ws.write(row,1,car["make"])
 ws.write(row,2,car["model"])
 ws.write(row,3,car["price"])
 row += 1
w.save('cars.xls')

dataString = {'reg':'08 C 1234','make':'Ford','model':'Galaxy','price':12324}
url = 'http://127.0.0.1:5000/cars'
response = requests.post(url, json=dataString)
#print (response.status_code)

dataString = {'make':'Ford','model':'Kuga'}
url = 'http://127.0.0.1:5000/cars/test'
response = requests.put(url, json=dataString)
#print (response.status_code)
#print (response.text)

url = 'http://127.0.0.1:5000/cars/08%20C%201234'
response = requests.delete(url)
#print (response.status_code)
print (response.text)

url = "https://api.github.com/users/andrewbeattycourseware/followers"
response = requests.get(url)
data = response.json()
#print(data)
#Get the file name for the new file to write
for githubuser in data["githubusers"]:
    filename = 'githubusers.json'
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

w = Workbook()
ws = w.add_sheet('githubusers')
row = 0;
ws.write(row,0,"login")
ws.write(row,1,"id")
ws.write(row,2,"node_id")
ws.write(row,3,"avatar_url")
row += 1
for githubuser in data["githubusers"]:
 ws.write(row,0, githubuser["login"])
 ws.write(row,1,githubuser["id"])
 ws.write(row,2,githubuser["node_id"])
 ws.write(row,3,githubuser["avatar_url"])
 row += 1
w.save('githubusers.xls')




