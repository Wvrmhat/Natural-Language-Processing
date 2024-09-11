#!/usr/bin/env python3

import spacy

nlp = spacy.load("en_core_web_sm")

# containers are objects that contain large amounts of data
# tokens are words and punctuation marks
# spans can be a token, or a sequence of multiple tokens

with open ("data/wiki_us.txt", "r") as F:
    text = F.read()
    
# document object    
doc = nlp(text)
print(len(text))
print(len(doc))

print("-" * 100)

# Sentence boundy detection (SBD)
# sent gives you each individual sentence
for sent in doc.sents:
    print(sent)

print("-" * 100)
# gets the very fist sentence
sentence1 = list(doc.sents)[0]
print(sentence1)

# token attributes

token2 = sentence1[2]
print(token2)

print(token2.left_edge)
print(token2.right_edge)
# type of entity
print(token2.ent_type_)
# I means it is inside an entity
print(token2.ent_iob_)
print(token2.lemma_)

# lemma is used when working with verbs
# the original of sentence1 is "known", but lemma form is the verb "know"
sentence1[12].lemma_
print(sentence1[12])

print("-" * 100)

# for morphological analysis, shows output of word
print(token2.morph)
print(sentence1[12].morph)

#part of speech
print(token2.pos_)

print(token2.dep_)
print(token2.lang_)

print("-" * 100)

text = "Leo sharpens his sword as he readies himself for the war to come."
doc2 = nlp(text)
print(doc2)

for token in doc2:
    print(token.text, token.pos_, token.dep_)

print("-" * 100)

# Named entity recognition

for ent in doc.ents:
    print(ent.text, ent.label_)
    
print("-" * 100)




    


