# Official Use

[Overview](README.md) · [All CQs](all-cqs.md)

Federal and state archives, compensation offices, public authorities, and lawyers checking whether a file exists, where it is kept, and whether published cards comply with legal requirements.

TP WGM: *Themenportal Wiedergutmachung* · BZK KG: *BZK Knowledge Graph*

**5 personas · 10 competency questions**

- [P20 · Kevin](#kevin-which-cards-may-need-to-be-removed-from-the-online-collection): Which cards may need to be removed from the online collection?
- [P21 · Sabine](#sabine-do-our-archives-files-match-the-bzk-cards): Do our archive's files match the BZK cards?
- [P22 · Mrs. C.L. Erk](#mrs-cl-erk-does-a-file-already-exist-and-where-is-it-kept): Does a file already exist, and where is it kept?
- [P23 · Mr. Grünberg](#mr-grünberg-did-this-applicant-receive-benefits-before): Did this applicant receive benefits before?
- [P24 · Daniel](#daniel-can-my-client-claim-german-citizenship): Can my client claim German citizenship?

---

## Kevin: "Which cards may need to be removed from the online collection?"

| | |
|---|---|
| **Persona name** | Kevin (P20) |
| **Role** | Employee at the Federal Archives |
| **Goal** | Kevin is responsible for the legal compliance of published BZK data. He has to check the legal compliance of the data put online and, in particular, to check cards from a specific region that may be problematic in a more targeted way. |
| **Research scenario** | As he has lately received many complaints from Hesse that some cards should be removed from the online collection, he browses TP WGM, filtering the cards from the Hessian State Archives. For more detailed, layout-specific information, he uses BZK KG, since the layout type is not a search criterion in TP WGM. |
| **User stories** | **US1** As an archive employee responsible for legal compliance, I want to filter cards by originating archive, so that I can review a specific region's holdings (e.g., the Hessian State Archives) for compliance issues.<br>**US2** As an archive employee, I want to see the layout type of a BZK card, so that I can assess whether a card should be removed from the online collection.<br>**US3** As an archive employee, I want to efficiently trace a complaint back to the specific card(s) it concerns, so that I can review and act on legal compliance concerns raised by archives. |
| **Competency questions** | **P20-CQ1** Which BZK cards originate from the archive X?<br>**P20-CQ2** What is the layout type of BZK card X? ⚠️ |
| **Notes** | **Available in the BZK KG (P20-CQ2):** The layout type is not a search criterion in TP WGM; however, BZK KG can answer this query. |

[↑ Back to top](#official-use)

---

## Sabine: "Do our archive's files match the BZK cards?"

| | |
|---|---|
| **Persona name** | Sabine (P21) |
| **Role** | Archivist at the State Archives of Baden-Württemberg |
| **Goal** | Sabine works at the State Archives of Baden-Württemberg and is in charge of the compensation files there. To check the number of files available in her archive (as a holding archive), she compares it with the number of BZK cards referring to them. |
| **Research scenario** | She browses TP WGM, filtering the cards from the State Archives of Baden-Württemberg, bearing in mind that only freely accessible cards can be found there. |
| **User stories** | **US1** As an archivist in charge of a state archive's holdings, I want to filter BZK cards by holding archive, so that I can see how many cards reference files held in the State Archives of Baden-Württemberg.<br>**US2** As an archivist, I want to know that only "free" (unrestricted) cards are searchable online, so that I can account for restricted cards when comparing counts.<br>**US3** As an archivist, I want to compare the number of files physically held in my archive against the number of BZK cards referencing that archive, so that I can identify discrepancies. |
| **Competency questions** | **P21-CQ1** How many BZK cards reference archive X as their holding archive? ⚠️<br>**P21-CQ2** Which BZK cards referencing archive X are available online? |
| **Notes** | **Available in the BZK KG (P21-CQ1):** TP WGM only provides access to freely accessible cards; the total number of cards referencing an archive, including restricted cards, can only be obtained from BZK KG. |

[↑ Back to top](#official-use)

---

## Mrs. C.L. Erk: "Does a file already exist, and where is it kept?"

| | |
|---|---|
| **Persona name** | Mrs. C.L. Erk (P22) |
| **Role** | Employee at the compensation office in Düsseldorf |
| **Goal** | She is in charge of active proceedings and of answering requests for completed files. She wants to check whether a proceeding or file already exists and to know where it is kept. |
| **Research scenario** | She browses TP WGM and enters the name, date of birth, birthplace, and date of death of the person concerned, if available. She may also enter the reference number or BZK number of the case, if available. |
| **User stories** | **US1** As a compensation office employee, I want to search by name, birthdate, birthplace, and death date, so that I can check whether a proceeding or file already exists for a person.<br>**US2** As a compensation office employee, I want to search directly by reference number or BZK number, so that I can quickly locate a specific case when I already have an identifier.<br>**US3** As a compensation office employee, I want to see where an existing file is kept, so that I can direct researchers or colleagues to the correct location. |
| **Competency questions** | **P22-CQ1** Is there a BZK card associated with a person whose given name is X, family name is Y, date of birth is Z, birthplace is W, and date of death is H?<br>**P22-CQ2** What is the holding archive of the BZK card associated with the person whose given name is X, family name is Y, date of birth is Z, birthplace is W, and date of death is H?<br>**P22-CQ3** Which BZK card has the BZK number X?<br>**P22-CQ4** Which archive holds the BZK card with the BZK number X? |

[↑ Back to top](#official-use)

---

## Mr. Grünberg: "Did this applicant receive benefits before?"

| | |
|---|---|
| **Persona name** | Mr. Grünberg (P23) |
| **Role** | Government official handling a hardship-relief application |
| **Goal** | An elderly person who was persecuted submits an application for hardship relief to the relevant authority in Rhineland-Palatinate. Because the applicant no longer has any supporting documents, Mr. Grünberg wants to determine whether they previously received benefits. |
| **Research scenario** | He goes to TP WGM and enters the applicant's name, date of birth, and birthplace to find out whether a file exists somewhere. |
| **User stories** | **US1** As an authority processing a hardship-relief application, I want to search by the applicant's name, birthdate, and birthplace, so that I can determine whether a compensation file already exists for them.<br>**US2** As an authority, I want to check whether an applicant has received prior benefits, so that I can assess eligibility for hardship measures even without supporting documents. |
| **Competency questions** | **P23-CQ1** Which BZK cards are associated with a persecuted person whose given name is X, family name is Y, date of birth is Z, and birthplace is W? |

[↑ Back to top](#official-use)

---

## Daniel: "Can my client claim German citizenship?"

| | |
|---|---|
| **Persona name** | Daniel (P24) |
| **Role** | Lawyer |
| **Goal** | His client wants to know whether he can claim German citizenship. Daniel wants to determine whether his client may be eligible on the basis of the family's persecution history. The client's grandparents anglicised their first and last names after settling in the USA. |
| **Research scenario** | He goes to TP WGM and searches for the client's ancestor using their names (both the former German and the newer anglicised versions), birthplace, and date of birth to find evidence of a compensation application. |
| **User story** | **US1** As a lawyer, I want to search using both the original German and English versions of a name, along with birthplace and date of birth, so that I can find evidence of a compensation application supporting my client's citizenship claim. |
| **Competency questions** | **P24-CQ1** Which BZK cards are associated with a persecuted person whose given name is X, alternative given name is XX, family name is Y, alternative family name is YY, date of birth is Z, and birthplace is W? |
| **Notes** | Citizenship information has not been extracted and is therefore not represented in BZK KG. The existence of a BZK card for a persecuted person born in Germany can, however, serve as evidence. |

[↑ Back to top](#official-use)
