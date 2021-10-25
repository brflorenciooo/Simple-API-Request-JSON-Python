import requests
from requests.models import Response

url = 'http://localhost:3001/images/1588529894017_11362.png'
nome_arquivo = url.split('/')[-1]

response = requests.get(url)

if response.status_code >= 200 and response.status_code <= 299:
    #sucesso
    print(response.status_code)
    print(response.reason)
    
    # print('content',response.content)

    with open(nome_arquivo,'wb') as file:
        file.write(response.content)

else:    
    print(response.status_code)
    print(response.reason)
    
    