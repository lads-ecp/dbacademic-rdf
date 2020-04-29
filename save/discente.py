
from model import  Docente, Curso, Discente, Unidade, Monografia, GrupoPesquisa
from simpot import serialize_to_rdf_file, mapper_all, serialize_all_to_rdf

from utils import *

import requests

from save.instituicoes_pt import *

serialize_rdf_discentes = {

    "classType" : Discente,

    "collection" : [

        { ## ufrn
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome_discente", 
                    "id": lambda d: hashcode ("ufrn", "discente", d["matricula"]),
                    "code" : "matricula",
                    "university" : lambda d: UFRN,
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
                    "university" : lambda d: UFPI,
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
                    "university" : lambda d: UFMA,
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
                    "university" : lambda d: IFPA,
                    "code" : "Matrícula",
                    #"curso": lambda d: "https://www.dbacademic.tech/resource/" + hashcode ( "ufma", "curso", str (d["codigo_curso"]))
            },

            "data" : lambda :  dados_ckan("http://pda.ifpa.edu.br/api/action/datastore_search?resource_id=d422ed80-e077-492f-82dd-5827390b261f"),
            
            "rdf_path" : "rdf/discentes_ifpa.rdf"
        },

   


        { ## ifma
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome",
                    "university" : lambda d: IFMA, 
                    "id": lambda d: hashcode ("ifma", "discente", d["matricula"]),
                    "code" : "matricula",
                    "curso": lambda d: "https://www.dbacademic.tech/resource/" + hashcode ( "ifma", "curso", str (d["curso"].upper()))
            },

            "data" : lambda :  requests.get("https://dados.ifma.edu.br/dataset/7781a4cd-6b97-44bb-bb11-fa25498d8fe5/resource/19927338-28eb-4f11-beb0-971a614ea54b/download/ckan_alunos_20190730.json").json()
            ,
            
            "rdf_path" : "rdf/discentes_ifma.rdf"
        },

         { ## ifc
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "university" : lambda d: IFC,
                    "id": lambda d: hashcode ("ifc", "discente", d["nome"]),
                    "code" : lambda d: hashcode ("ifc", "discente", d["nome"]),
                    "curso": lambda d: "https://www.dbacademic.tech/resource/" + hashcode ( "ifc", "curso", str (d["curso"].upper()))
            },

            "data" : lambda :  filter ( lambda d: d["nivel"] == "GRADUAÇÃO", 
                    dados_csv ("http://dadosabertos.ifc.edu.br/pt_BR/dataset/d8dd8d6d-a4a7-444e-8b95-dba2095aa117/resource/c78fea00-2ba8-4df9-9b50-5bc1e7fb6075/download/discentes.csv")
            ),
            
            "rdf_path" : "rdf/discentes_ifc.rdf"
        },

        { ## ifpb
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "code": "matricula",
                    "university" : lambda d: IFPB,
                    "id" : "uuid",
                    "curso": lambda d: "https://www.dbacademic.tech/resource/" + d["curso"]["uuid"] ,

            }, 

            "data" :  lambda : 
                        requests.get("https://dados.ifpb.edu.br/dataset/d02eb6b8-5745-4436-ae22-ef1c182897d9/resource/61f5a0ad-642d-4580-ab62-1110318d0eea/download/alunos.json").json()
                    ,
            
            "rdf_path" : "rdf/discente_ifpb.rdf"
        },

        { ## ifms
            "toSave" : False,
            "mapper" : {
                    "nome" : "curso", 
                    "university" : lambda d: IFMS,
                    "code" : "ra",
                    "id": lambda d: hashcode ( "ifms", "discente", str(d["ra"])),
                    "university" : lambda d: IFMS,        
                    "curso": lambda d: "https://www.dbacademic.tech/resource/" + hashcode ( "ifms", "curso", str (d["curso"].upper()))
            },

            "data" : lambda : list ( filter ( lambda d: d["nivel_do_curso"] == "TECNOLOGIA",
                    dados_ckan("http://dados.ifms.edu.br/api/action/datastore_search?resource_id=b8b4dfdf-98ef-4d57-baff-75c163be6e9a"),
            )),
            
            "rdf_path" : "rdf/discente_ifms.rdf"
        },


        { ## ifrn
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "code": "matricula",
                    "university" : lambda d: IFRN,
                    "id" : lambda d: hashcode ("ifrn",  "discente", str(d["matricula"])),

            }, 

            "data" :  lambda :
                        requests.get("https://dados.ifrn.edu.br/dataset/d5adda48-f65b-4ef8-9996-1ee2c445e7c0/resource/00efe66e-3615-4d87-8706-f68d52d801d7/download/dados_extraidos_recursos_alunos-da-instituicao.json").json()
                ,
            
            "rdf_path" : "rdf/discentes_ifrn.rdf"
        },

             { ## iffar
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "university" : lambda d: IFFAR,
                    "id": lambda d: hashcode ("iffar", "discente", str(d["id_discente"])),
                    "code" : "id_discente",
                    "curso": lambda d: "https://www.dbacademic.tech/resource/" + hashcode ( "iffar", "docente", str (d["id_curso"]))
            },

            "data" : lambda :  dados_iffar("http://dados.iffarroupilha.edu.br/api/v1/alunos.json?nivel=T"),
            
            "rdf_path" : "rdf/discentes_iffar.rdf"
        },

    ]
}

serialize_all_to_rdf(serialize_rdf_discentes)

