## Customize Makefile settings for bzk
## 
## If you need to customize your Makefile, make
## changes here rather than in the main Makefile


$(IMPORTDIR)/nfdicore_import.owl: $(MIRRORDIR)/nfdicore.owl $(IMPORTDIR)/nfdicore_terms.txt | all_robot_plugins
	$(ROBOT) annotate --input $< --remove-annotations \
	     remove --term IAO:0000102 --select "self descendants" \
		 extract --term-file $(IMPORTDIR)/nfdicore_terms.txt  \
		         --force true --copy-ontology-annotations true \
		         --individuals exclude \
		         --method BOT \
		 $(ANNOTATE_CONVERT_FILE)

$(IMPORTDIR)/schema_import.owl: $(MIRRORDIR)/schema.owl $(IMPORTDIR)/schema_terms.txt | all_robot_plugins
	$(ROBOT) annotate --input $< --remove-annotations \
	     remove --term https://schema.org/name --select "annotation-properties" \
	     query --update $(IMPORTDIR)/schema_remove_puns.ru \
		 extract --term-file $(IMPORTDIR)/schema_terms.txt  \
		         --force true --copy-ontology-annotations true \
		         --individuals include \
		         --method STAR \
		 $(ANNOTATE_CONVERT_FILE)

$(IMPORTDIR)/rico_import.owl: $(MIRRORDIR)/rico.owl $(IMPORTDIR)/rico_terms.txt | all_robot_plugins
	$(ROBOT) annotate --input $< --remove-annotations \
		 extract --term-file $(IMPORTDIR)/rico_terms.txt  \
		         --force true --copy-ontology-annotations true \
		         --individuals include \
		         --method SUBSET \
		 remove $(foreach p, $(ANNOTATION_PROPERTIES), --term $(p)) \
		        --term-file $(IMPORTDIR)/rico_terms.txt  \
		        --select complement --select annotation-properties \
		 $(ANNOTATE_CONVERT_FILE)

$(IMPORTDIR)/pico_import.owl: $(MIRRORDIR)/pico.owl $(IMPORTDIR)/pico_terms.txt | all_robot_plugins
	$(ROBOT) annotate --input $< --remove-annotations \
		 extract --term-file $(IMPORTDIR)/pico_terms.txt  \
		         --force true --copy-ontology-annotations true \
		         --individuals include \
		         --method STAR \
		 remove $(foreach p, $(ANNOTATION_PROPERTIES), --term $(p)) \
		        --term-file $(IMPORTDIR)/pico_terms.txt  \
		        --select complement --select annotation-properties \
		 $(ANNOTATE_CONVERT_FILE)

$(IMPORTDIR)/prov_import.owl: $(MIRRORDIR)/prov.owl $(IMPORTDIR)/prov_terms.txt | all_robot_plugins
	$(ROBOT) annotate --input $< --remove-annotations \
		 extract --term-file $(IMPORTDIR)/prov_terms.txt  \
		         --force true --copy-ontology-annotations true \
		         --individuals include \
		         --method STAR \
		 remove $(foreach p, $(ANNOTATION_PROPERTIES), --term $(p)) \
		        --term-file $(IMPORTDIR)/prov_terms.txt  \
		        --select complement --select annotation-properties \
		 $(ANNOTATE_CONVERT_FILE)		 


$(IMPORTDIR)/ro_import.owl: $(MIRRORDIR)/ro.owl $(IMPORTDIR)/ro_terms.txt | all_robot_plugins
	$(ROBOT) annotate --input $< --remove-annotations \
		 extract --term-file $(IMPORTDIR)/ro_terms.txt  \
		         --force true --copy-ontology-annotations true \
		         --individuals include \
		         --method SUBSET \
		 remove $(foreach p, $(ANNOTATION_PROPERTIES), --term $(p)) \
		        --term-file $(IMPORTDIR)/ro_terms.txt  \
		        --select complement --select annotation-properties \
		 $(ANNOTATE_CONVERT_FILE)		 


## make extension release artefact:

#$(ONT)-extension.ttl: $(ONT).ttl
#	$(ROBOT) merge -i bzk-extension.owl -o $@ 

bzk-extension.owl: $(ONT).owl
	$(ROBOT) remove --input $< --select imports --trim false \
	merge --input bzk-extension-edit.owl   \
	reason --reasoner ELK --equivalent-classes-allowed asserted-only --exclude-tautologies structural \
		relax \
		reduce -r ELK \
		$(SHARED_ROBOT_COMMANDS) annotate --ontology-iri $(ONTBASE)extension annotate -V $(ONTBASE)extension/$(VERSION) --annotation owl:versionInfo $(VERSION) --output $@.tmp.owl && mv $@.tmp.owl $@ ; \

release-extension: bzk-extension.owl
		cp bzk-extension.owl $(RELEASEDIR)/bzk-extension.owl
		cp bzk-extension.owl $(RELEASEDIR)/bzk-extension-full.owl
		$(ROBOT) convert  --input $(RELEASEDIR)/bzk-extension.owl --output $(RELEASEDIR)/bzk-extension.ttl
		$(ROBOT) convert  --input $(RELEASEDIR)/bzk-extension-full.owl --output $(RELEASEDIR)/bzk-extension-full.ttl


CITATION="'BZKO Ontology. Version $(VERSION), https://bzk.fiz-karlsruhe.de/ontology/'"

ALL_ANNOTATIONS=--annotate-defined-by false \
	--annotation http://purl.org/dc/terms/created "$(TODAY)" \
	--annotation http://purl.org/dc/terms/bibliographicCitation "$(CITATION)"  \
	#--link-annotation owl:priorVersion https://bzk.fiz-karlsruhe.de/ontology/$(PRIOR_VERSION) \

ALL_ANNOTATIONS_AND_VERSION=--annotate-defined-by false \
	--ontology-iri https://bzk.fiz-karlsruhe.de/ontology/ -V https://bzk.fiz-karlsruhe.de/ontology/$(VERSION) \
	--annotation http://purl.org/dc/terms/created "$(TODAY)" \
	--annotation http://purl.org/dc/terms/bibliographicCitation "$(CITATION)"  \
	#--link-annotation owl:priorVersion https://bzk.fiz-karlsruhe.de/ontology/$(PRIOR_VERSION) \


update-ontology-annotations: 
	$(ROBOT) annotate --input ../../bzk.owl $(ALL_ANNOTATIONS_AND_VERSION) --output ../../bzk.owl 
	$(ROBOT) annotate --input ../../bzk.ttl $(ALL_ANNOTATIONS_AND_VERSION) --output ../../bzk.ttl 
	$(ROBOT) annotate --input ../../bzk-full.owl $(ALL_ANNOTATIONS_AND_VERSION) --output ../../bzk-full.owl 
	$(ROBOT) annotate --input ../../bzk-full.ttl $(ALL_ANNOTATIONS_AND_VERSION) --output ../../bzk-full.ttl 
	$(ROBOT) annotate --input ../../bzk-extension.owl $(ALL_ANNOTATIONS) --output ../../bzk-extension.owl 
	$(ROBOT) annotate --input ../../bzk-extension.ttl $(ALL_ANNOTATIONS) --output ../../bzk-extension.ttl 
	$(ROBOT) annotate --input ../../bzk-extension-full.owl $(ALL_ANNOTATIONS) --output ../../bzk-extension-full.owl 
	$(ROBOT) annotate --input ../../bzk-extension-full.ttl $(ALL_ANNOTATIONS) --output ../../bzk-extension-full.ttl 


