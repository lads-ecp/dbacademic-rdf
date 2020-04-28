
from model import  Docente, Curso, Discente, Unidade, Monografia, GrupoPesquisa
from simpot import serialize_to_rdf_file, mapper_all, serialize_all_to_rdf

from utils import dados_sigaa, dados_ufma, dados_iffar, hashcode


serialize_rdf_discentes = {

    "classType" : Discente,

    "collection" : [

        { ## ufrn
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome_discente", 
                    "id": lambda d: hashcode ("ufrn", d["matricula"]),
                    "code" : "matricula",
                    "curso": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufrn", str (d["id_curso"]))
            },

            "data" : lambda :  dados_sigaa("http://dados.ufrn.br/api/action/datastore_search?resource_id=a55aef81-e094-4267-8643-f283524e3dd7"),
            
            "rdf_path" : "rdf/discentes_ufrn.rdf"
        },

        { ## ufpi
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome_discente", 
                    "id": lambda d: hashcode ("ufpi", d["matricula"]),
                    "code" : "matricula",
                    "curso": lambda d: "https://www.dbacademic.tech/resource/" + hashcode ( "ufpi", str (d["id_curso"]))
            },

            "data" : lambda :  dados_sigaa("https://dados.ufpi.br/api/action/datastore_search?resource_id=20df1fac-f3f1-4344-a514-655bd251db2b"),
            
            "rdf_path" : "rdf/discentes_ufpi.rdf"
        },

        { ## ufma
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome", 
                    "id": lambda d: hashcode ("ufma", d["matricula"]),
                    "code" : "matricula",
                    "curso": lambda d: "https://www.dbacademic.tech/resource/" + hashcode ( "ufma", str (d["codigo_curso"]))
            },

            "data" : lambda :  dados_ufma("https://dados-ufma.herokuapp.com/api/v01/discente/"),
            
            "rdf_path" : "rdf/discentes_ufma.rdf"
        },

        { ## iffar
            "toSave" : True,
            "mapper" : {
                    "nome" : "nome", 
                    "id": lambda d: hashcode ("iffar", d["id_discente"]),
                    "code" : "id_discente",
                    "curso": lambda d: "https://www.dbacademic.tech/resource/" + hashcode ( "iffar", str (d["id_curso"]))
            },

            "data" : lambda :  dados_iffar("http://dados.iffarroupilha.edu.br/api/v1/alunos.json?nivel=T"),
            
            "rdf_path" : "rdf/discentes_iffar.rdf"
        },

    ]
}

serialize_all_to_rdf(serialize_rdf_discentes)

