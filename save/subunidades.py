
from model import  Docente, Curso, Discente, Unidade, Monografia, GrupoPesquisa, Subunidade
from simpot import serialize_to_rdf_file, mapper_all, serialize_all_to_rdf

from utils import dados_ckan, dados_ufma, hashcode, dados_iffar

from save.instituicoes_pt import *

serialize_rdf_subunidades = {

    "classType" : Subunidade,

    "collection" : [

        { ## ufrn
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome_unidade", 
                    "id": lambda d : hashcode ("ufrn", "departamento", d["id_unidade"]),
                    "code" : "id_unidade",
                    "university" : lambda d: UFRN,
                    "unidade": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufrn", "centro", d["id_unidade_responsavel"]),
                    "sameas" : lambda d: "https://sigaa.ufrn.br/sigaa/public/departamento/portal.jsf?id=" + str(d["id_unidade"]),                    
            },

            "data" : lambda : list (filter ( lambda d: d["tipo_unidade_organizacional"].find("DEPARTAMENTO") > -1, dados_ckan("http://dados.ufrn.br/api/action/datastore_search?resource_id=3f2e4e32-ef1a-4396-8037-cbc22a89d97f") )),
            "rdf_path" : "rdf/subunidades_ufrn.rdf"
        },

        { ## ufma
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "university" : lambda d: UFMA,
                    "id": lambda d : hashcode ("ufma", "departamento", d["codigo"]),
                    "code" : "codigo",
                    "sameas" : lambda d: "https://sigaa.ufma.br/sigaa/public/departamento/portal.jsf?id=" + str(d["codigo"]),                    
            },

            "data" : lambda : dados_ufma("https://dados-ufma.herokuapp.com/api/v01/subunidade/"),
            "rdf_path" : "rdf/subunidades_ufma.rdf"
        },

        { ## iffar
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "university" : lambda d: IFFAR,
                    "id": lambda d : hashcode ("iffar", "departamento", str(d["id_unidade"])),
                    "code" : "id_unidade",
                    "sameas" : lambda d: "https://sig.iffarroupilha.edu.br/sigaa/public/departamento/portal.jsf?id=" + str(d["id_unidade"])                    
            },

            "data" : lambda : dados_iffar("http://dados.iffarroupilha.edu.br/api/v1/unidades-organizacionais.json"),
            "rdf_path" : "rdf/subunidades_iffar.rdf"
        },

    ]
}

serialize_all_to_rdf(serialize_rdf_subunidades)

