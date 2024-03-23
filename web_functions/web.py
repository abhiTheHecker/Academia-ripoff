import requests


def get_token(username: str = "", password: str = "") -> dict:
    """'username': 'Username without @srmist.edu.in'\n'password': 'password'\n """
    data = {
        "username": username,
        "password": password
    }

    token_url = "https://academia-s-2.azurewebsites.net/login"

    res = requests.post(url=token_url, json=data, timeout=100)
    token = res.json()
    return token


def get_data(token_dict) -> dict:
    """Input: The token(which is a dictionary btw) obtained from get_token\nOutput: Returns the academic data of the user in the form of a dictionary"""
    headers = {
        "X-Access-Token": token_dict['token'],
        "Origin": "https://a.srmcheck.me",
        "Accept": "*/*",
        "Referer": "https://a.srmcheck.me/"
    }

    url = "https://academia-s-2.azurewebsites.net/course-user"

    res = requests.post(url=url, headers=headers, timeout=100)
    return dict(res.json())


# token = get_token("netid", "password")
# print(get_data(token_dict=token))
