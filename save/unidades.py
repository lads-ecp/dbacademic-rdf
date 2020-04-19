
from model import  Docente, Curso, Discente, Unidade, Monografia, GrupoPesquisa
from simpot import serialize_to_rdf_file, mapper_all, serialize_all_to_rdf

from utils import dados_sigaa, dados_ufma


serialize_rdf_unidades = {

    "classType" : Unidade,

    "collection" : [

        { ## ufrn
            "toSave" : True,
            "mapper" : {
                    "nome" : "nome_unidade", 
                    "id": lambda d : "ufrn_"+d["id_unidade"],
                    "sameas" : lambda d: "https://sigaa.ufrn.br/sigaa/public/departamento/portal.jsf?id=" + str(d["id_unidade"]),                    
            },

            "data" : lambda :  dados_sigaa("http://dados.ufrn.br/api/action/datastore_search?resource_id=3f2e4e32-ef1a-4396-8037-cbc22a89d97f&limit=5"),
            "rdf_path" : "rdf/unidades_ufrn.rdf"
        }

    ]
}

serialize_all_to_rdf(serialize_rdf_unidades)

