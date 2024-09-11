#!/usr/bin/env python3

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Britain is a place. Mary is a doctor.")

for ent in doc.ents:
    print(ent.text, ent.label_)
    
# gets all the instances of gpe so we can flag it or change it to loc
# so we create a custom component, a custom component allows changes to the doc object along the way in the pipeline
from spacy.language import Language
@Language.component("remove_gpe")
def removeGPE(doc):
    original_ents = list(doc.ents)
    for ent in doc.ents:
        if ent.label_ == "GPE":
            original_ents.remove(ent)
    doc.ents = original_ents
    return (doc)

nlp.add_pipe("remove_gpe")

nlp.analyze_pipes()
print("-"*100)
doc = nlp("Britain is a place. Mary is a doctor.")
for ent in doc.ents:
    print(ent.text, ent.label_)


    