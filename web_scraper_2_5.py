import requests
import json
from bs4 import BeautifulSoup

url = input("Input the URL:\n")
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")
try:
    x = json.loads("".join(soup.find("script",  {"type":"application/ld+json"}).contents))
    u = x.get("name")
    v = x.get("description")
    dict = {"title": u, "description": v}
    if x.get("@type") == "Person":
        print('Invalid movie page!')
    else:
        print(dict)
except AttributeError:
    print("Invalid movie page!")


#https://www.imdb.com/name/nm0001191/
#https://www.imdb.com/title/tt10048342/
#https://www.imdb.com/title/tt0080684/
