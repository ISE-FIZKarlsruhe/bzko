PREFIX owl: <http://www.w3.org/2002/07/owl#>

DELETE {
  <https://schema.org/name> a owl:AnnotationProperty .
  <https://schema.org/birthDate> a owl:ObjectProperty .
  <https://schema.org/deathDate> a owl:ObjectProperty .
}
WHERE {
#  ?s ?p ?o .
}