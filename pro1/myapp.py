# username:hello , pass: hello


import requests
URL="http://127.0.0.1:8000/stuinfo/"

#  this application is seprate apllication he want connected api 
r=requests.get(url=URL)
data=r.json()
print(data)