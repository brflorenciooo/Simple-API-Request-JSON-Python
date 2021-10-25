import requests
from pprint import pprint
_print = print
print = pprint

url = 'http://127.0.0.1:3001/tokens'

user_data = {
	"password": "123456",
	"email": "bruno@gmail.com"
}

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    #sucesso
    print(response.status_code)
    print(response.reason)
    print(response.text)
    print(response.json())

    response_data = response.json()
    token = response_data['token']

    with open('token.txt', 'w') as file:
        file.write(token)

    # print('content',response.content)
else:    
    print(response.status_code)
    print(response.reason)
    print(response.text)
    print(response.json())
    #preguiça de colocar os outros erros