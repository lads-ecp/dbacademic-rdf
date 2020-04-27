
from model import  Docente, Curso, Discente, Unidade, Monografia, GrupoPesquisa
from simpot import serialize_to_rdf_file, mapper_all, serialize_all_to_rdf

from utils import dados_ckan, dados_ufma, hashcode, dados_csv

from save.recursos import CURSO, DEPARTAMENTO

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
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "id": lambda d: hashcode ( "ufrn",CURSO, d["id_curso"]),
                    "code" : "id_curso",
                    "area" : "area_conhecimento",
                    "coordenador" : lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufrn", "docente", str (d["id_coordenador"])),
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Rio_Grande_do_Norte",
                    "unidade" : lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufrn","departamento", str (d["id_unidade_responsavel"])),
                    "sameas" : lambda d: "https://sigaa.ufrn.br/sigaa/public/curso/portal.jsf?id=" + d["id_curso"],
            },

            "data" : lambda :  dados_ckan("http://dados.ufrn.br/api/action/datastore_search?resource_id=a10bc434-9a2d-491a-ae8c-41cf643c35bc"),
            
            "rdf_path" : "rdf/cursos_ufrn.rdf"
        },

        { ## ufpi
            "toSave" : False,
            "mapper" : {
                    "nome" : "Nome Curso", 
                    "code" : lambda d: d["website"][ d["website"].index("?id=") +4: d["website"].index("&lc") ],
                    "id": lambda d: hashcode ( "ufpi", CURSO,  d["website"][ d["website"].index("?id=") +4: d["website"].index("&lc") ]),
                    "area" : "Area",
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Piaui",
                    "sameas" : "website",
            },

            "data" : lambda :  dados_ckan("https://dados.ufpi.br/api/action/datastore_search?resource_id=fa6f9042-ac3d-48fb-89db-410f5a455757"),
            
            "rdf_path" : "rdf/cursos_ufpi.rdf"
        },


        { ## ufpb
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "code" : "id_curso",
                    "id": lambda d: hashcode ( "ufpb",  CURSO, str (d["id_curso"])),
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Para%C3%ADba",
                    "sameas" : lambda d: "https://sigaa.ufpbbr/sigaa/public/curso/portal.jsf?id=" + str(d["id_curso"]),
                    
            },

            "data" : lambda : cursos_ufpb(),
            
            "rdf_path" : "rdf/cursos_ufpb.rdf"
        },

        { ## ufms
            "toSave" : False,
            "mapper" : {
                    "nome" : CURSO, 
                    "code" : "id",
                    "id": lambda d: hashcode ( "ufms",  CURSO, d["id"]),
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Mato_Grosso_do_Sul",
                    
            },

            "data" : lambda : dados_ckan("https://dadosabertos.ufms.br/api/action/datastore_search?resource_id=e239fd31-fe43-45e1-9d84-ba60a8d7fae7"),
            
            "rdf_path" : "rdf/cursos_ufms.rdf"
        },

        { ## ufma
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "code" : "codigo",
                    "id": lambda d: hashcode ( "ufma",  CURSO, d["codigo"]),
                    "coordenador" : lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufma", "docente", str (d["coordenador"])),
                    "sameas" : lambda d: "https://sigaa.ufma.br/sigaa/public/curso/portal.jsf?id=" + d["codigo"],
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Maranhao",
                    
            },

            "data" : lambda : dados_ufma("https://dados-ufma.herokuapp.com/api/v01/curso/"),
            
            "rdf_path" : "rdf/cursos_ufma.rdf"
        },

        { ## ufpel
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome_curso", 
                    "code" : "cod_curso",
                    "id": lambda d: hashcode ( "ufpel", CURSO, str(d["cod_curso"])),
                    "unidade": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufpel", DEPARTAMENTO, str (d["cod_unidade"])),
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Pelotas",        
            },

            "data" : lambda : dados_ckan("http://dados.ufpel.edu.br/api/action/datastore_search?resource_id=335bed66-d18b-40e1-9ac1-0db6d4f50a99"),
            
            "rdf_path" : "rdf/cursos_ufpel.rdf"
        },

        { ## ufca
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome_curso", 
                    "code" : "_id",
                    "id": lambda d: hashcode ( "ufca", CURSO, str(d["_id"])),
                    "university" : lambda d: "http://dbpedia.org/resource/Universidade_Federal_do_Cariri",        
            },

            "data" : lambda : dados_ckan("https://dados.ufca.edu.br/api/action/datastore_search?resource_id=5f31e620-a366-42c9-a54c-96da666c93b7"),
            
            "rdf_path" : "rdf/cursos_ufca.rdf"
        },
        
        { ## unifesspa
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome_curso", 
                    "code" : "_id",
                    "id": lambda d: hashcode ( "unifesspa", CURSO, str(d["_id"])),
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Southern_and_Southeastern_Par%C3%A1",        
            },

            "data" : lambda : dados_ckan("http://ckan.unifesspa.edu.br/api/action/datastore_search?resource_id=9ee93dc4-9398-43fc-91c4-1173b9378fed"),
            
            "rdf_path" : "rdf/cursos_unifesspa.rdf"
        },

        { ## ufv
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "code" : "_id",
                    "id": lambda d: hashcode ( "ufv", CURSO, str(d["_id"])),
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Vi%C3%A7osa",        
            },

            "data" : lambda : dados_ckan("http://dados.ufv.br/api/3/action/datastore_search?resource_id=e569f2e0-8ba0-4922-b715-9928980ae9f2"),
            
            "rdf_path" : "rdf/cursos_ufv.rdf"
        },

        { ## ifma
            "toSave" : False,
            "mapper" : {
                    "nome" : "descricao", 
                    "code": "codigo",
                    #"id" : lambda d: hashcode ("ifma",  "curso", str(d["codigo"])),
                    "id" : lambda d: hashcode ("ifma",  "curso", str(d["descricao"]).upper()),
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_Institute_of_Maranhao",        

            }, 

            "data" :  lambda : list( filter (  lambda d: d["modalidade"] and (d["modalidade"] == "Bacharelado"  or d["modalidade"] == "Tecnologia" ),
                        requests.get("https://dados.ifma.edu.br/dataset/510eb6ec-ae1a-4a4c-ada2-93d931d5db19/resource/a9d94e8b-9836-4651-b05d-ede34d97d47b/download/cursos_20190807.json").json()
                    )),
            
            "rdf_path" : "rdf/cursos_ifma.rdf"
        },

        { ## ifrn
            "toSave" : False,
            "mapper" : {
                    "nome" : "descricao", 
                    "code": "codigo",
                    "id" : lambda d: hashcode ("ifrn",  "curso", str(d["codigo"])),
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_Institute_of_Rio_Grande_do_Norte",        

            }, 

            "data" :  lambda : list( filter (  lambda d: d["modalidade"] and (d["modalidade"] == "Bacharelado"  or d["modalidade"] == "Tecnologia" ),
                        requests.get("https://dados.ifrn.edu.br/dataset/7b48f9d0-205d-46b1-8225-a3cc7d3973ff/resource/fe0e9d2c-1c02-4625-b692-13edcc3380ae/download/dados_extraidos_recursos_cursos-ofertados.json").json()
                    )),
            
            "rdf_path" : "rdf/cursos_ifrn.rdf"
        },

        { ## ifpb
            "toSave" : False,
            "mapper" : {
                    "nome" : "descricao", 
                    "code": "codigo",
                    "id" : lambda d: hashcode ("ifpb",  "curso", str(d["codigo"])),
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_Institute_of_Paraiba",        

            }, 

            "data" :  lambda : list( filter (  lambda d: d["modalidade"] and (d["modalidade"] == "Bacharelado"  or d["modalidade"] == "Tecnologia" ),
                        requests.get("https://dados.ifpb.edu.br/dataset/f2902132-dfc9-4fba-98ab-40346075224e/resource/47c6e782-6ef9-4942-8361-38d8aac22922/download/cursos.json").json()
                    )),
            
            "rdf_path" : "rdf/cursos_ifpb.rdf"
        },


        { ## ufcspa
            "toSave" : False,
            "mapper" : {
                    "nome" : "NOME_CURSO_DIPLOMA", 
                    "code" : "_id",
                    "id": lambda d: hashcode ( "ufcspa", "curso", str(d["_id"])),
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Health_Sciences_of_Porto_Alegre",        
            },

            "data" : lambda : dados_ckan("https://dados.ufcspa.edu.br/api/action/datastore_search?resource_id=6096d836-9160-43ae-bbbd-8712d4b202ca"),
            
            "rdf_path" : "rdf/cursos_ufcspa.rdf"
        },

        { ## ufsj
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome_curso", 
                    "code" : "codCurso",
                    "id": lambda d: hashcode ( "ufsj", "curso", str(d["codCurso"])),
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_S%C3%A3o_Jo%C3%A3o_del-Rei",        
            },

            "data" : lambda : dados_ckan("http://dados.ufsj.edu.br/api/action/datastore_search?resource_id=15625dc7-acc2-45e8-9189-46e4362c013f"),
            
            "rdf_path" : "rdf/cursos_ufsj.rdf"
        },

        { ## uffs
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome_curso", 
                    "code" : "cod_uffs",
                    "id": lambda d: hashcode ( "uffs", "curso", str(d["cod_uffs"])),
                    "coordenador" : lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "uffs", "docente", str (d["coord_curso"])),
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Fronteira_Sul",        
            },

            "data" : lambda : dados_ckan("https://dados.uffs.edu.br/api/3/action/datastore_search?resource_id=c35a0c22-fe50-4d7c-8339-7f253fe7e977"),
            
            "rdf_path" : "rdf/cursos_uffs.rdf"
        },

        { ## unirio
            "toSave" : False,
            "mapper" : {
                    "nome" : "NOME_UNIDADE", 
                    "code" : "COD_CURSO",
                    "id": lambda d: hashcode ( "unirio", "curso", str(d["COD_CURSO"])),
                    "area": "DESCR_AREA_CONHEC",
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_the_State_of_Rio_de_Janeiro",        
            },

            "data" : lambda : dados_csv("http://dados.unirio.br/dataset/bfc6f424-6137-4feb-9c4e-5512f8821415/resource/83d0d21f-63e1-4295-959a-1683e6a21937/download/cursosunirio2.csv"),
            
            "rdf_path" : "rdf/cursos_unirio.rdf"
        },

        { ## ifms
            "toSave" : False,
            "mapper" : {
                    "nome" : "curso", 
                    "code" : "_id",
                    "id": lambda d: hashcode ( "ifms", "curso", str(d["_id"])),
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_Institute_of_Mato_Grosso_do_Sul",        
            },

            "data" : lambda : list ( filter ( lambda d: d["nivel_ensino_curso"] == "Educação Superior",
                    dados_ckan("http://dados.ifms.edu.br/api/action/datastore_search?resource_id=b1913941-fcd6-4216-882f-fc2a81121bcc"),
            )),
            
            "rdf_path" : "rdf/cursos_ifms.rdf"
        },


        { ## ifs
            "toSave" : False,  # nao deu certo
            "mapper" : {
                    "nome" : "Nome", 
                    #"code": "codigo",
                    #"id" : lambda d: hashcode ("ifma",  "curso", str(d["codigo"])),
                    "id" : lambda d: hashcode ("ifs",  "curso", str(d["Nome"]).upper()),
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_Institute_of_Espirito_Santo",        

            }, 

            "data" :  lambda : list( filter (  lambda d: d["Grau"] and (d["Grau"] == "Bacharelado"  or d["Grau"] == "Tecnológico" ),
                        dados_csv("http://dados.ifs.edu.br/dataset/cc7b829b-54fc-4c24-91cd-915fa81f98c1/resource/07271cc7-c229-496d-b6cc-da19119c425e/download/20-cursos.csv")
                    )),
            
            "rdf_path" : "rdf/cursos_ifs.rdf"
        },


    ]
}

serialize_all_to_rdf(serialize_rdf_cursos)

