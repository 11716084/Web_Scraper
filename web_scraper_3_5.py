import requests
import json
from bs4 import BeautifulSoup
import urllib.request


url = input("Input the URL:\n")
resp = requests.get(url)
if resp.status_code == 200:
    # soup = BeautifulSoup(resp.text, "html.parser")
    site = urllib.request.urlopen(url)
    data = site.read()
    file = open("source.html","wb") #open file in binary mode
    file.write(data)
    file.close()
    print("Content saved.")

else:
    print(f"The URL returned {resp.status_code}!")

#http://www.pythonchallenge.com/pc/def/0.html
#http://google.com/asdfg
#https://www.imdb.com/name/nm0001191/
#https://www.imdb.com/title/tt10048342/
#https://www.imdb.com/title/tt0080684/
