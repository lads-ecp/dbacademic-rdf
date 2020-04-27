from model import  Docente, Curso, Discente, Unidade, Monografia, GrupoPesquisa
from simpot import serialize_to_rdf_file, mapper_all, serialize_all_to_rdf

from utils import dados_sigaa, dados_ufma, hashcode

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
                    "id" : lambda d: hashcode ("ufrn", d["siape"]),
                    "siape": "siape",
                    "formacao" : "formacao",
                    "sameas" : lambda d: "https://sigaa.ufrn.br/sigaa/public/docente/portal.jsf?siape=" + d["siape"],
                    #"sexo": lambda d: sexo_dict[d["sexo"]],
                    "unidade": lambda d: "https://sigaa.ufrn.br/sigaa/public/departamento/portal.jsf?id=" + d["id_unidade_lotacao"]
            },

            "data" : lambda :  dados_sigaa("http://dados.ufrn.br/api/action/datastore_search?resource_id=ff0a457e-76fa-4aca-ad99-48aebd7db070"),
            
            "rdf_path" : "rdf/docentes_ufrn.rdf"
        },


        { ## unifespa
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome_servidor", 
                    "siape": "vinculo_servidor",
                    "id" : lambda d: hashcode ("unifespa", d["vinculo_servidor"]),
                    "formacao": "escolaridade",
                    "sameas" : lambda d: "https://sigaa.unifesspa.edu.br/sigaa/public/docente/portal.jsf?siape=" + d["vinculo_servidor"]
            },

            "data" : lambda  :  dados_sigaa("http://ckan.unifesspa.edu.br/api/action/datastore_search?resource_id=eff99b8c-09d3-453b-b7dd-1de846ab18a7"),
            
            "rdf_path" : "rdf/docentes_unifespa.rdf"
        },


        { ## ufpi
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "siape": "siape",
                    "id" : lambda d: hashcode ("ufpi", d["siape"]),
                    "sameas" : lambda d: "https://sigaa.ufpi.br/sigaa/public/docente/portal.jsf?siape=" + d["siape"]
            },

            "data" : lambda :  dados_sigaa("http://dados.ufrn.br/api/action/datastore_search?resource_id=ff0a457e-76fa-4aca-ad99-48aebd7db070"),
            
            "rdf_path" : "rdf/docentes_ufpi.rdf"
        },

        { ## ufsj
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "siape": "siape",
                    "id" : lambda d: hashcode ("ufsj", d["siape"]),
                    "sameas" : lambda d: "https://sig.ufsj.edu.br/sigaa/public/docente/portal.jsf?siape=" + d["siape"]
            },

            "data" : lambda : dados_sigaa("http://dados.ufsj.edu.br/api/action/datastore_search?resource_id=8e2e35ed-e255-4894-b070-ad8857366faf"),
            
            "rdf_path" : "rdf/docentes_ufsj.rdf"
        },


        { ## ufma (DEPOIS MUDAR A API PARA RETORNAR NO MODELO)
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "siape": "siape",
                    "id" : lambda d: hashcode ("ufma", str(d["siape"])),
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

        { ## ufpel
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "siape": "siape",
                    "formacao": "titulacao",
                    "id" : lambda d: hashcode ("ufpel", d["siape"])
            },

            "data" : lambda : dados_sigaa("http://dados.ufpel.edu.br/api/action/datastore_search_sql?sql=SELECT%20*%20from%20%22b63c24da-d96d-4ee2-bdaf-f7a8c37f0007%22%20WHERE%20categoria%20LIKE%20%27Docente%27"),
            
            "rdf_path" : "rdf/docentes_ufpel.rdf"
        },

        { ## ufms
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "siape": "_id",
                    "id" : lambda d: hashcode ("ufms", str(d["_id"]))
            },

            "data" : lambda : dados_sigaa("https://dadosabertos.ufms.br/api/action/datastore_search_sql?sql=SELECT%20*%20from%20%22a8ca7f30-0824-489b-8c70-faddcbd74f53%22%20WHERE%20cargo%20LIKE%20%27Professor%25%27"),
            
            "rdf_path" : "rdf/docentes_ufms.rdf"
        },

        { ## ufv
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "siape": "siape",
                    "id" : lambda d: hashcode ("ufv", d["siape"])
            },

            "data" : lambda : dados_sigaa("http://dados.ufv.br/api/3/action/datastore_search_sql?sql=SELECT%20*%20from%20%22a949a903-9536-4d20-87e5-cca5c217771a%22%20WHERE%20categoria%20LIKE%20%27DOCENTE%25%27"),
            
            "rdf_path" : "rdf/docentes_ufv.rdf"
        },
        
        { ## ufcspa
            "toSave" : True,
            "mapper" : {
                    "nome" : "NOME_FUNCIONARIO", 
                    "siape": "_id",
                    "id" : lambda d: hashcode ("ufcspa", d["_id"])
            },

            "data" : lambda : dados_sigaa("https://dados.ufcspa.edu.br/api/action/datastore_search?resource_id=4286a4d5-9de7-4f88-bb37-f0f064415118&q=PROFESSOR"),
            
            "rdf_path" : "rdf/docentes_ufcspa.rdf"
        },

    ]
}


serialize_all_to_rdf(serialize_rdf_docentes)