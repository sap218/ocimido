# MIRO Guidelines

Below we follow the MIRO guidelines for reporting on an ontology [1]. 

---

**A. The basics**
  * A.1 Ocular Immune-Mediated Inflammatory Diseases Ontology (OcIMIDo) v1.2.0.
  * A.2 Ontology owner: [Samantha Pendleton](mailto:samanfapc@gmail.com) MSc (Institute of Cancer and Genomic Sciences, University of Birmingham, UK) & [Tasanee Braithwaite](mailto:tasaneebraithwaite@gmail.com) DM (The Medical Eye Unit, St Thomas’ Hospital NHS Foundation Trust, London, UK).
  * A.3 [Licence](https://github.com/sap218/ocimido/blob/master/LICENSE), which governs the permissions surrounding the ontology, https://creativecommons.org/licenses/by/3.0/.
  * A.4 Located in GitHub repository `ontology` directory: `ocimido.owl`.
  * A.5 GitHub repository: `https://github.com/sap218/ocimido`.
  * A.6 Methodological framework: used [Protégé](https://protege.stanford.edu/) software for ontology building and used the tf-idf statistical analysis for curation of patient-preferred synonyms.

**B. Motivation**
  * B.1 Ontology is required as there currently lacks controlled vocabulary for ocular immune-mediated inflammatory diseases & the need for understanding the “patient-voice” [2], currently biomedical ontologies don't fully represent our domain of interest.
  * B.2 OcIMIDo was developed from domain experts and clinical guidelines, additionally derived from other biomedical ontologies, which are currently limited in the ocular domain, such as DOID, HPO, and ORDO.
  * B.3 Target audience are those in the ophthalmology research area, or even extended to other medical domains. Plus for those who wish to create an ontology and expand with synonyms: we present the time-efficient tf-idf method.

**C. Scope, requirements, development community**
  * C.1 The requirements of the ontology is to be an extensive vocabulary for ocular-related disorders and their associated diseases, in addition to patient-preferred synonyms. The ontology includes therapeutic interventions, investigations, symptoms, complications, genotypic data, and more. 
  * C.2 Development community: [Samantha Pendleton](mailto:samanfapc@gmail.com) MSc (Institute of Cancer and Genomic Sciences, University of Birmingham, UK) & [Tasanee Braithwaite](mailto:tasaneebraithwaite@gmail.com) DM (The Medical Eye Unit, St Thomas’ Hospital NHS Foundation Trust, London, UK). In addition to Luke T Slater PhD, Alastair K Denniston PhD, and Georgios V Gkoutos PhD.
  * C.3 Issue tracking system used for future developements/requests/bugs: `https://github.com/sap218/ocimido/issues`. 

**D. Knowledge acquisition**
  * D.1 Foundation built from clinical guidelines and experts derived list of terms to be included – and then an extensive review of current biomedical ontologies.
  * D.2 Clinical guidleines included reports/datasets from the Royal College of Ophthalmology Consensus document for Uveitis [3]. Access to current biomedical ontologies were made via the [Ontology Lookup Service](https://www.ebi.ac.uk/ols/index).
  * D.3 Experts decided on the contents of OcIMIDo from the biomedical ontologies by searching through and extracting most relevant terms, for example, from UBERON we extracted eye-related anatomy concepts, e.g. `uvea` [UBERON:0001768]. However we avoided `iris nevus` [HP:0011525] from HPO.

**E. Ontology content**
  * E.1 Currently, ontology format is `RDF/XML` OWL, however v1.2.0 older format is available as `OWL/XML` - ask SP if you wish for an alternative ontology format or advice.
  * E.2 Used [Protégé](https://protege.stanford.edu/) to develop the ontology with Git version control.
  * E.3 Ontology metrics, as of 14-06-2020 version 1.2.0 (see [`CHANGELOG.md`](https://github.com/sap218/ocimido/blob/master/CHANGELOG.md)) there are a total of 661 classes, 1661 relationships and axioms, 2851 annotations, including 1131 database cross-references, and 187 patient-preferred synonyms.
  * E.4 Cross-references ontologies inclue: DOID [4], HPO [5], ORDO [6], PATO [7], and UBERON [8].
  * E.5 IRI for OcIMIDo is: `https://github.com/sap218/ocimido/blob/master/ontology/ocimido.owl#OCIMIDO_00000`.
  * E.6 Identifier generation policy: Protégé’s preferences schema is that ontology’s entities are to have the prefix “OCIMIDO” followed by an underscore then a five digit number: currently they consists of 00001 up to ~000600. All classes have OCIMIDO prefix and own numeric identifier since OcIMIDo avoids importing axioms from other ontologies.
  * E.7 Entity metadata policy: currently `exact` synonyms in the ontology are additional clinical/medical terms. However `broad` synonyms are to be used for all Layman terms from the tf-idf method extracting from [Olivia's Vision](http://www.oliviasvision.org/) open forum.
  * E.8 BFO [9] and RO [10] were used as upper ontologies for relationships.
  * E.9 Currently, relationships in OcIMIDo are cross-referenced, such as `adjacent to` and `treatment of` from RO. We defined our own, `investigated by` (inverse `investigation for`) based on the investgations from the clinical guidelines document [3].
  * E.10 Axiom patterns are inferred from the ontology structure itself (`subclass`) and by defined relationships, `is a` - currently only 100% true cases.

**F. Managing change**
  * F.1 Sustainability plan: OcIMIDo is freely available on GitHub and the creator, Samantha Pendleton, will constantly update/change based on expert opinion or via Issue notifications. Anyone from the community can suggest new terms, but with sufficient evidence/justification. Potentially users can `fork` the ontology and make their own changes, which then allows the creator to merge these changes. If often particular individuals are making positive/appropriate changes they can be given direct access to co-maintain the ontology with the creator.
  * F.2 There is the change log ([CHANGELOG.md](https://github.com/sap218/ocimido/blob/master/CHANGELOG.md)) for entitles which need to be removed/split/redefined, additionally we can annotate these entities as obsolete. 
  * F.3 Ontology will follow “semantic versioning” guidelines and that it will maintain as version 1 unless a major foundation change is made then it will become version 2. Otherwise additional terms/fixes will increment to version 1.1 or 1.0.1 over time.

**G. Quality Assurance**
  * G.1 Successful testing on the [Olivia's Vision](http://www.oliviasvision.org/) public forum for the `broad` synonyms plus annotations. Also used [Protégé](https://protege.stanford.edu/) Pellet reasoner to ensure a coherent and consistent ontology. Experts in the opthamology background deemed/judged the ontology achieves the claims. 
  * G.2 Ontology is novel and first in ophthalmology. Additionally this method of building (tf-idf) is validated and proven a fast approach to synonym curation. OcIMIDo meets the stated requirements as an ontology suitable for the opthamology domain in additon to capturing the patient voice.
  * G.3 An example of application is using the ontology for sentiment analysis on the forum. Additionally future applications include GWAS analysis on the UK Biobank cohort and other electronic health databases - OcIMIDo provides an implicit axiomatic structure for data annotated with SNOMED-CT, ICD-10, ICD-9, or Read codes as these are included as cross-references in the ontology, enhancing the potential value of OcIMIDo for searching and curating unstructured clinical data.
  * G.4 Ontology available on other platforms, such as [BioPortal](https://bioportal.bioontology.org/ontologies/OCIMIDO/).
  * G.5 Current evidence of OcIMIDo application is text mining and sentiment analysis on forum data. To read more, the [manuscript](https://doi.org/10.1016/j.compbiomed.2021.104542) is available online. We show that using clinical terms in addition to patient-preferred terms, text mining efforts are increased, and the sentiment analysis provided insight of the role online forum play for patients/carers.

---

[1] Matentzoglu, N., Malone, J., Mungall, C., & Stevens, R. (2018). MIRO: guidelines for minimum information for the reporting of an ontology. Journal of Biomedical Semantics, 9(1), 6.

[2] Dean, S., Mathers, J. M., Calvert, M., Kyte, D. G., Conroy, D., Folkard, A., Southworth, S., Murray, P. I., & Denniston, A. K. (2017). “The patient is speaking”: discovering the patient voice in ophthalmology. The British Journal of Ophthalmology, 101(6), 700–708.

[3] Denniston, A. K., Lee, R. W., Pavesio, C., Stanford, M. R., Murray, P. I., Okada, A., Sen, H. N., & Dick, A. D. (2018). Uveitis Dataset Clinical Dataset. The Royal College of Ophthalmologists. https://www.rcophth.ac.uk/wp-content/uploads/2014/12/Uveitis-Data-Set-Oct-2018.pdf

[4] Schriml, L. M., Arze, C., Nadendla, S., Chang, Y.-W. W., Mazaitis, M., Felix, V., Feng, G., & Kibbe, W. A. (2012). Disease Ontology: a backbone for disease semantic integration. Nucleic Acids Research, 40(Database issue), D940–D946.

[5] Robinson, P. N., Köhler, S., Bauer, S., Seelow, D., Horn, D., & Mundlos, S. (2008). The Human Phenotype Ontology: a tool for annotating and analyzing human hereditary disease. American Journal of Human Genetics, 83(5), 610–615.

[6] Vasant, D., Chanas, L., Malone, J., Hanauer, M., Olry, A., Jupp, S., Robinson, P. N., Parkinson, H., & Rath, A. (2014). Ordo: An ontology connecting rare disease, epidemiology and genetic data. Proceedings of ISMB, 30. 

[7] Gkoutos, G. V., Schofield, P. N., & Hoehndorf, R. (2018). The anatomy of phenotype ontologies: principles, properties and applications. Briefings in Bioinformatics, 19(5), 1008–1021.

[8] Mungall, C. J., Torniai, C., Gkoutos, G. V., Lewis, S. E., & Haendel, M. A. (2012). Uberon, an integrative multi-species anatomy ontology. Genome Biology, 13(1), R5.

[9] Smith, B., Kumar, A., & Bittner, T. (2005). Basic Formal Ontology for Bioinformatics. IFOMIS Reports.

[10] Smith, B., Ceusters, W., Klagges, B., Köhler, J., Kumar, A., Lomax, J., Mungall, C., Neuhaus, F., Rector, A. L., & Rosse, C. (2005). Relations in biomedical ontologies. Genome Biology, 6(5), R46.
