import requests

params = {
    "userid": 1,
    "username": "admin",
    "userpassword": "admin",
    "isadmin": 1
}
method = "get"
url = "http://localhost:8092/BookManager/user/login"
data = {
    
    "userid": 1,
    "username": "admin",
    "userpassword": "admin",
    "isadmin": 1
}
r = requests.request(method,url,json=data)
print(r.text)