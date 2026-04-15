## Customize Makefile settings for bzk
## 
## If you need to customize your Makefile, make
## changes here rather than in the main Makefile

$(IMPORTDIR)/schema_import.owl: $(MIRRORDIR)/schema.owl $(IMPORTDIR)/schema_terms.txt | all_robot_plugins
	$(ROBOT) annotate --input $< --remove-annotations \
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
		        --term-file $(IMPORTDIR)/rico_terms.txt $(T_IMPORTSEED) \
		        --select complement --select annotation-properties \
		 $(ANNOTATE_CONVERT_FILE)

$(IMPORTDIR)/pico_import.owl: $(MIRRORDIR)/pico.owl $(IMPORTDIR)/pico_terms.txt | all_robot_plugins
	$(ROBOT) annotate --input $< --remove-annotations \
		 extract --term-file $(IMPORTDIR)/pico_terms.txt  \
		         --force true --copy-ontology-annotations true \
		         --individuals include \
		         --method STAR \
		 remove $(foreach p, $(ANNOTATION_PROPERTIES), --term $(p)) \
		        --term-file $(IMPORTDIR)/pico_terms.txt $(T_IMPORTSEED) \
		        --select complement --select annotation-properties \
		 $(ANNOTATE_CONVERT_FILE)



$(IMPORTDIR)/prov_import.owl: $(MIRRORDIR)/prov.owl $(IMPORTDIR)/prov_terms.txt | all_robot_plugins
	$(ROBOT) annotate --input $< --remove-annotations \
		 extract --term-file $(IMPORTDIR)/prov_terms.txt  \
		         --force true --copy-ontology-annotations true \
		         --individuals include \
		         --method STAR \
		 remove $(foreach p, $(ANNOTATION_PROPERTIES), --term $(p)) \
		        --term-file $(IMPORTDIR)/prov_terms.txt $(T_IMPORTSEED) \
		        --select complement --select annotation-properties \
		 $(ANNOTATE_CONVERT_FILE)		 