# OcIMIDo Documentation

[Home](README.md) | [Documentation](MIRO.md) | [License](LICENSE.md) | [Changelog](CHANGELOG.md) | [Manuscript](https://doi.org/10.1016/j.compbiomed.2021.104542) | [Bioportal](https://bioportal.bioontology.org/ontologies/OCIMIDO)

## MIRO Guidelines

Below we follow the MIRO guidelines for reporting on an ontology [1]. 

---

**A. The basics**
  * A.1 Ocular Immune-Mediated Inflammatory Diseases Ontology (OcIMIDo) v1.2.0.
  * A.2 Ontology owners: [Samantha Pendleton](mailto:samanfapc@gmail.com) MSc, PhD student at Institute of Cancer and Genomic Sciences, University of Birmingham, UK & [Tasanee Braithwaite](mailto:tasaneebraithwaite@gmail.com) DM, Ophthalmologist at The Medical Eye Unit, St Thomas’ Hospital NHS Foundation Trust, London, UK.
  * A.3 [Licence](LICENSE.md), which governs the permissions surrounding the ontology, https://creativecommons.org/licenses/by/3.0/. Essentially users are free to use and edit, with appropriate credit, which can be cited via the [Manuscript](https://doi.org/10.1016/j.compbiomed.2021.104542). If users edit, they are free to make changes via [Issues](https://github.com/sap218/ocimido/issues) or a pull-request.
  * A.4 Located in GitHub repository `ocimido.owl`. However available on public repository [Bioportal](https://bioportal.bioontology.org/ontologies/OCIMIDO).
  * A.5 GitHub repository: `https://github.com/sap218/ocimido`.
  * A.6 Methodological framework: used [Protégé](https://protege.stanford.edu/) software for ontology building and used the TF-IDF statistical analysis for curation of patient-preferred synonyms for ontology expansion.

**B. Motivation**
  * B.1 Ontology is required as there currently lacks controlled vocabulary for ocular immune-mediated inflammatory diseases (IMID) & the need for understanding the “patient-voice” [2]. Currently biomedical ontologies don't fully represent our domain of interest and so there needed an application ontology for ocular IMIDs and their relevant clinical information. 
  * B.2 OcIMIDo was developed from domain experts and clinical guidelines, additionally derived from other biomedical ontologies, which are currently limited in the ocular domain, such as DOID, HPO, and ORDO. Some examples include HPO and DOID, whilst despite including types of uveitis, they lack inner subclasses. 
  * B.3 Target audience are those in the ophthalmology research area, or even extended to other medical domains. Plus for those who wish to create an ontology and expand with synonyms: we present the time-efficient TF-IDF method.

**C. Scope, requirements, development community**
  * C.1 The requirements of the ontology is to be an extensive vocabulary for ocular-related disorders and their associated diseases, in addition to patient-preferred synonyms. The ontology includes therapeutic interventions, investigations, symptoms, complications, genotypic data, and more. 
  * C.2 Development community: [Samantha Pendleton](mailto:samanfapc@gmail.com) MSc, PhD student at Institute of Cancer and Genomic Sciences, University of Birmingham, UK & [Tasanee Braithwaite](mailto:tasaneebraithwaite@gmail.com) DM, Ophthalmologist at The Medical Eye Unit, St Thomas’ Hospital NHS Foundation Trust, London, UK. In addition to Luke T Slater PhD, Alastair K Denniston PhD, and Georgios V Gkoutos PhD.
  * C.3 Issue tracking system used for future developements/requests/bugs: `https://github.com/sap218/ocimido/issues`. The [Issues](https://github.com/sap218/ocimido/issues) tab allows users to request information/classes, discuss future developments, or express ontological opinions. Users who make substantial additions to OcIMIDo can create a pull-request, which the ontology owners will review. 

**D. Knowledge acquisition**
  * D.1 Foundation built from clinical guidelines and experts derived list of terms to be included – and then an extensive review of current biomedical ontologies.
  * D.2 Clinical guidleines included reports/datasets from the Royal College of Ophthalmology Consensus document for Uveitis [3]. Access to current biomedical ontologies were made via the [Ontology Lookup Service](https://www.ebi.ac.uk/ols/index) and [Bioportal](https://bioportal.bioontology.org/ontologies/).
  * D.3 Experts decided on the contents of OcIMIDo from the biomedical ontologies by searching through and extracting most relevant terms, for example, from UBERON [8] we extracted eye-related anatomy concepts: `uvea` [UBERON:0001768]. However we avoided `iris nevus` [HP:0011525] from HPO [5].

**E. Ontology content**
  * E.1 Currently, ontology (v1.2.0) format is `RDF/XML OWL` - users are free to create an [Issues](https://github.com/sap218/ocimido/issues) to request information on alternative formats or advice.
  * E.2 Used [Protégé](https://protege.stanford.edu/) to develop the ontology with Git version control.
  * E.3 Ontology metrics, as of v1.2.0 (see [Changelog](CHANGELOG.md) for 14-06-2020) there are a total of 661 classes, 1661 relationships and axioms, 2851 annotations, including 1131 database cross-references, and 187 patient-preferred synonyms.
  * E.4 Cross-references ontologies inclue: DOID [4], HPO [5], ORDO [6], PATO [7], and UBERON [8].
  * E.5 IRI for OcIMIDo is: `https://github.com/sap218/ocimido/blob/master/ocimido.owl#OCIMIDO_00000`.
  * E.6 Identifier generation policy: Protégé’s preferences schema is that ontology’s entities are to have the prefix “OCIMIDO” followed by an underscore then a five digit number: currently they consists of 00001 up to ~000600. All classes have OCIMIDO prefix and own numeric identifier since OcIMIDo avoids importing axioms from other ontologies.
  * E.7 Entity metadata policy: currently `exact` synonyms in the ontology are additional clinical/medical terms. However `broad` synonyms are to be used for all Layman terms from the TF-IDF extracting from [Olivia's Vision](http://www.oliviasvision.org/) open forum.
  * E.8 BFO [9] and RO [10] were used as upper ontologies for relationships.
  * E.9 Currently, relationships in OcIMIDo are cross-referenced, such as `adjacent to` and `treatment of` from RO. We defined our own, `investigated by` (inverse `investigation for`) based on the investgations from the clinical guidelines document [3].
  * E.10 Axiom patterns are inferred from the ontology structure itself (`subclass`) and by defined relationships, `is a` - currently only 100% true cases.

**F. Managing change**
  * F.1 Sustainability plan: OcIMIDo is freely available on [GitHub](https://github.com/sap218/ocimido) and released on [Bioportal](https://bioportal.bioontology.org/ontologies/OCIMIDO). Ontology creator/owner, Samantha Pendleton, will constantly update/change based on expert opinion or via [Issues](https://github.com/sap218/ocimido/issues) and pull-request notifications. Anyone from the community can suggest new terms, but with sufficient evidence/justification. If particular users, with correct ontological use and credidentials, are making positive/appropriate changes often, they can be given direct access to co-maintain the ontology with the creator.
  * F.2 There is a [Changelog](CHANGELOG.md) to major changes to be noted: e.g. entitles which need to be removed/split/redefined, additional metadata, or ontology restructuring. 
  * F.3 Ontology will follow “semantic versioning” guidelines and that it will maintain as version 1 unless a major foundation change is made then it will become version 2. Otherwise additional terms/fixes will increment to version 1.2.1 or 1.3.0 over time (currently OcIMIDo is v1.2.0).

**G. Quality Assurance**
  * G.1 Successful testing on the [Olivia's Vision](http://www.oliviasvision.org/) public forum for the `broad` synonyms plus annotations. Also used [Protégé](https://protege.stanford.edu/) Pellet reasoner to ensure a coherent and consistent ontology. Experts in the opthamology background deemed/judged the ontology achieves the claims. 
  * G.2 Ontology is novel and first in ophthalmology. Additionally this method of building (TF-IDF) is validated and proven a fast approach to synonym curation. OcIMIDo meets the stated requirements as an ontology suitable for the opthamology domain in additon to capturing the patient voice.
  * G.3 An example of application is using the ontology for sentiment analysis on the forum in the [Manuscript](https://doi.org/10.1016/j.compbiomed.2021.104542). Additionally future applications include semantic similarity via implicit axiomatic structure, or annotation of electronic health databases via x-ref of medical terminologies SNOMED-CT, ICD-10, ICD-9, or Read codes.
  * G.4 Ontology available on other platforms, such as [BioPortal](https://bioportal.bioontology.org/ontologies/OCIMIDO/) and will be updated accordingly to version updates.
  * G.5 Current evidence of OcIMIDo application is text mining and sentiment analysis on forum data. To read more, the [Manuscript](https://doi.org/10.1016/j.compbiomed.2021.104542) is available online. We show that using clinical terms in addition to patient-preferred terms, text mining efforts are increased, and the sentiment analysis provided insight of the role online forum play for patients/carers.

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
