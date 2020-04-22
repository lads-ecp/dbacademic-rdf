
from model import  Docente, Curso, Discente, Unidade, Monografia, GrupoPesquisa
from simpot import serialize_to_rdf_file, mapper_all, serialize_all_to_rdf

from utils import dados_sigaa, dados_ufma, hashcode



serialize_rdf_monografia = {

    "classType" : Monografia,

    "collection" : [

        { ## ufrn
            "toSave" : True,
            "mapper" : {
                    "titulo" : "titulo", 
                    "id": lambda d : hashcode( "ufrn", str(d["_id"])),
                    "autor": "nome_autor"
            },

            "data" : lambda :  dados_sigaa("http://dados.ufrn.br/api/action/datastore_search?resource_id=7c01071b-81a4-4793-9a63-acfcd8a1aa83"),
            "rdf_path" : "rdf/monografias_ufrn.rdf"
        },

         { ## ufma
            "toSave" : True,
            "mapper" : {
                    "titulo" : lambda d:  d["titulo"].encode('utf-8', 'xmlcharrefreplace'), 
                    "id": lambda d : hashcode( "ufma", str(d["codigo"]) ),
                    "curso": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufma", str (d["codigo_curso"])),
                    "orientador": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufma", str (d["siape_orientador"])),
                    #"autor": lambda d: "https://www.dbacademic.tech/resource/" +  hashcode ( "ufma", str (d["codigo_curso"])),
                    "autor": "discente"
                    
            },

            "data" : lambda :  dados_ufma("https://dados-ufma.herokuapp.com/api/v01/monografia/"),
            "rdf_path" : "rdf/monografias_ufma.rdf"
        }


    ]
}

serialize_all_to_rdf(serialize_rdf_monografia)

