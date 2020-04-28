
import requests
import hashlib
import string
import re
import csv
import io
import json


def dados_ckan (url):
    data = requests.get(url+"&limit=1000000").json()
    print (len (data["result"]["records"] ))
    return data["result"]["records"]


def dados_ufma (url):
    data = requests.get(url).json()
    return data["data"]




def hashcode (university, resource,  code):
  return hashlib.md5((university+resource+code).encode()).hexdigest()

s ="Estudo Comparativo de Estratégias de Controle Aplicadas a um Gerador Síncrono"

def removeNonUTF8 (s):
    #return bytes(s, 'utf-8').decode('utf-8', 'ignore')
    return ''.join(x for x in s if x in string.printable)
    #return str(bytes(s, 'utf-8').decode('cp1252').encode('utf-8'))

def remove_unicode(string_data):
    """ (str|unicode) -> (str|unicode)

    recovers ascii content from string_data
    """
    if string_data is None:
        return string_data

    if isinstance(string_data, bytes):
        string_data = bytes(string_data.decode('ascii', 'ignore'))
    else:
        string_data = string_data.encode('ascii', 'ignore')

    remove_ctrl_chars_regex = re.compile(r'[^\x20-\x7e]')


def dados_csv (url, delimiter=","):
    r = requests.get(url, verify=False)
    encoding = r.encoding or "Utf-8"
    #print (encoding)
    file = r.text
    file = file.encode(encoding).decode( 'utf-8')
    reader = csv.DictReader(io.StringIO(file), delimiter=delimiter)
    data = json.dumps(list(reader))
    return json.loads(data)

def dados_iffar(url):
    data = requests.get(url).json()
    print(data["info"])
    return data["data"]