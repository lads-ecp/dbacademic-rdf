
from model import  Docente, Curso, Discente, Unidade, Monografia, GrupoPesquisa
from simpot import serialize_to_rdf_file, mapper_all, serialize_all_to_rdf

from utils import dados_sigaa, dados_ufma, dados_csv, hashcode

import requests

def cursos_ufpb ():
    r = requests.get('http://ckan.ufpb.br/dataset/c46a74c4-9a91-4380-a3a2-06030ccc8484/resource/c1e234ab-7089-4336-9a84-a38f49a8fffd/download/ensino_cursos.json')
    data = r.json()["select * from dadosabertos.ensino_cursos"]
    data = filter(lambda d:  d["nivel_ensino"] == "GRADUAÇÃO", data)
    return data   

serialize_rdf_cursos = {

    "classType" : Curso,

    "collection" : [

        { ## ufrn
            "toSave" : True,
            "mapper" : {
                    "nome" : "nome", 
                    "id": lambda d: hashcode ( "ufrn", d["id_curso"]),
                    "code" : "id_curso",
                    "area" : "area_conhecimento",
                    "coordenador" : lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufrn", str (d["id_coordenador"])),
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Rio_Grande_do_Norte",
                    "unidade" : lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufrn", str (d["id_unidade_responsavel"])),
                    "sameas" : lambda d: "https://sigaa.ufrn.br/sigaa/public/curso/portal.jsf?id=" + d["id_curso"],
            },

            "data" : lambda :  dados_sigaa("http://dados.ufrn.br/api/action/datastore_search?resource_id=a10bc434-9a2d-491a-ae8c-41cf643c35bc"),
            
            "rdf_path" : "rdf/cursos_ufrn.rdf"
        },

        { ## ufpi
            "toSave" : True,
            "mapper" : {
                    "nome" : "Nome Curso", 
                    "code" : lambda d: d["website"][ d["website"].index("?id=") +4: d["website"].index("&lc") ],
                    "id": lambda d: hashcode ( "ufpi", d["website"][ d["website"].index("?id=") +4: d["website"].index("&lc") ]),
                    "area" : "Area",
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Piaui",
                    "sameas" : "website",
            },

            "data" : lambda :  dados_sigaa("https://dados.ufpi.br/api/action/datastore_search?resource_id=fa6f9042-ac3d-48fb-89db-410f5a455757"),
            
            "rdf_path" : "rdf/cursos_ufpi.rdf"
        },


        { ## ufpb
            "toSave" : True,
            "mapper" : {
                    "nome" : "nome", 
                    "code" : "id_curso",
                    "id": lambda d: hashcode ( "ufpb", str (d["id_curso"])),
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Para%C3%ADba",
                    "sameas" : lambda d: "https://sigaa.ufpbbr/sigaa/public/curso/portal.jsf?id=" + str(d["id_curso"]),
                    
            },

            "data" : lambda : cursos_ufpb(),
            
            "rdf_path" : "rdf/cursos_ufpb.rdf"
        },

        { ## ufms
            "toSave" : True,
            "mapper" : {
                    "nome" : "curso", 
                    "code" : "id",
                    "id": lambda d: hashcode ( "ufms", d["id"]),
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Mato_Grosso_do_Sul",
                    
            },

            "data" : lambda : dados_sigaa("https://dadosabertos.ufms.br/api/action/datastore_search?resource_id=e239fd31-fe43-45e1-9d84-ba60a8d7fae7"),
            
            "rdf_path" : "rdf/cursos_ufms.rdf"
        },

        { ## ufma
            "toSave" : True,
            "mapper" : {
                    "nome" : "nome", 
                    "code" : "codigo",
                    "id": lambda d: hashcode ( "ufma", d["codigo"]),
                    "coordenador" : lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufma", str (d["coordenador"])),
                    "sameas" : lambda d: "https://sigaa.ufma.br/sigaa/public/curso/portal.jsf?id=" + d["codigo"],
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Maranhao",
                    
            },

            "data" : lambda : dados_ufma("https://dados-ufma.herokuapp.com/api/v01/curso/"),
            
            "rdf_path" : "rdf/cursos_ufma.rdf"
        },

        { ## ufpel
            "toSave" : True,
            "mapper" : {
                    "nome" : "nome_curso", 
                    "code" : "cod_curso",
                    "id": lambda d: hashcode ( "ufpel", str(d["cod_curso"])),
                    "unidade": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufpel", str (d["cod_unidade"])),
                    "university" : lambda d: "http://dbpedia.org/page/Federal_University_of_Pelotas",        
            },

            "data" : lambda : dados_sigaa("http://dados.ufpel.edu.br/api/action/datastore_search?resource_id=335bed66-d18b-40e1-9ac1-0db6d4f50a99"),
            
            "rdf_path" : "rdf/cursos_ufpel.rdf"
        },

        { ## ufca
            "toSave" : True,
            "mapper" : {
                    "nome" : "nome_curso", 
                    "code" : "_id",
                    "id": lambda d: hashcode ( "ufca", str(d["_id"])),
                    "university" : lambda d: "http://dbpedia.org/page/Universidade_Federal_do_Cariri",        
            },

            "data" : lambda : dados_sigaa("https://dados.ufca.edu.br/api/action/datastore_search?resource_id=5f31e620-a366-42c9-a54c-96da666c93b7"),
            
            "rdf_path" : "rdf/cursos_ufca.rdf"
        },
        
        { ## unifesspa
            "toSave" : True,
            "mapper" : {
                    "nome" : "nome_curso", 
                    "code" : "_id",
                    "id": lambda d: hashcode ( "unifesspa", str(d["_id"])),
                    "university" : lambda d: "http://dbpedia.org/page/Federal_University_of_Southern_and_Southeastern_Par%C3%A1",        
            },

            "data" : lambda : dados_sigaa("http://ckan.unifesspa.edu.br/api/action/datastore_search?resource_id=9ee93dc4-9398-43fc-91c4-1173b9378fed"),
            
            "rdf_path" : "rdf/cursos_unifesspa.rdf"
        },

        { ## ufv
            "toSave" : True,
            "mapper" : {
                    "nome" : "nome", 
                    "code" : "_id",
                    "id": lambda d: hashcode ( "ufv", str(d["_id"])),
                    "university" : lambda d: "http://dbpedia.org/page/Federal_University_of_Vi%C3%A7osa",        
            },

            "data" : lambda : dados_sigaa("http://dados.ufv.br/api/3/action/datastore_search?resource_id=e569f2e0-8ba0-4922-b715-9928980ae9f2"),
            
            "rdf_path" : "rdf/cursos_ufv.rdf"
        },

        { ## ufcspa
            "toSave" : True,
            "mapper" : {
                    "nome" : "NOME_CURSO_DIPLOMA", 
                    "code" : "_id",
                    "id": lambda d: hashcode ( "ufcspa", str(d["_id"])),
                    "university" : lambda d: "http://dbpedia.org/page/Federal_University_of_Health_Sciences_of_Porto_Alegre",        
            },

            "data" : lambda : dados_sigaa("https://dados.ufcspa.edu.br/api/action/datastore_search?resource_id=6096d836-9160-43ae-bbbd-8712d4b202ca"),
            
            "rdf_path" : "rdf/cursos_ufcspa.rdf"
        }
    ]
}

serialize_all_to_rdf(serialize_rdf_cursos)

# saving