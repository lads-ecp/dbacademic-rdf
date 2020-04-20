
from rdflib import Namespace, Literal, URIRef
from simpot import RdfsClass, BNamespace
from rdflib.namespace import DC, FOAF


VCARD = Namespace('https://www.w3.org/2006/vcard/ns#')
DBO = Namespace('http://dbpedia.org/data3/.n3#')
DC = Namespace('http://purl.org/dc/terms/#')
VIVO = Namespace("http://vivoweb.org/ontology/core#")
BIBO = Namespace("http://purl.org/ontology/bibo/")
OWL = Namespace("http://www.w3.org/TR/owl-ref/")
OPENCIN = Namespace("http://purl.org/ontology/opencin/")
DBACAD = Namespace("http://purl.org/ontology/dbacademic/")
AIISO = Namespace("http://purl.org/vocab/aiiso/schema#")



class Curso ():

    nome = FOAF.name

    area = OPENCIN.knowledgeArea

    coordenador = AIISO.responsibilityOf

    unidade = AIISO.part_of

    university = AIISO.part_of

    code= AIISO.code

    @RdfsClass(OPENCIN.Undergratuate, "https://www.dbacademic.tech/resource/")
    @BNamespace('cin', OPENCIN)
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
    siape = OPENCIN.SIAPE
    formacao = OPENCIN.academicDegree
    
    sameas = OWL.sameas

    unidade = DBACAD.hasOrganization

    sexo = VCARD.hasGender

    telefone = VCARD.hasTelephone
    imagem = VCARD.hasPhoto
    email = VCARD.hasEmail
    lattes = OPENCIN.lattes
    descricao = DBO.abstract
    
    @RdfsClass(OPENCIN.FullProfessor, "https://www.dbacademic.tech/resource/")
    @BNamespace('foaf', FOAF)
    @BNamespace('cin', OPENCIN)
    @BNamespace('owl', OWL)
    @BNamespace('vcard', VCARD)
    @BNamespace('dbo', DBO)
    @BNamespace('dbacad', DBACAD)
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

    nome = OPENCIN.name
    sameas = OWL.sameas

     # unidade ? ou subunidade
    @RdfsClass(OPENCIN.Center, "https://www.dbacademic.tech/center/")   
    def __init__(self, dict):
        self.nome = Literal(dict["nome"])
        self.id = str(dict["id"])
        if "sameas" in dict:
            self.sameas = URIRef(dict["sameas"])

class Department ():

    nome = OPENCIN.name
    sameas = OWL.sameas

     # unidade ? ou subunidade
    @RdfsClass(OPENCIN.Center, "https://www.dbacademic.tech/department/")   
    def __init__(self, dict):
        self.nome = Literal(dict["nome"])
        self.id = str(dict["id"])
        if "sameas" in dict:
            self.sameas = URIRef(dict["sameas"])

class Discente ():

    nome = FOAF.name
    curso = OPENCIN.belongsA
    code= AIISO.code


    @RdfsClass(OPENCIN.Student, "https://www.dbacademic.tech/resource/")
    @BNamespace('foaf', FOAF)
    @BNamespace('cin', OPENCIN)
    @BNamespace('aiiso', AIISO)
    def __init__(self, dict ):
        self.nome = Literal(dict["nome"])
        self.id = dict["id"]
        self.code = dict["code"]
        if "curso" in dict:
            self.curso = URIRef(dict["curso"])

class GrupoPesquisa ():


    nome = OPENCIN.name
    area = OPENCIN.knowledgeArea
    university = OPENCIN.University
    coordenador = OPENCIN.hasCoordinator

    @RdfsClass(OPENCIN.researchGroup, "https://www.dbacademic.tech/researchgroup/")
    @BNamespace('dc', DC)
    def __init__(self, dict):
        self.id = dict["id"]
        self.nome = Literal (dict["nome"])
        self.area = Literal (dict["area"])
        self.coordenador = URIRef(dict["coordenador"])
  
class Monografia ():

    title = DC.title
    autor = DC.creator
    curso = BIBO.issuer
    orientador = DC.contributor

    @RdfsClass(BIBO.Report, "https://www.dbacademic.tech/monography/")
    @BNamespace('dc', DC)
    @BNamespace('bibo', BIBO)
    def __init__(self, dict ):
        self.title = Literal(dict["titulo"])
        self.id = dict["id"]
        #self.curso = Literal ("curso")
        #self.curso = URIRef("https://sigaa.ufma.br/sigaa/public/curso/portal.jsf?id=" + str(curso))
        #self.autor = Literal("autor")
        #self.orientador = Literal("orientador")
        #self.orientador = URIRef("https://sigaa.ufma.br/sigaa/public/docente/portal.jsf?siape=" + str(orientador))
