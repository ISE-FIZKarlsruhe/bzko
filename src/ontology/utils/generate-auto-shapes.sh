
# create the reasoned version of the edit ontology
sh run.sh robot --catalog catalog-v001.xml merge --input bzk-edit.owl remove --term owl:real reason --reasoner hermit --axiom-generators "SubClass SubObjectProperty ClassAssertion InverseObjectProperties PropertyAssertion" --output ./tmp/tmp-reasoned.ttl

# generate the shacle shapes from the 
docker run --rm -v ./:/data ghcr.io/ashleycaselli/shacl:latest infer -datafile /data/tmp/tmp-reasoned.ttl -shapesfile /data/utils/owl2shacl/owl2sh-open.ttl > ../../data/shapes/auto-shapes-open.ttl
docker run --rm -v ./:/data ghcr.io/ashleycaselli/shacl:latest infer -datafile /data/tmp/tmp-reasoned.ttl -shapesfile /data/utils/owl2shacl/owl2sh-semi-closed.ttl > ../../data/shapes/auto-shapes-semi-closed.ttl
docker run --rm -v ./:/data ghcr.io/ashleycaselli/shacl:latest infer -datafile /data/tmp/tmp-reasoned.ttl -shapesfile /data/utils/owl2shacl/owl2sh-closed.ttl > ../../data/shapes/auto-shapes-closed.ttl


