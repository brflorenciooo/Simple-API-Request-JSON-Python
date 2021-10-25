import mimetypes
import requests
from pprint import pprint
from mimetypes import MimeTypes
from requests_toolbelt import MultipartEncoder

from requests.api import head
from get_token import token

_print = print
print = pprint

mimetypes = MimeTypes()

nome_arquivo = 'python.png'
mimetype_arquivo = mimetypes.guess_type(nome_arquivo)[0]

multipart = MultipartEncoder(fields={
    'aluno_id': '1',
    'foto': (nome_arquivo, open(nome_arquivo, 'rb'), mimetype_arquivo)
})


url = 'http://127.0.0.1:3001/fotos'

headers = {
    'Authorization': token,
    'Content-Type': multipart.content_type
}

response = requests.post(url=url, headers=headers )

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