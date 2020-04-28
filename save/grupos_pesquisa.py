
from model import  Docente, Curso, Discente, Unidade, Monografia, GrupoPesquisa
from simpot import serialize_to_rdf_file, mapper_all, serialize_all_to_rdf

from utils import *

from save.recursos import *

serialize_rdf_grupopesquisa = {

    "classType" : GrupoPesquisa,

    "collection" : [


        { ## ufrn
            "toSave" : False,
            "mapper" : {
                    "nome" : "base_pesquisa", 
                    "id": lambda d : hashcode ("ufrn", "grupopesquisa", str(d["codigo"])),
                    "area" : "area_conhecimento_cnpq",
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Rio_Grande_do_Norte",
                    "coordenador": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufrn", "docente", str (d["id_coordenador"])),
            },

            "data" : lambda :  dados_ckan("http://dados.ufrn.br/api/action/datastore_search?resource_id=09951a7c-46c4-4d1b-a537-2e50caa070c4"),
            "rdf_path" : "rdf/grupospesquisa_ufrn.rdf"
        },

        { ## ufv
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome_grupo", 
                    "id": lambda d : hashcode ("ufv", "grupopesquisa", str(d["_id"])),
                    "area" : "area_predominante",
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Vicosa",
                   # "coordenador": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufrn", "docente", str (d["id_coordenador"])),
            },

            "data" : lambda :  dados_ckan("http://dados.ufv.br/api/3/action/datastore_search?resource_id=b8d9fd2a-a72b-472c-be4e-eed0f0bab85a"),
            "rdf_path" : "rdf/grupospesquisa_ufv.rdf"
        },


        { ## ufca
            "toSave" : False,
            "mapper" : {
                    "nome" : "Nome do Grupo", 
                    "id": lambda d : hashcode ("ufca", "grupopesquisa", str(d["_id"])),
                    "area" : "Área Predominante",
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Vicosa",
                   # "coordenador": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufrn", "docente", str (d["id_coordenador"])),
            },

            "data" : lambda :  dados_ckan("https://dados.ufca.edu.br/api/action/datastore_search?resource_id=56774760-1ff8-4f02-8279-df516e778338"),
            "rdf_path" : "rdf/grupospesquisa_ufca.rdf"
        },

        { ## ifc
            "toSave" : False,
            "mapper" : {
                    "nome" : "Nome do grupo", 
                    "id": lambda d : hashcode ("ifc", "grupopesquisa", str(d["Nome do grupo"])),
                    "area" : "Área predominante do grupo",
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_Instituto_Catarinense",
                   # "coordenador": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufrn", "docente", str (d["id_coordenador"])),
            },

            "data" : lambda :  dados_csv ("http://dadosabertos.ifc.edu.br/dataset/21491f20-55b4-494b-9e4c-fc480a17ebbb/resource/b76d5d70-b67f-4acf-b009-cb9e801fef68/download/dados-grupos-de-pesquisa.csv") ,
            "rdf_path" : "rdf/grupospesquisa_ifc.rdf"
        },

        { ## ifpi
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome_do_grupo", 
                    "id": lambda d : hashcode ("ifpi", "grupopesquisa", str(d["id_grupo"])),
                    "area" : "area_predominante",
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Piaui",
                   # "coordenador": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufrn", "docente", str (d["id_coordenador"])),
            },

            "data" : lambda :  dados_ckan ("https://dados.ufpi.br/api/action/datastore_search?resource_id=39fe54a4-ac85-4562-b5bc-06aa92e48ab4") ,
            "rdf_path" : "rdf/grupospesquisa_ifpi.rdf"
        },

    { ## ufop
            "toSave" : False,
            "mapper" : {
                    "nome" : "grupo", 
                    "id": lambda d : hashcode ("ufop", "grupopesquisa", str(d["id"])),
                    "area" : "area_predominante",
                    "university" : lambda d: UFOP,
                   # "coordenador": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufrn", "docente", str (d["id_coordenador"])),
            },

            "data" : lambda :  dados_csv ("http://dados.ufop.br/dataset/5bf7be63-4ca3-4a7d-8450-12ed5bc672c3/resource/72334807-6452-4ca3-b573-49c3afbc565a/download/grupos_pesquisa_ufop_v110032020.csv", delimiter=";") ,
            "rdf_path" : "rdf/grupospesquisa_ufop.rdf"
        },

        { ## unifesspa
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome_do_grupo", 
                    "id": lambda d : hashcode ("unifesspa", "grupopesquisa", str(d["_id"])),
                    "area" : "nome_area",
                    "university" : lambda d: UNIFESSPA,
                   # "coordenador": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufrn", "docente", str (d["id_coordenador"])),
            },

            "data" : lambda :  dados_ckan ("http://ckan.unifesspa.edu.br/api/action/datastore_search?resource_id=d1eb1b6a-c4ff-4c4a-8d1d-91929ab14ed0") ,
            "rdf_path" : "rdf/grupospesquisa_unifesspa.rdf"
        },

           { ## iffar
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "id": lambda d : hashcode ("iffar", "grupopesquisa", str(d["id_grupo_pesquisa"])),
                    "area" : lambda d: d["links"]["id_area_conhecimento_cnpq"]["title"].split(':')[1].strip(),
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_Institute_Farroupilha",
                    "coordenador": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "iffar", "docente", str(d["id_coordenador"]))
            },

            "data" : lambda :  dados_iffar("http://dados.iffarroupilha.edu.br/api/v1/grupos-pesquisa.json"),
            "rdf_path" : "rdf/grupospesquisa_iffar.rdf"
        },

    ]
}

serialize_all_to_rdf(serialize_rdf_grupopesquisa)
