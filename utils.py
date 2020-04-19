
import requests

def dados_sigaa (url):
    data = requests.get(url).json()
    return data["result"]["records"]


def dados_ufma ():
    url = "https://dados-ufma.herokuapp.com/api/v01/docente/"
    data = requests.get(url).json()
    return data["data"]

