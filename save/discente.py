
from model import  Docente, Curso, Discente, Unidade, Monografia, GrupoPesquisa
from simpot import serialize_to_rdf_file, mapper_all, serialize_all_to_rdf

from utils import dados_ckan, dados_ufma, hashcode

import requests

serialize_rdf_discentes = {

    "classType" : Discente,

    "collection" : [

        { ## ufrn
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome_discente", 
                    "id": lambda d: hashcode ("ufrn", "discente", d["matricula"]),
                    "code" : "matricula",
                    "curso": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufrn", "curso", str (d["id_curso"]))
            },

            "data" : lambda :  dados_ckan("http://dados.ufrn.br/api/action/datastore_search?resource_id=a55aef81-e094-4267-8643-f283524e3dd7"),
            
            "rdf_path" : "rdf/discentes_ufrn.rdf"
        },

        { ## ufpi
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome_discente", 
                    "id": lambda d: hashcode ("ufpi",  "discente", d["matricula"]),
                    "code" : "matricula",
                    "curso": lambda d: "https://www.dbacademic.tech/resource/" + hashcode ( "ufpi","curso", str (d["id_curso"]))
            },

            "data" : lambda :  dados_ckan("https://dados.ufpi.br/api/action/datastore_search?resource_id=20df1fac-f3f1-4344-a514-655bd251db2b"),
            
            "rdf_path" : "rdf/discentes_ufpi.rdf"
        },

        { ## ufma
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "id": lambda d: hashcode ("ufma", "discente", d["matricula"]),
                    "code" : "matricula",
                    "curso": lambda d: "https://www.dbacademic.tech/resource/" + hashcode ( "ufma", "curso", str (d["codigo_curso"]))
            },

            "data" : lambda :  dados_ufma("https://dados-ufma.herokuapp.com/api/v01/discente/"),
            
            "rdf_path" : "rdf/discentes_ufma.rdf"
        },


        { ## ifpa
            "toSave" : True,
            "mapper" : {
                    "nome" : "Nome", 
                    "id": lambda d: hashcode ("ifpa", "discente", d["Matrícula"]),
                    "code" : "Matrícula",
                    #"curso": lambda d: "https://www.dbacademic.tech/resource/" + hashcode ( "ufma", "curso", str (d["codigo_curso"]))
            },

            "data" : lambda :  dados_ckan("http://pda.ifpa.edu.br/api/action/datastore_search?resource_id=d422ed80-e077-492f-82dd-5827390b261f"),
            
            "rdf_path" : "rdf/discentes_ifpa.rdf"
        },

        { ## ifms
            "toSave" : False,
            "mapper" : {
                    "nome" : "Nome", 
                    "id": lambda d: hashcode ("ifpa", "discente", d["Matrícula"]),
                    "code" : "Matrícula",
                    #"curso": lambda d: "https://www.dbacademic.tech/resource/" + hashcode ( "ufma", "curso", str (d["codigo_curso"]))
            },

            "data" : lambda :  dados_ckan("http://dados.ifms.edu.br/api/action/datastore_search?resource_id=b8b4dfdf-98ef-4d57-baff-75c163be6e9a&limit=5"),
            
            "rdf_path" : "rdf/discentes_ifpa.rdf"
        },


        { ## ifma
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "id": lambda d: hashcode ("ifma", "discente", d["matricula"]),
                    "code" : "matricula",
                    "curso": lambda d: "https://www.dbacademic.tech/resource/" + hashcode ( "ifma", "curso", str (d["curso"].upper()))
            },

            "data" : lambda :  requests.get("https://dados.ifma.edu.br/dataset/7781a4cd-6b97-44bb-bb11-fa25498d8fe5/resource/19927338-28eb-4f11-beb0-971a614ea54b/download/ckan_alunos_20190730.json").json()
            ,
            
            "rdf_path" : "rdf/discentes_ifma.rdf"
        },

    ]
}

serialize_all_to_rdf(serialize_rdf_discentes)

