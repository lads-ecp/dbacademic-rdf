
from model import  Docente, Curso, Discente, Unidade, Monografia, GrupoPesquisa
from simpot import serialize_to_rdf_file, mapper_all, serialize_all_to_rdf

from utils import dados_sigaa, dados_ufma

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
                    "id": lambda d: "ufrn_"+ d["id_curso"],
                    "area" : "area_conhecimento",
                    "coordenador" : lambda d: "https://sigaa.ufrn.br/sigaa/public/docente/portal.jsf?siape=" + d["id_coordenador"],
                    "unidade" : lambda d: "https://sigaa.ufrn.br/sigaa/public/departamento/portal.jsf?lc=pt_BR&id=" + d["id_unidade_responsavel"],
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Rio_Grande_do_Norte",
                    "sameas" : lambda d: "https://sigaa.ufrn.br/sigaa/public/curso/portal.jsf?id=" + d["id_curso"],
            },

            "data" : lambda :  dados_sigaa("http://dados.ufrn.br/api/action/datastore_search?resource_id=a10bc434-9a2d-491a-ae8c-41cf643c35bc&limit=5"),
            
            "rdf_path" : "rdf/cursos_ufrn.rdf"
        },

        { ## ufpi
            "toSave" : False,
            "mapper" : {
                    "nome" : "Nome Curso", 
                    "id": lambda d: d["website"][ d["website"].index("?id=") +4: d["website"].index("&lc") ],
                    "area" : "Area",
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Piaui",
                    "sameas" : "website",
            },

            "data" : lambda :  dados_sigaa("https://dados.ufpi.br/api/action/datastore_search?resource_id=fa6f9042-ac3d-48fb-89db-410f5a455757&limit=5"),
            
            "rdf_path" : "rdf/cursos_ufpi.rdf"
        },


        { ## ufpb
            "toSave" : True,
            "mapper" : {
                    "nome" : "nome", 
                    "id": "id_curso",
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Para%C3%ADba",
                    "sameas" : lambda d: "https://sigaa.ufpbbr/sigaa/public/curso/portal.jsf?id=" + str(d["id_curso"]),
                    
            },

            "data" : lambda : cursos_ufpb(),
            
            "rdf_path" : "rdf/cursos_ufpb.rdf"
        },

    ]
}

serialize_all_to_rdf(serialize_rdf_cursos)

# saving