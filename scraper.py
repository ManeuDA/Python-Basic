import requests
from bs4 import BeautifulSoup
import ssl
import urllib.request
import urllib.error

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

response = requests.get(
	url="https://de.wikipedia.org/wiki/Liste_der_Museen_in_M%C3%BCnchen",
)
print(response.status_code)

url = input("Enter - ")
if len(url) < 1:
    url = "https://de.wikipedia.org/wiki/Liste_der_Museen_in_M%C3%BCnchen"

html_handle = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html_handle, "html.parser")
# print(soup)
span = soup.find_all("span")
museumlist=[]
for id in span:
    if id.get('id') is None: continue
    museumid = id.get('id')
    museumid = str(museumid)
    newmuseumid = museumid.replace("_", " ")
    museumlist.append(newmuseumid)
print(museumlist)


with open('nbgwiki.txt', 'w') as f:
    for line in museumlist:
        f.write(line)
        f.write('\n')