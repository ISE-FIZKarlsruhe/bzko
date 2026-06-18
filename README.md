# BZK Ontology (BZKO)

The **BZK Ontology (BZKO)** is a BFO-based ontology for representing the **Federal Central Register (Bundeszentralkartei, BZK)** of the German *Wiedergutmachung* process. The ontology provides a semantically rigorous representation of BZK index cards documenting compensation claims submitted by victims of National Socialist persecution and their relatives.

BZKO has been developed within the **Themenportal Wiedergutmachung** project to support semantic integration, provenance-aware knowledge graph construction, and interoperability with archival and Digital Humanities infrastructures.

---

## Overview

The ontology models the entities and relations represented on BZK index cards, including:

- BZK cards and their digitized representations
- Applicants and persecutees
- Compensation offices
- Personal names and identifiers
- Birth and death information
- Addresses and places
- BZK numbers
- Card layouts
- Provenance links between extracted information and archival sources

The ontology follows the **Basic Formal Ontology (BFO)** and reuses existing ontology modules wherever possible to maximize interoperability and semantic consistency.

---

## Scientific Motivation

BZKO is more than a domain vocabulary for historical index cards. It provides a **general ontology engineering approach for archival resources**, combining ontological rigor with practical interoperability.

The ontology distinguishes between a **knowledge layer**, containing ontologically grounded domain entities, and an **extension layer**, providing mappings to archival standards and user-oriented shortcut relations. This modular architecture enables:

- semantic interoperability with existing Digital Humanities infrastructures,
- provenance-preserving knowledge graph generation,
- modular ontology reuse,
- logically rigorous modeling based on BFO while remaining compatible with archival standards such as RiC-O.

---

## Two-layer Architecture

BZKO is organized into two ontology layers.

### Knowledge Layer (`bzk.owl`)

The knowledge layer contains the **core domain model**:

- primitive ontology classes,
- rigid entities,
- BFO-compliant representations,
- domain-specific object properties.

This layer captures the ontological structure of the BZK cards independently of application-specific mappings.

### Extension Layer (`bzk-extension.owl`)

The extension layer provides:

- mappings to external ontologies,
- shortcut relations,
- provenance relations,
- interoperability constructs,
- SPARQL CONSTRUCT mappings.

This separation allows applications to reuse the core ontology independently from archival or interoperability requirements.

---

## Imported Ontologies

BZKO builds upon several existing semantic resources:

- Basic Formal Ontology (BFO)
- NFDIcore
- Information Artifact Ontology (IAO)
- Relations Ontology (RO)
- Ontology for Biomedical Investigations (OBI)
- Records in Contexts Ontology (RiC-O)
- Provenance Ontology (PROV-O)
- Persons in Context (PiCo)
- Schema.org

The extension layer provides mappings to these ontologies while preserving the ontological commitments of the knowledge layer.

---

## Design Principles

The ontology follows several design principles:

- **BFO compliance** for ontological consistency.
- **Role-based modeling**, distinguishing persons from context-dependent roles such as applicants and persecutees.
- **Modular architecture**, separating core semantics from interoperability mappings.
- **Provenance preservation**, linking extracted information back to digitized archival sources.
- **Ontology reuse** through alignment with established community ontologies.
- **Compatibility with Digital Humanities infrastructures.**

---

## Repository Structure

This repository follows the standard **Ontology Development Kit (ODK)** layout.

```
src/
└── ontology/
    ├── imports/			
    ├── components/
    ├── bzk-edit.owl
    └── bzk-extension-edit.owl
bzk.ttl		# release artefact of knowledge layer
bzk.owl		# release artefact of knowledge layer
bzk-extension.ttl   # release artefact of extension layer 
bzk-extension.owl 	# release artefact of extension layer 

```

Release artifacts are generated automatically through the ODK build workflow.

---

## Building the Ontology

The repository uses the **Ontology Development Kit (ODK)**.

Prepare a release:

```bash
cd src/ontology
sh run.sh make 
```

Generate all release artifacts:

```bash
sh release.sh
```

For more information about ODK, see the official documentation:

[https://github.com/INCATools/ontology-development-kit](https://github.com/INCATools/ontology-development-kit)

---

## Citation

BZKO Ontology. Version 1.0.0, [https://bzk.fiz-karlsruhe.de/ontology/](https://bzk.fiz-karlsruhe.de/ontology/)

---

## License

The ontolgy is published under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

See the `LICENSE.txt` file in this repository for licensing information.


---

## Acknowledgements

BZKO is being developed within the **Themenportal Wiedergutmachung** project to support the semantic integration and analysis of archival sources documenting compensation processes for victims of National Socialist persecution.

---

## Contributing

Contributions, bug reports, and feature requests are welcome through GitHub Issues and Pull Requests.