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

$(ONT)-extension.ttl: $(ONT).ttl
	$(ROBOT) merge -i bzk-extension.owl -o $@ 

