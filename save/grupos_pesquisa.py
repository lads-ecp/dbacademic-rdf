
from model import  Docente, Curso, Discente, Unidade, Monografia, GrupoPesquisa
from simpot import serialize_to_rdf_file, mapper_all, serialize_all_to_rdf

from utils import dados_sigaa, dados_ufma, dados_iffar, dados_csv, hashcode



serialize_rdf_grupopesquisa = {

    "classType" : GrupoPesquisa,

    "collection" : [


        { ## ufrn
            "toSave" : True,
            "mapper" : {
                    "nome" : "base_pesquisa", 
                    "id": lambda d : hashcode ("ufrn", str(d["codigo"])),
                    "area" : "area_conhecimento_cnpq",
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_University_of_Rio_Grande_do_Norte",
                    "coordenador": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufrn", str (d["id_coordenador"])),
            },

            "data" : lambda :  dados_sigaa("http://dados.ufrn.br/api/action/datastore_search?resource_id=09951a7c-46c4-4d1b-a537-2e50caa070c4"),
            "rdf_path" : "rdf/grupospesquisa_ufrn.rdf"
        },

        { ## iffar
            "toSave" : True,
            "mapper" : {
                    "nome" : "nome", 
                    "id": lambda d : hashcode ("iffar", str(d["id_grupo_pesquisa"])),
                    "area" : lambda d: d["links"]["id_area_conhecimento_cnpq"]["title"].split(':')[1].strip(),
                    "university" : lambda d: "http://dbpedia.org/resource/Federal_Institute_Farroupilha",
                    "coordenador": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "iffar", str (d["links"]["id_coordenador"]["title"].split(":")[0].strip()))
            },

            "data" : lambda :  dados_iffar("http://dados.iffarroupilha.edu.br/api/v1/grupos-pesquisa.json"),
            "rdf_path" : "rdf/grupospesquisa_iffar.rdf"
        },

        { ## ufersa
            "toSave" : True,
            "mapper" : {
                    "nome" : "titulo_projeto", 
                    "id": lambda d : hashcode ("ufersa", str(d["codigo"])),
                    "area" : lambda d: "area",
                    "coordenador": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode("ufersa", str(d["codigo"])),
                    "university" : lambda d: "http://dbpedia.org/page/Federal_Rural_University_of_the_Semi-arid_Region",
            },

            "data" : lambda :  dados_csv("http://api.ufersa.edu.br:8080/apiufersa/rest/pda/projetos-pesquisa"),
            "rdf_path" : "rdf/grupospesquisa_ufersa.rdf"
        },



    ]
}

serialize_all_to_rdf(serialize_rdf_grupopesquisa)
