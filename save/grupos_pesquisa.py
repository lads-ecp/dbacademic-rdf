
from model import  Docente, Curso, Discente, Unidade, Monografia, GrupoPesquisa
from simpot import serialize_to_rdf_file, mapper_all, serialize_all_to_rdf

from utils import dados_ckan, dados_ufma, hashcode



serialize_rdf_grupopesquisa = {

    "classType" : GrupoPesquisa,

    "collection" : [


        { ## ufrn
            "toSave" : True,
            "mapper" : {
                    "nome" : "base_pesquisa", 
                    "id": lambda d : hashcode ("ufrn", "grupopesquisa", str(d["codigo"])),
                    "area" : "area_conhecimento_cnpq",
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Rio_Grande_do_Norte",
                    "coordenador": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufrn", "docente", str (d["id_coordenador"])),
            },

            "data" : lambda :  dados_ckan("http://dados.ufrn.br/api/action/datastore_search?resource_id=09951a7c-46c4-4d1b-a537-2e50caa070c4"),
            "rdf_path" : "rdf/grupospesquisa_ufrn.rdf"
        }

    ]
}

serialize_all_to_rdf(serialize_rdf_grupopesquisa)
