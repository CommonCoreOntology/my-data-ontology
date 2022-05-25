# My Data Ontology
> The My Data Ontology (MDO) is an extension of the [Common Core Ontologies (CCO)](https://github.com/CommonCoreOntology/CommonCoreOntologies) that provides a standardized extensible semantics for representing personal data, such as that found in a user profile or wallet. As an extension of CCO, MDO also inherits and re-uses [Basic Formal Ontology (BFO)](https://github.com/BFO-ontology/BFO) and [OBO Relation Ontology](https://github.com/oborel/obo-relations). Use of the methodology and standards derived from CCO, BFO, and RO, provides an integration layer for personal data that enables a transparent and unified semantics across domains and applications.

![Ontology Archetecture](./onto_arch.png)
<br/>
<br/>
## Mapping Data Models to the My Data Ontology
1. Select a defined data model for personal information 
2. Categorized all the attributes of the data model into a table. See the example below:

    | Data Model   | Attributes              |
    | ------------ | ----------------------- |
    | Investopedia | Full Name               |
    | Investopedia | Social Security Number  |
    | Investopedia | Driver’s license        |
    | Investopedia | Mailing address         |
    | Investopedia | Credit card information |
    | Investopedia | Passport information    |
    | Investopedia | Financial information   |
    | Investopedia | Medical records         |

3. Using the [My data ontology](https://github.com/I-AM-project/my-data-ontology/blob/master/MyDataOntology.ttl), create an ontological representation for all the attributes in the data model. Add the represention to the table. Below is an example for the first row. 

    | Data Model   | Attributes | My Data Ontology Representation                                   |
    | ------------ | ---------- | ----------------------------------------------------------------- |
    | Investopedia | Full Name  | cco:Person, cco:designated_by, cco:PersonGivenName, cco:has_value |

4. Complete the process until all the attributes have a corresponding representation. 