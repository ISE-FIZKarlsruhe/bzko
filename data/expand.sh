
# you can download robot here: https://github.com/ontodev/robot/releases/tag/v1.9.10
ROBOT="java -jar $HOME/robot.jar"


python data.py > output/data.ttl

#  we need to merge the extension ontology with the data
mkdir -p tmp
echo "merging bzko-extension with data"
$ROBOT merge --catalog ../src/ontology/catalog-v001.xml --input ../src/ontology/bzk-extension-edit.owl --input "output/data.ttl" --output tmp/merged-bzk.ttl

# we now do reasoning to materialize defined classes, etc.
echo "reasoning"
$ROBOT reason --input tmp/merged-bzk.ttl --reasoner hermit --axiom-generators "SubClass EquivalentClass DataPropertyCharacteristic EquivalentDataProperties SubDataProperty EquivalentObjectProperty InverseObjectProperties SubObjectProperty ObjectPropertyRange ObjectPropertyDomain ClassAssertion PropertyAssertion" remove --term owl:topObjectProperty --output tmp/merged-data-reasoned.ttl 


# we now apply the construc queries in the ontology to materialize shortcuts and mappings
echo "expanding"
$ROBOT expand --input tmp/merged-data-reasoned.ttl --output output/expanded.ttl

# we test against our geenrated shacle shapes
echo "testing shacl shapes autoshapes"
python3 -m pyshacl  -s shapes/auto-shapes-open.ttl output/expanded.ttl


# if the ontology is inconsistent: use the following cmd for explanation
#  java -jar robot.jar explain --mode inconsistency --input tmp/merged2.ttl --explanation errors.md