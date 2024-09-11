#!/usr/bin/env python3

import spacy

nlp = spacy.load("en_core_web_sm")
text = "West Chestertenfieldville was referenced by Mr. Deeds."

doc = nlp(text)

#Using rules based apprach

for ent in doc.ents:
    print(ent.text, ent.label_)
    
ruler = nlp.add_pipe("entity_ruler")

print(nlp.analyze_pipes())

patterns = [
    {"label": "GPE",
    "pattern": "Chestertenfieldville"}
]

ruler.add_patterns(patterns)

doc2 = nlp(text)
for ent in doc2.ents:
    print(ent.text, ent.label_)

print("-" * 100)    
nlp2 = spacy.load("en_core_web_sm")
ruler = nlp2.add_pipe("entity_ruler", before="ner")

ruler.add_patterns(patterns)

doc = nlp2(text)
for ent in doc.ents:
    print(ent.text, ent.label_)
    
print(nlp2.analyze_pipes())


nlp3 = spacy.load("en_core_web_sm")

ruler = nlp3.add_pipe("entity_ruler", before="ner")

patterns = [
    {"label": "GPE", "pattern": "Chestertenfieldville"},
    {"label": "FILM", "pattern": "Mr. Deeds"}
]

ruler.add_patterns(patterns)
doc = nlp3(text)
print("-" * 100)
for ent in doc.ents:
    print(ent.text, ent.label_)

# toponym resolution
