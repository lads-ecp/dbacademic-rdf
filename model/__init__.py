
from rdflib import Namespace, Literal, URIRef
from simpot import RdfsClass, BNamespace
from rdflib.namespace import DC, FOAF


VCARD = Namespace('https://www.w3.org/2006/vcard/ns#')
DBO = Namespace('http://dbpedia.org/ontology/')
DC = Namespace('http://purl.org/dc/terms/#')
VIVO = Namespace("http://vivoweb.org/ontology/core#")
BIBO = Namespace("http://purl.org/ontology/bibo/")
OWL = Namespace("http://www.w3.org/TR/owl-ref/")
OPENCIN = Namespace("http://purl.org/ontology/opencin/")
DBACAD = Namespace("http://purl.org/ontology/dbacademic/")
AIISO = Namespace("http://purl.org/vocab/aiiso/schema#")


ORG = Namespace ("https://www.w3.org/TR/vocab-org/")


OPENUAI = Namespace("http://purl.org/ontology/openuai#")

class Curso ():

    nome = FOAF.name

    area = OPENUAI.hasKnowledgeArea

    coordenador = AIISO.responsibilityOf

    unidade = AIISO.responsibilityOf

    university = AIISO.responsibilityOf

    code= AIISO.code

    @RdfsClass(AIISO.Programme, "https://www.dbacademic.tech/resource/")
    @BNamespace('cin', OPENCIN)
    @BNamespace('uai', OPENUAI)
    @BNamespace('aiiso', AIISO)
    @BNamespace('foaf', FOAF)
    def __init__(self, dict):
        self.nome = Literal(dict["nome"])
        self.id = str(dict["id"])
        self.code = str (dict["id"])

        if "area" in dict:
            self.area = Literal(dict["area"])
        
        if "coordenador" in dict:
            self.coordenador = URIRef(dict["coordenador"])

        if "unidade" in dict:
            self.unidade = URIRef(dict["unidade"])
            
        self.university = URIRef(dict["university"])



class Docente ():

    nome = FOAF.name
    siape = OPENCIN.siape

    formacao = OPENCIN.academicDegree
    
    sameas = OWL.sameas

    unidade = ORG.memberOf

    sexo = VCARD.hasGender

    telefone = VCARD.hasTelephone
    imagem = VCARD.hasPhoto
    email = VCARD.hasEmail
    lattes = OPENCIN.lattes
    descricao = DBO.abstract
    
    @RdfsClass(DBO.Professor, "https://www.dbacademic.tech/resource/")
    @BNamespace('foaf', FOAF)
    @BNamespace('cin', OPENCIN)
    @BNamespace('owl', OWL)
    @BNamespace('vcard', VCARD)
    @BNamespace('dbo', DBO)
    @BNamespace('org', ORG)
    def __init__(self, dict):
        self.nome = Literal(dict["nome"])
        self.siape = Literal(dict["siape"])
        self.id = str(dict["id"])
        if "formacao" in dict:
            self.formacao = Literal(dict["formacao"])
        if "sameas" in dict:
            self.sameas = URIRef(dict["sameas"])
        if "sexo" in dict:
            self.sexo = Literal (dict["sexo"])

        if "unidade" in dict:
            self.unidade = URIRef(dict["unidade"])

        if "telefone" in dict:
            if dict["telefone"]:
                self.telefone = Literal('tel:+55.98'+dict["telefone"])

        if "imagem" in dict:
            if dict["imagem"]:
                self.imagem = URIRef(dict["imagem"])

        if "email" in dict:
            if dict["email"]:
                self.email = Literal('mailto:' + dict["email"]) # mudar para uriref

        if "lattes" in dict: # nao considerou valido
            if dict["lattes"]:
                self.lattes = Literal(dict["lattes"])
                #self.lattes = URIRef(dict["lattes"])

        if "descricao" in dict:
            if dict["descricao"]:
                self.descricao = Literal(dict["descricao"])





class Unidade ():

    nome = FOAF.name
    sameas = OWL.sameas
    diretor = AIISO.responsibleFor
    code= AIISO.code

     # unidade ? ou subunidade
    @RdfsClass(AIISO.Center, "https://www.dbacademic.tech/resource/")   
    @BNamespace('foaf', FOAF)
    @BNamespace('cin', OPENCIN)
    @BNamespace('owl', OWL)
    @BNamespace('aiiso', AIISO)
    def __init__(self, dict):
        self.nome = Literal(dict["nome"])
        self.code = dict["code"]
        self.id = str(dict["id"])
        if "sameas" in dict:
            self.sameas = URIRef(dict["sameas"])
        if "diretor" in dict:
            self.diretor = URIRef(dict["diretor"])

class Subunidade ():

    nome = FOAF.name
    sameas = OWL.sameas
    chefe = AIISO.responsibleFor
    unidade = AIISO.part_of
    code= AIISO.code

     # unidade ? ou subunidade
    @RdfsClass(AIISO.Department, "https://www.dbacademic.tech/resource/")   
    @BNamespace('foaf', FOAF)
    @BNamespace('cin', OPENCIN)
    @BNamespace('owl', OWL)
    @BNamespace('aiiso', AIISO)
    def __init__(self, dict):
        self.nome = Literal(dict["nome"])
        self.id = str(dict["id"])
        self.code = dict["code"]
        if "sameas" in dict:
            self.sameas = URIRef(dict["sameas"])
        if "unidade" in dict:
            self.unidade = URIRef(dict["unidade"])

class Discente ():

    nome = FOAF.name
    curso = DBACAD.isStudying
    code= DC.identifier


    @RdfsClass(OPENCIN.Student, "https://www.dbacademic.tech/resource/")
    @BNamespace('foaf', FOAF)
    @BNamespace('cin', OPENCIN)
    @BNamespace('aiiso', AIISO)
    @BNamespace('dc', DC)
    @BNamespace('dbacad', DBACAD)
    def __init__(self, dict ):
        self.nome = Literal(dict["nome"])
        self.id = dict["id"]
        self.code = dict["code"]
        if "curso" in dict:
            self.curso = URIRef(dict["curso"])

class GrupoPesquisa ():


    nome = FOAF.name
    area = OPENUAI.hasKnowledgeArea
    university = AIISO.responsibilityOf
    coordenador = AIISO.responsibilityOf

    @RdfsClass(AIISO.ResearchGroup, "https://www.dbacademic.tech/resource/")
    @BNamespace('foaf', FOAF)
    @BNamespace('cin', OPENCIN)
    @BNamespace('aiiso', AIISO)
    def __init__(self, dict):
        self.id = dict["id"]
        self.nome = Literal (dict["nome"])
        self.area = Literal (dict["area"])
        self.coordenador = URIRef(dict["coordenador"])
        self.university = URIRef(dict["university"])

  
class Monografia ():

    title = DC.title
    autor = DC.creator
    curso = BIBO.issuer
    orientador = DC.contributor

    @RdfsClass(BIBO.Report, "https://www.dbacademic.tech/resource/")
    @BNamespace('dc', DC)
    @BNamespace('bibo', BIBO)
    def __init__(self, dict ):
        self.title = Literal(dict["titulo"])
        self.id = dict["id"]
        if "curso" in dict:
            self.curso = URIRef(dict["curso"])
        if "autor" in dict:
            #self.autor = URIRef(dict["autor"])
            self.autor = Literal(dict["autor"])
        if "orientador" in dict:
            self.orientador = URIRef(dict["orientador"])        
