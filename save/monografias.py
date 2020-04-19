
from model import  Docente, Curso, Discente, Unidade, Monografia, GrupoPesquisa
from simpot import serialize_to_rdf_file, mapper_all, serialize_all_to_rdf

from utils import dados_sigaa, dados_ufma



serialize_rdf_monografia = {

    "classType" : Monografia,

    "collection" : [

        { ## ufrn
            "toSave" : True,
            "mapper" : {
                    "titulo" : "titulo", 
                    "id": lambda d : "ufrn_"+ str(d["_id"]),
            },

            "data" : lambda :  dados_sigaa("http://dados.ufrn.br/api/action/datastore_search?resource_id=7c01071b-81a4-4793-9a63-acfcd8a1aa83&limit=5"),
            "rdf_path" : "rdf/monografias_ufrn.rdf"
        }

    ]
}

serialize_all_to_rdf(serialize_rdf_monografia)

