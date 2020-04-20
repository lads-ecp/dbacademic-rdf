
import requests
import hashlib

def dados_sigaa (url):
    data = requests.get(url+"&limit=1000000").json()
    print (len (data["result"]["records"] ))
    return data["result"]["records"]


def dados_ufma ():
    url = "https://dados-ufma.herokuapp.com/api/v01/docente/"
    data = requests.get(url).json()
    return data["data"]


def hashcode (university, code):
  return hashlib.md5((university+code).encode()).hexdigest()
