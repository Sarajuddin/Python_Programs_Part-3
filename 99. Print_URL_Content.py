# 99. Write a Python program to access and print a URL's content to the console.

# from http.client import HTTPConnection
# conn = HTTPConnection("https://www.w3resource.com")
# conn.request("GET", "/")  
# result = conn.getresponse()
# # retrieves the entire contents.  
# contents = result.read() 
# print(contents)


import requests
data = requests.get('https://www.w3resource.com')
print(data.text)
