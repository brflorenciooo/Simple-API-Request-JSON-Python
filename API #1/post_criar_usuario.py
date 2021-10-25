import requests
from pprint import pprint
_print = print
print = pprint

url = 'http://127.0.0.1:3001/users'

user_data = {
	"nome": "Bruno Florencio",
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
    # print('content',response.content)
else:    
    print(response.status_code)
    print(response.reason)
    print(response.text)
    print(response.json())
    #preguiça de colocar os outros erros