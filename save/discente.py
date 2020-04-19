
from model import  Docente, Curso, Discente, Unidade, Monografia, GrupoPesquisa
from simpot import serialize_to_rdf_file, mapper_all, serialize_all_to_rdf

from utils import dados_sigaa, dados_ufma


serialize_rdf_discentes = {

    "classType" : Discente,

    "collection" : [

        { ## ufrn
            "toSave" : False,
            "mapper" : {
                    "nome" : "nome_discente", 
                    "id": lambda d: "ufrn_" + d["matricula"],
                    "curso": lambda d: "https://www.dbacademic.tech/course/ufrn_" + str(d["id_curso"])
            },

            "data" : lambda :  dados_sigaa("http://dados.ufrn.br/api/action/datastore_search?resource_id=a55aef81-e094-4267-8643-f283524e3dd7&limit=5"),
            
            "rdf_path" : "rdf/discentes_ufrn.rdf"
        },

        { ## ufpi
            "toSave" : True,
            "mapper" : {
                    "nome" : "nome_discente", 
                    "id": lambda d: "ufpi_" + d["matricula"],
                    "curso": lambda d: "https://www.dbacademic.tech/course/ufpi_" + str(d["id_curso"])
            },

            "data" : lambda :  dados_sigaa("https://dados.ufpi.br/api/action/datastore_search?resource_id=20df1fac-f3f1-4344-a514-655bd251db2b&limit=5"),
            
            "rdf_path" : "rdf/discentes_ufpi.rdf"
        },

    ]
}

serialize_all_to_rdf(serialize_rdf_discentes)

