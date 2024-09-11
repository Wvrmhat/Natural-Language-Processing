#!/usr/bin/env python3

import spacy
import pandas as pd

data = pd.read_csv("data/stocks.tsv", sep="\t")
data2 = pd.read_csv("data/indexes.tsv", sep="\t")
data3 = pd.read_csv("data/stock_exchanges.tsv", sep="\t")

symbols = data.Symbol.to_list()
companies = data.CompanyName.to_list()
print(symbols[:10])

stops = ["two"]

nlp = spacy.blank("en")
ruler = nlp.add_pipe("entity_ruler")
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
patterns = []

# converting indexes to list
indexes = data2.IndexName.to_list()
index_symbols = data2.IndexSymbol.to_list()

exchanges = data3.ISOMIC.to_list()+ data3["Google Prefix"].to_list() + data3.Description.to_list()
print(exchanges[:10])

for symbol in symbols:
    patterns.append({"label": "STOCK", 
                     "pattern": symbol})
    for l in letters:
        patterns.append({"label": "STOCK",
                        "pattern": symbol+f".{l}"})     # any occurence of l
    
for company in companies:
    if company not in stops:
        patterns.append({"label": "COMPANY",
                        "pattern": company})
        
for index in indexes:
    patterns.append({"label": "INDEX", 
                     "pattern": index})
    words = index.split()
    patterns.append({"label": "INDEX", 
                     "pattern": " ".join(words[:2])})   # join words up until second index 

for index in index_symbols:
    patterns.append({"label": "INDEX", 
                     "pattern": index})
    
for e in exchanges:
    patterns.append({"label": "STOCK_EXCHANGE", "pattern": e})            
        
with open("data/reuters.txt") as f:
    text = f.read()

print("-" * 100)

ruler.add_patterns(patterns)
# extracting entities    
doc = nlp(text)
for ent in doc.ents:
    print(ent.text, ent.label_)
    


