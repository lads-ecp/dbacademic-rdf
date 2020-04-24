f = open ("./instituicoes.txt", "r")

s = """
<?xml version="1.0" encoding="utf-8" ?>
<rdf:RDF
	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
	xmlns:owl="http://www.w3.org/2002/07/owl#"
	xmlns:dct="http://purl.org/dc/terms/"
	xmlns:dbo="http://dbpedia.org/ontology/"
	xmlns:foaf="http://xmlns.com/foaf/0.1/"
	xmlns:prov="http://www.w3.org/ns/prov#"
	xmlns:dbp="http://dbpedia.org/property/"
	xmlns:ns8="http://purl.org/linguistics/gold/" >
"""
rdf = open ("instituicoes.rdf","w")
rdf.write(s)

rdfline = """
<rdf:Description rdf:about="%s">
    <rdf:type rdf:resource="http://dbpedia.org/ontology/EducationalInstitution" />
  </rdf:Description>
"""

lines = f.readlines()
for line in lines:
    rdf.write (rdfline%line.strip())




rdf.write("</rdf:RDF>")

f.close()
rdf.close()