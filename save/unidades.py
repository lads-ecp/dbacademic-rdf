
from model import  Docente, Curso, Discente, Unidade, Monografia, GrupoPesquisa
from simpot import serialize_to_rdf_file, mapper_all, serialize_all_to_rdf

from utils import dados_ckan, dados_ufma, hashcode

import requests


serialize_rdf_unidades = {

    "classType" : Unidade,

    "collection" : [

        { ## ufrn
            "toSave" : True,
            "mapper" : {
                    "nome" : "nome_unidade", 
                    "code" : "id_unidade",
                    "id": lambda d : hashcode ("ufrn", "centro",   d["id_unidade"]),
                    
                    "sameas" : lambda d: "https://sigaa.ufrn.br/sigaa/public/departamento/portal.jsf?id=" + str(d["id_unidade"]),                    


            },

            "data" : lambda : list (filter ( lambda d: d["tipo_unidade_organizacional"].find("CENTRO") > -1, dados_ckan("http://dados.ufrn.br/api/action/datastore_search?resource_id=3f2e4e32-ef1a-4396-8037-cbc22a89d97f") )),
            "rdf_path" : "rdf/unidades_ufrn.rdf"
        },

        { ## ufma
            "toSave" : True,
            "mapper" : {
                    "nome" : "nome", 
                    "id": lambda d : hashcode ("ufma", "centro",  d["codigo"]),
                    "code" : "codigo",
                    "diretor" : lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufma", "docente", d["siape_diretor"]),
                    "sameas" : "url_sigaa",                    
            },

            "data" : lambda : list ( filter ( lambda d: "siape_diretor" in d, requests.get("https://dados-live-ufma.herokuapp.com/api/v01/unidade/").json() )), # nao desconsiderar unidade sem siape do diretor
            "rdf_path" : "rdf/unidades_ufma.rdf"
        },

        { ## ufpel
            "toSave" : True,
            "mapper" : {
                    "nome" : "nome", 
                    "id": lambda d : hashcode ("ufma", "centro",  d["cod_unidade"]),
                    "code" : "cod_unidade",
                    "sameas" : "site",                    
            },

            "data" : lambda : dados_ckan("http://dados.ufpel.edu.br/api/action/datastore_search?resource_id=3cac9468-e23e-4cc7-a83f-de670520c902")
            "rdf_path" : "rdf/unidades_ufpel.rdf"
        },

    ]
}

serialize_all_to_rdf(serialize_rdf_unidades)

