import requests
from pprint import pprint

from requests.api import head
from get_token import token

_print = print
print = pprint

id = 2
url = f'http://127.0.0.1:3001/alunos/{id}'

headers = {
    'Authorization': token
}

aluno_data = {
	"nome": "Let",
	# "sobrenome": "Moreira",
	# "email": "luana@email.com",
	# "idade": "50",
	# "peso": "80.04",
	# "altura": "1.90"
}

response = requests.put(url=url, json=aluno_data, headers=headers)

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