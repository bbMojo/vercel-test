import requests

create_url = "https://proxpiapi.herokuapp.com/new/create"


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InllRkRqam5ZbVhqUXRwV1VkbllYayJ9.eyJpc3MiOiJodHRwczovL3Byb3hwaS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDEzNDkzMTY0ODg0ODM1OTYzNzMiLCJhdWQiOlsiZnJlZHlzb215QGdtYWlsLmNvbSIsImh0dHBzOi8vcHJveHBpLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MjY4NDk1OTIsImV4cCI6MTYyNjkzNTk5MiwiYXpwIjoiRlhNTFd2VGVYMVFGNUZlalVEczZ1ZExDUEpOWFdnQW4iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIn0.M4VzuDA3bVZb04RFqRXyyvOorMsmX53FERGiXPRO_ERnMFs09X6mqazNWmI-PiTdpjRawg9Qfwl4rc2d94LLRdpCcYO35rQaygVTA51NtDExd5vC8mQ9QAlRmAL596JRwHURDTJsT8u-PAeHBGwXQOD5bSgO8Hg9bqWlUb3VwrS9ZKDfKz_RgODwGUeH8ukvZJyuZEgzZB0mTXFMfe5heFoirGSyF6i3aacCRj4R3-TfyiLdx-qYhCfdgdxJ_V5QomoCEL5YoNQpaHZqFu1FzLEah2Uzzf_E-8QgaI07CmShorT6KPEK5H7yHRHlE81c6FEEPoV43wnsEvcQxsfusw",
    "Connection": "keep-alive",
    "Content-Length": "438",
    "Content-Type": "application/json;charset=UTF-8",
    "Host": "proxpiapi.herokuapp.com",
    "Origin": "https://proxpiapp.vercel.app",
    'Referer': "https://proxpiapp.vercel.app/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "Sec-GPC": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
}

body = {
    "body": {"name": "a_cli_made", "method": "GET", "access": "public", "url": "my_endpoints"},
    "email": "adwaithrajesh3180@gmail.com",
    "email_verified": "true",
    "family_name": "Rajesh",
    "given_name": "Adwaith",
    "locale": "en",
    "name": "Adwaith Rajesh",
    "nickname": "adwaithrajesh3180",
    "picture": "https://lh3.googleusercontent.com/a-/AOh14GiM3ckaRh3hWzas28d1YQBd7WtFraH6mtEHXaAw=s96-c",
    "sub": "google-oauth2|101349316488483596373",
    "updated_at": "2021-07-20T16:56:27.586Z"
}


rv = requests.post(create_url, data=body, headers=headers)
print(rv)
print(rv.text)
