import requests

data = {
    "username" : "Username without @srmist.edu.in",
    "password" : "password"
}

headers = {
    "Content-Type": "application/json", "Accept": "application/json"
}

token_url = "https://academia-s-2.azurewebsites.net/login"

res = requests.post(url=token_url, json=data)
print(res.text)

