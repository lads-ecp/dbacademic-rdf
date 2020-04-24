

pipenv install requests

pipenv install rdflib

# contando

PREFIX  cin:<http://purl.org/ontology/opencin/>
SELECT (COUNT(*) as ?Triples)
WHERE { ?s a cin:Student. }


PREFIX  dbo:<http://dbpedia.org/ontology/>
SELECT (COUNT(*) as ?Triples)
WHERE { ?s a dbo:Professor. }
  
  
PREFIX aiiso: <http://purl.org/vocab/aiiso/schema#>
SELECT (COUNT(*) as ?Triples)
WHERE { ?s a aiiso:Programme. }

PREFIX aiiso: <http://purl.org/vocab/aiiso/schema#>
SELECT (COUNT(*) as ?Triples)
WHERE { ?s a aiiso:Center. }










PREFIX  foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?name ?cursoname
WHERE {
  ?subject a <http://purl.org/ontology/opencin/Student>.
  ?subject <http://purl.org/ontology/opencin/belongsA> ?curso.
  ?subject foaf:name ?name.
  ?curso foaf:name ?cursoname.
}
LIMIT 25
