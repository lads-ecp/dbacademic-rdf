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
            "toSave" : True,
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
            "toSave" : True,
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
            "toSave" : True,
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
            "toSave" : True,
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
            "toSave" : True,
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

    ]
}


serialize_all_to_rdf(serialize_rdf_docentes)