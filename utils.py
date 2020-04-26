
import requests, csv, json, io
import hashlib

def dados_sigaa (url):
    data = requests.get(url+"&limit=1000000").json()
    print (len (data["result"]["records"] ))
    return data["result"]["records"]


def dados_ufma (url):
    data = requests.get(url).json()
    return data["data"]


def hashcode (university, code):
    return hashlib.md5((university+code).encode()).hexdigest()


def dados_csv (url):
    file = requests.get(url).text
    reader = csv.DictReader(io.StringIO(file))
    data = json.dumps(list(reader))
    return data