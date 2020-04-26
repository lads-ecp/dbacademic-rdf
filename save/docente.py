from model import  Docente, Curso, Discente, Unidade, Monografia, GrupoPesquisa
from simpot import serialize_to_rdf_file, mapper_all, serialize_all_to_rdf

from utils import dados_ckan, dados_ufma, hashcode
import requests

sexo_dict = {
    'F' : 'Male',
    'M' : 'Female'
}


serialize_rdf_docentes = {

    "classType" : Docente,

    "collection" : [

        { ## ufrn
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "id" : lambda d: hashcode ("ufrn", "docente", d["siape"]),
                    "siape": "siape",
                    "formacao" : "formacao",
                    "sameas" : lambda d: "https://sigaa.ufrn.br/sigaa/public/docente/portal.jsf?siape=" + d["siape"],
                    #"sexo": lambda d: sexo_dict[d["sexo"]],
                    "unidade": lambda d: "https://www.dbacademic.tech/resource/" + hashcode ( "ufrn", "departamento", str (d["id_unidade_lotacao"]))  
            },

            "data" : lambda :  dados_ckan("http://dados.ufrn.br/api/action/datastore_search?resource_id=ff0a457e-76fa-4aca-ad99-48aebd7db070"),
            
            "rdf_path" : "rdf/docentes_ufrn.rdf"
        },


        { ## unifespa
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome_servidor", 
                    "siape": "vinculo_servidor",
                    "id" : lambda d: hashcode ("unifespa",  "docente", d["vinculo_servidor"]),
                    "formacao": "escolaridade",
                    "sameas" : lambda d: "https://sigaa.unifesspa.edu.br/sigaa/public/docente/portal.jsf?siape=" + d["vinculo_servidor"]
            },

            "data" : lambda  :  dados_ckan("http://ckan.unifesspa.edu.br/api/action/datastore_search?resource_id=eff99b8c-09d3-453b-b7dd-1de846ab18a7"),
            
            "rdf_path" : "rdf/docentes_unifespa.rdf"
        },


        { ## ufpi
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "siape": "siape",
                    "id" : lambda d: hashcode ("ufpi",  "docente", d["siape"]),
                    "sameas" : lambda d: "https://sigaa.ufpi.br/sigaa/public/docente/portal.jsf?siape=" + d["siape"]
            },

            "data" : lambda :  dados_ckan("http://dados.ufrn.br/api/action/datastore_search?resource_id=ff0a457e-76fa-4aca-ad99-48aebd7db070"),
            
            "rdf_path" : "rdf/docentes_ufpi.rdf"
        },

        { ## ufsj
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "siape": "siape",
                    "id" : lambda d: hashcode ("ufsj",  "docente", d["siape"]),
                    "sameas" : lambda d: "https://sig.ufsj.edu.br/sigaa/public/docente/portal.jsf?siape=" + d["siape"]
            },

            "data" : lambda : dados_ckan("http://dados.ufsj.edu.br/api/action/datastore_search?resource_id=8e2e35ed-e255-4894-b070-ad8857366faf"),
            
            "rdf_path" : "rdf/docentes_ufsj.rdf"
        },


        { ## ufma (DEPOIS MUDAR A API PARA RETORNAR NO MODELO)
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "siape": "siape",
                    "id" : lambda d: hashcode ("ufma",  "docente", str(d["siape"])),
                    "telefone" : "telefone",
                    "imagem" : "urlimg",
                    "email" : "email",
                    "lattes" : "lattes",
                    "descricao" : "descricao",

                    "sameas" : lambda d: "https://sigaa.ufma.br/sigaa/public/docente/portal.jsf?siape=" + str(d["siape"])
            }, 

            "data" :  lambda : dados_ufma("https://dados-ufma.herokuapp.com/api/v01/docente/"),
            
            "rdf_path" : "rdf/docentes_ufma.rdf"
        },

     { ## ifma  
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "siape": "matricula",
                    "id" : lambda d: hashcode ("ifma",  "docente", str(d["matricula"])),
                    "lattes" : lambda d: "http://lattes.cnpq.br/"+(d["curriculo_lattes"] or "") ,

            }, 

            "data" :  lambda : list( filter (  lambda d:  d["categoria"] == "Docente" ,
                        requests.get("https://dados.ifma.edu.br/dataset/3facdc4a-90a4-4372-86c5-4f189d5addf1/resource/bf91b51a-464f-47a0-ae2d-ec86fade5bbe/download/servidores_20191119.json").json()
                    )),
            
            "rdf_path" : "rdf/docentes_ifma.rdf"
        },

        { ## ifrn
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "siape": "matricula",
                    "id" : lambda d: hashcode ("ifrn",  "docente", str(d["matricula"])),
                    #"lattes" : lambda d: "http://lattes.cnpq.br/"+(d["curriculo_lattes"] or "") ,

            }, 

            "data" :  lambda : list( filter (  lambda d:  d["categoria"] == "docente" ,
                        requests.get("https://dados.ifrn.edu.br/dataset/0c5c1c1a-7af8-4f24-ba37-a9eda0baddbb/resource/c3f64d5b-f2df-4ef2-8e27-fb4f10a7c3ea/download/dados_extraidos_recursos_servidores.json").json()
                    )),
            
            "rdf_path" : "rdf/docentes_ifrn.rdf"
        },

        { ## ifpb
            "toSave" : True,
            "mapper" : {
                    "nome" : "nome", 
                    "siape": "matricula",
                    "id" : lambda d: hashcode ("ifpb",  "docente", str(d["matricula"])),
                    #"lattes" : lambda d: "http://lattes.cnpq.br/"+(d["curriculo_lattes"] or "") ,

            }, 

            "data" :  lambda : list( filter (  lambda d: d["cargo_emprego"] and d["cargo_emprego"].find("PROFESSOR") > -1 ,
                        requests.get("https://dados.ifpb.edu.br/dataset/26d67876-0cb2-41a4-83ed-7bde06eb736c/resource/0d03ee6a-2af1-4dde-9b3d-90419c48fabe/download/servidores.json").json()
                    )),
            
            "rdf_path" : "rdf/docentes_ifpb.rdf"
        },

    ]
}


serialize_all_to_rdf(serialize_rdf_docentes)