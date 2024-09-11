#!/usr/bin/env python3

import re
import spacy
from spacy.tokens import Span
from spacy.language import Language

text = "Johan Liebecht was a German college student, but Johan Schrodinger also ventured across most of Europe. The name Johan is not his real name and is used to hide his true identity."

# gets any instance of Johan and everything that starts with a capital, and everything until the word break
pattern = r"Johan [A-Z]\w+"

# uses regex to find pattern within the text
matches = re.finditer(pattern, text)
for match in matches:
    print(match)
    
print("-" * 100)

# creates blank spacy pipeline to put all info into
nlp = spacy.blank("en")
doc = nlp(text)
# original_ents = list(doc.ents)

# # multi-word token entity
# mwt_ents = []
# for match in re.finditer(pattern, doc.text):
#     # gets the span attribute
#     start, end = match.span()
#     span = doc.char_span(start, end)
#     print(span)
#     # now we get the span into our entities
#     if span is not None:
#         mwt_ents.append((span.start, span.end, span.text))
#         print(mwt_ents)  

# print("-" * 100)

# # we can inject them into our original entities
# for ent in mwt_ents:
#     start, end, name = ent
#     per_ent = Span(doc, start, end, label="PERSON")
#     original_ents.append(per_ent)
# print(doc.ents)
# print("-" * 100)
# # we inject these in the doc object
# doc.ents = original_ents
# for ent in doc.ents:
#     print(ent.text, ent.label_)
    
# print("-" * 100)

# making a custom pipe that acts as our own custom enity ruler
@Language.component("johan_ner")
def johan_ner(doc):
    pattern = r"Johan [A-Z]\w+"
    
    original_ents = list(doc.ents)

    # multi-word token entity
    mwt_ents = []
    for match in re.finditer(pattern, doc.text):
        # gets the span attribute
        start, end = match.span()
        span = doc.char_span(start, end)
        print(span)
        # now we get the span into our entities
        if span is not None:
            mwt_ents.append((span.start, span.end, span.text))
            print(mwt_ents)  

    print("-" * 100)

    # we can inject them into our original entities
    for ent in mwt_ents:
        start, end, name = ent
        per_ent = Span(doc, start, end, label="PERSON")
        original_ents.append(per_ent)
    print(doc.ents)
    print("-" * 100)
    # we inject these in the doc object
    doc.ents = original_ents
    return(doc)

nlp2 = spacy.blank("en")
nlp2.add_pipe("johan_ner")
doc2 = nlp2(text)

print(doc2.ents)










