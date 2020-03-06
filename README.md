# Ocular Immune-Mediated Inflammatory Diseases Ontology (**OcIMIDo**)

#### See :grey_exclamation: [Issues](https://github.com/sap218/ocular-immune-mediated-inflammatory-disease-ontology/issues)  for the term-tracker

---

**Creators**

* Samantha C Pendleton (University of Birmingham, UK ) | [samanfapc@gmail.com](mailto:samanfapc@gmail.com) | [Twitter](https://twitter.com/sap218) | [GitHub](https://github.com/sap218)
* Tasanee Braithwaite (NHS Foundation Trust, UK)  | [tasaneebraithwaite@gmail.com](mailto:tasaneebraithwaite@gmail.com) | [Twitter](https://twitter.com/tasbraithwaite) | [GitHub](https://github.com/tasbraithwaite)  

---

**License**

[https://creativecommons.org/licenses/by/3.0/](https://creativecommons.org/licenses/by/3.0/) - please see [LICENSE](https://github.com/sap218/ocimido/blob/master/LICENSE) for further information

---

* Ontology is located in :file_folder: [`ontology`](https://github.com/sap218/ocimido/tree/master/ontology) directory
* Ontology named appropriately :page_facing_up: [`ocimido.owl`](https://github.com/sap218/ocimido/blob/master/ontology/ocimido.owl) 

**Development**

* Ontology was built with `Protégé`
* Ontology has appropriate concepts: codes (`#OCIMIDO_00001`), class labels, comments/definitions, relationships/axioms 
* Foundation based on [Royal College Clinical Dataset 2018](https://www.rcophth.ac.uk/wp-content/uploads/2014/12/Uveitis-Data-Set-Oct-2018.pdf) [RCOphth]
* Classes curated from other biomedical ontologies and included with cross-references (e.g `HPO`, `SNOMED-CT`, & more)
* Expert opinion on other missing classes 
* Synonyms (layman's terms) extracted from [Olivia's Vision](http://www.oliviasvision.org/) [OV] public (open-access) forum, with permission using a tf-idf statistical analysis

---

**Motivation**

* ontology is needed because there is a lack of controlled vocabulary for eye inflammation disorders and diseases
* `DOID` and `HPO` exist however are limited: they are domain ontologies, we need an application ontology
* target audience is aimed for those who wish to use an ontology for patient-specific text (layman's terms)

---

**Requirements / Development Community**

*Contributors*

* Luke Slater
* Alastair Denniston
* Georgios Gkoutos

* See :grey_exclamation: [Issues](https://github.com/sap218/ocular-immune-mediated-inflammatory-disease-ontology/issues)  for the term-tracker if user wants to submit a request (new term/change/suggestion) - if frequent issues when an additional main contributor will be added

---

**Knowledge Acquisition**

* an expert derived ontology
* used other biomedical ontologies from online repositories
* foundation based on [RCOphth](https://www.rcophth.ac.uk/wp-content/uploads/2014/12/Uveitis-Data-Set-Oct-2018.pdf)
* layman's terms based on [OV](http://www.oliviasvision.org/)

---

**Ontology Content**

* `IRI`s: https://github.com/sap218/ocimido/blob/master/ontology/ocimido.owl#OCIMIDO_00001

* 615 classes, with 210 of those extracted from the [RCOphth](https://www.rcophth.ac.uk/wp-content/uploads/2014/12/Uveitis-Data-Set-Oct-2018.pdf) and 234 expert opinion
* entities/concepts are `OCIMIDO` - not to be confused w/ ontology abbreviation: OcIMIDo
* 1567 relationships (including axioms)
* 2600 annotations with those 948 being xrefs (570 to medical ontologies which of those 363 xrefs to SNOMED-CT)
* and a total of 131 synonyms from [OV](http://www.oliviasvision.org/)

* OWL/XML Syntax w/ `Protégé`
* used `Protégé’s` `Pellet` reasoner which resulted in a coherent and consistent ontology

* ontologies cross-references: `DOID`, `HPO`, `ORDO`, `PATO`, `UBERON`, `ICD-10`, `Read Codes`, `SNOMED-CT`

* relationships (not including inverses): `adjacent to`, `part of`, `characterised by`, `investigated by`, `is a`, `occurs in`, `treatment of`

* metadata/annotations: `rdfs:comment`, `rdfs:databaseCrossReference`, `rdfs:extractedFrom`, `rdfs:hasExactSynonym`, `rdfs:synonymExtraction`

---

Following the MIRO guidelines for reporting on an ontology [1] - additional content will be included in the OcIMIDo paper

[1] Matentzoglu, N., Malone, J., Mungall, C. and Stevens, R., 2018. MIRO: guidelines for minimum information for the reporting of an ontology. *Journal of biomedical semantics*, 9(1), p.6. accessed via: https://jbiomedsem.biomedcentral.com/articles/10.1186/s13326-017-0172-7
