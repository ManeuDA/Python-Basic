#Scraping Numbers from HTML using Beautiful Soup
#Your to find all the <span>tags in the file and pull out the numbers from the tag and sum the numbers.
#You need to adjust this code to look for span tags and pull out the text content of the span tag, convert them to
#integers and add them up to complete the assignment
#Python code ends with 74

import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

web_address = input("Enter - ")
if len(web_address) < 1:
    web_address = "http://py4e-data.dr-chuck.net/comments_1377692.html"
html_handle = urllib.request.urlopen(web_address, context=ctx).read()       # socket
soup_parse = BeautifulSoup(html_handle, "html.parser")                      # open with bs4 using html.parser
# print(soup_parse)

find_data = soup_parse.find_all('td')       # find data 'td'
# print(find_data)
numbers = []                                # creating empty list
for text in find_data:                      # a loop for text in data
    text = str(find_data)                   # text is string in data
    file_number = re.findall('[0-9]+', text)        # find numbers in data
print(file_number)
for number in file_number:                      # a loop number in numbers
    number = float(number)                      # number is float
    if number > 0:                              # number is higher than zero
        numbers.append(number)              # append the list
print(int(sum(numbers)))                # print sum as integer
