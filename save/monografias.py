
from model import  Docente, Curso, Discente, Unidade, Monografia, GrupoPesquisa
from simpot import serialize_to_rdf_file, mapper_all, serialize_all_to_rdf

from utils import dados_ckan, dados_ufma, hashcode, removeNonUTF8, dados_csv

from save.instituicoes_pt import *


serialize_rdf_monografia = {

    "classType" : Monografia,

    "collection" : [

        { ## ufrn
            "toSave" : False,
            "mapper" : {
                    "titulo" : lambda d:  removeNonUTF8 (d["titulo"]),
                    "university" : lambda d: UFRN, 
                    "id": lambda d : hashcode( "ufrn", "monografias", str(d["_id"])),
                    "autor": "nome_autor"
            },

            "data" : lambda :  dados_ckan("http://dados.ufrn.br/api/action/datastore_search?resource_id=7c01071b-81a4-4793-9a63-acfcd8a1aa83"),
            "rdf_path" : "rdf/monografias_ufrn.rdf"
        },

         { ## ufma
            "toSave" : False,
            "mapper" : {
                    "titulo" : lambda d:   (d["titulo"]), 
                    "university" : lambda d: UFMA,
                    "id": lambda d : hashcode( "ufma",  "monografias", str(d["codigo"]) ),
                    "curso": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufma", "curso", str (d["codigo_curso"])),
                    "orientador": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufma", "docente", str (d["siape_orientador"])),
                    #"autor": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufma", str (d["codigo_curso"])),
                    "autor": "discente"
                    
            },

            "data" : lambda :  dados_ufma("https://dados-ufma.herokuapp.com/api/v01/monografia/"),
            "rdf_path" : "rdf/monografias_ufma.rdf"
        }
,

         { ## ufob
            "toSave" : False,
            "mapper" : {
                    "titulo" : lambda d:   (d["TItulo do TCC"]), 
                    "university" : lambda d: UFOB,
                    "id": lambda d : hashcode( "ufob",  "monografias", str(d["TItulo do TCC"]) ),
                    #"curso": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufma", "curso", str (d["codigo_curso"])),
                    #"orientador": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufma", "docente", str (d["siape_orientador"])),
                    #"autor": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufma", str (d["codigo_curso"])),
                    "autor": "Autor"
                    
            },

            "data" : lambda :  dados_csv ("https://ufob.edu.br/acessoainformacao/index.php/dados-abertos?download=99:relacao-dos-trabalhos-de-conclusao-de-curso-4-2019", delimiter=";"),
            "rdf_path" : "rdf/monografias_ufob.rdf"
        }

#dados_csv ("https://ufob.edu.br/acessoainformacao/index.php/dados-abertos?download=99:relacao-dos-trabalhos-de-conclusao-de-curso-4-2019", delimiter=";")
    ]
}

serialize_all_to_rdf(serialize_rdf_monografia)

