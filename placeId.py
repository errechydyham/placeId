import urllib.request, urllib.parse, urllib.error 
import json 

a = "http://py4e-data.dr-chuck.net/json?"

while True: 
    address = input("Enter location: ")

    #break the loop if the user didn't enter a location 
    if len(address) < 1: break 

    #add the location to the API url 
    u = a + urllib.parse.urlencode({'address': address}) 

    #connect with the API + read the data 
    n = urllib.request.urlopen(u)
    data = n.read().decode()  

    #organize the json data 
    try: 
        j = json.loads(data)
    except: 
        j = None 
