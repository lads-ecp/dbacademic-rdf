
from model import  Docente, Curso, Discente, Unidade, Monografia, GrupoPesquisa
from simpot import serialize_to_rdf_file, mapper_all, serialize_all_to_rdf

from utils import dados_sigaa, dados_ufma



serialize_rdf_grupopesquisa = {

    "classType" : GrupoPesquisa,

    "collection" : [


        { ## ufrn
            "toSave" : True,
            "mapper" : {
                    "nome" : "base_pesquisa", 
                    "id": lambda d : "ufrn_"+ str(d["codigo"]),
                    "area" : "area_conhecimento_cnpq",
                    "coordenador": lambda d: "https://www.dbacademic.tech/professor/ufrn_" + d["id_coordenador"]
            },

            "data" : lambda :  dados_sigaa("http://dados.ufrn.br/api/action/datastore_search?resource_id=09951a7c-46c4-4d1b-a537-2e50caa070c4&limit=5"),
            "rdf_path" : "rdf/grupospesquisa_ufrn.rdf"
        }

    ]
}

serialize_all_to_rdf(serialize_rdf_grupopesquisa)
