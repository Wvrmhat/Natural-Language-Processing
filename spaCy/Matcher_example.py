#!/usr/bin/env python3

import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")

matcher = Matcher(nlp.vocab)
# extracts everything that looks like an email
# each pattern is a list within a list
pattern = [{"LIKE_EMAIL": True}]
matcher.add("EMAIL_ADDRESS", [pattern])

# we find matches with matcher(doc)
# then we print it and get a list of tuples with 3 indices
doc = nlp("This is an email address: wmattingly@aol.com")
matches = matcher(doc)
# index 0 is the lexeme, 1 is the start token and 2 is the end token
print(matches)
# shows us what the number corresponds to in the index
print(nlp.vocab[matches[0][0]].text)

print("-" * 100)

with open("data/wiki_mlk.txt", "r") as f:
    text = f.read()
print(text)
print("-" * 100)

nlp = spacy.load("en_core_web_sm")

# finds a part of speech, that corresponds with a proper noun
matcher = Matcher(nlp.vocab)
pattern = [{"POS": "PROPN"}]
matcher.add("PROPER_NOUN", [pattern])
doc = nlp(text)
matches = matcher(doc)
print(len(matches))
for match in matches[:10]:
    print(match, doc[match[1]:match[2]])

print("-" * 100)

matcher = Matcher(nlp.vocab)
# OP means operator, + meaning the required pattern matches 1 or more times, this does however overlap
pattern = [{"POS": "PROPN", "OP": "+"}]
matcher.add("PROPER_NOUN", [pattern])
doc = nlp(text)
matches = matcher(doc)
print(len(matches))
for match in matches[:10]:
    print(match, doc[match[1]:match[2]])

print("-" * 100)

# therefore we add an extra layer to filter
# "longest" looks for the longest token 
matcher = Matcher(nlp.vocab)
pattern = [{"POS": "PROPN", "OP": "+"}]
matcher.add("PROPER_NOUN", [pattern], greedy="LONGEST")
doc = nlp(text)
matches = matcher(doc)
print(len(matches))
for match in matches[:10]:
    print(match, doc[match[1]:match[2]])
    
print("-" * 100)

# adjusted again to sort the matches
matcher = Matcher(nlp.vocab)
pattern = [{"POS": "PROPN", "OP": "+"}]
matcher.add("PROPER_NOUN", [pattern], greedy="LONGEST")
doc = nlp(text)
matches = matcher(doc)
# sorts the tuples by the start token
matches.sort(key = lambda x: x[1])
print(len(matches))
for match in matches[:10]:
    print(match, doc[match[1]:match[2]])
    
print("-" * 100)
# we can also match when proper nouns occur after a verb
# Therefore we can 
matcher = Matcher(nlp.vocab)
pattern = [{"POS": "PROPN", "OP": "+"},
           {"POS": "VERB"}]
matcher.add("PROPER_NOUN", [pattern], greedy="LONGEST")
doc = nlp(text)
matches = matcher(doc)
# sorts the tuples by the start token
matches.sort(key = lambda x: x[1])
print(len(matches))
for match in matches[:10]:
    print(match, doc[match[1]:match[2]])