
import csv
import json
import requests

f = open("/home/sergio/Insync/sergio.costa@ecp.ufma.br/Google Drive/NewDrive/projetos/dbacademic/papers/ibicit2020/dados/universidades_dbpedia.csv","r+",encoding="utf-8") 
reader = csv.DictReader(f, delimiter=",")
data = json.dumps(list(reader))
ufs = json.loads(data)



for u in ufs:
    r = requests.get(u["URL_DBPEDIA"]+"?output=application%2Frdf%2Bxml")
    rdf = open("rdf/"+u["SIGLA"]+".rdf","w+",encoding="utf-8")
    rdf.write(r.text)
    rdf.close()


f.close()
