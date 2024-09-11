#!/usr/bin/env python3

import spacy
from spacy.matcher import Matcher
import json

with open("data/alice.json", "r") as f:
    data = json.load(f)

nlp = spacy.load("en_core_web_sm")

text = data[0][2][0]
print(text)

# can replace syntax in texts
text = text.replace("`","'")
print(text)

print("-" * 100)
# now we create a pattern that gets all instances of a quotation

matcher = Matcher(nlp.vocab)
# matches with the quotation mark with ORTH, then gets the sentence in between those quotation marks
pattern = [{"ORTH": "'"},
           {"IS_ALPHA": True, "OP": "+"},
           # * allows the pattern to match 0 or more times
           {"IS_PUNCT": True, "OP": "*"},
           {"ORTH": "'"}
        ]
matcher.add("PROPER_NOUN", [pattern], greedy="LONGEST")
doc = nlp(text)
matches = matcher(doc)
# sorts the tuples by the start token
matches.sort(key = lambda x: x[1])
print(len(matches))
for match in matches[:10]:
    print(match, doc[match[1]:match[2]])
    
print("-" * 100)

# we add a list of lemmatized forms of verbs

speak_lemmas = ["think", "say"]
matcher = Matcher(nlp.vocab)
# matches with the quotation mark with ORTH, then gets the sentence in between those quotation marks
pattern = [{"ORTH": "'"},
           {"IS_ALPHA": True, "OP": "+"},
           # * allows the pattern to match 0 or more times
           {"IS_PUNCT": True, "OP": "*"},
           {"ORTH": "'"},
           # the next token needs to be a verb, and has to have a lemmatized form that is in the list of speak_lemmas
           {"POS": "VERB", "LEMMA": {"IN": speak_lemmas}},
          
           # we can also find who the speaker is
          
           {"POS": "PROPN", "OP": "+"},
           {"ORTH": "'"},
           {"IS_ALPHA": True, "OP": "+"},
           {"IS_PUNCT": True, "OP": "*"},
           {"ORTH": "'"},
        ]
matcher.add("PROPER_NOUN", [pattern], greedy="LONGEST")
doc = nlp(text)
matches = matcher(doc)
# sorts the tuples by the start token
matches.sort(key = lambda x: x[1])
print(len(matches))
for match in matches[:10]:
    print(match, doc[match[1]:match[2]])
 
 
print("-" * 100) 
# iterates over the whole chapter    
for text in data[0][2]:
    text = text.replace("`","'")
    doc = nlp(text)
    matches = matcher(doc)
    matches.sort(key = lambda x: x[1])
    for match in matches[:10]:
        print(match, doc[match[1]:match[2]])
    
