#!/usr/bin/env python3

import spacy
import numpy as np

# Word vectors are numberical representations of words
# helps computers understand what words actually are

nlp = spacy.load("en_core_web_md")

with open("data/wiki_us.txt") as F:
    text = F.read()
    
doc = nlp(text)
sentence1 = list(doc.sents)[0]
print(sentence1)
print("-"*100)

your_word = "country"

ms = nlp.vocab.vectors.most_similar(
    np.asarray([nlp.vocab.vectors[nlp.vocab.strings[your_word]]]), n=10)

words = [nlp.vocab.strings[w] for w in ms[0][0]]
distances = ms[2]
print(words)
print("-"*100)
# can calculate document similarity in spacey

doc1 = nlp("I like salty fries and hamburgers")
doc2 = nlp("Fast food tastes very good.")

print (doc1, "<->", doc2, doc1.similarity(doc2))

doc3 = nlp("The Empire State Building is in New York.")
print (doc1, "<->", doc3, doc1.similarity(doc3))

doc4 = nlp("I enjoy oranges.")
doc5 = nlp("I enjoy apples.")
print (doc4, "<->", doc5, doc4.similarity(doc5))

french_fries = doc1[2:4]
burgers = doc1[5]

print(french_fries, "<->", burgers, french_fries.similarity(burgers))

print("-" * 100)

#analysing pipeline

print(nlp.analyze_pipes())

