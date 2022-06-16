import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import spacy
import re
from spacy import displacy
from collections import Counter
nlp = spacy.load("en_core_web_sm")

#Extracting named entity from an article
print("\n .............................Article Named Entity........................ \n")

fp = open('Algor.txt',encoding='utf-8')
sampletest= fp.readlines()
print("Length: \n",len(sampletest))

article = nlp(str(sampletest))
print("Article: \n",article)
print("Length of an articles: \n",len(article.ents))
#
labels = [x.label_ for x in article.ents]
print("Count the label entities of an articles: \n",Counter(labels))
# #three most frequent tokens.
items = [x.text for x in article.ents]
print("three most common Entities: \n",Counter(items).most_common(3))
#
# #randomly select one sentence
sentences = [x for x in article.sents]
print("Random sentence: \n",sentences[10])
#
# displacy.render(nlp(str(sentences[20])), jupyter=True, style='ent')#generte raw markup
# displacy.render(nlp(str(sentences[20])), style='dep', jupyter = True, options = {'distance': 120})
#
# #verbatise , extract part-of-speech and lemmatize this sentence.
g = [(x.orth_, x.pos_, x.lemma_) for x in [y for y in nlp(str(sentences[10])) if not y.is_stop and y.pos_ != 'PUNCT']]
print("After preprocessed data POS: \n",g)
d=dict([(str(x), x.label) for x in nlp(str(sentences[10])).ents])
print("Dictionary: \n",d)
#Named entity extraction are correct except “F.B.I”.
print("All correct one Result: \n",[(x, x.ent_iob_, x.ent_type_) for x in sentences[10]])



print("\n .............................SPACY........................ \n")

doc = nlp(str(sampletest))
print("Doc Entities of label and test: \n",[(X.text, X.label_) for X in doc.ents])

#European is NORP (nationalities or religious or political groups), Google is an organization, $5.1 billion is monetary value
#  and Wednesday is a date object.
#token
print("Tokenized: \n",[(X, X.ent_iob_, X.ent_type_) for X in doc])
#"B" means the token begins an entity, "I" means it is inside an entity,
# "O" means it is outside an entity, and "" means no entity tag is set.


#I took a sentence from The New York Times, “European authorities fined Google a record $5.1 billion on Wednesday
# for abusing its power in the mobile phone market and ordered the company to alter its practices.”
print("\n .............................NLTK........................ \n")


ex = str(sampletest)
#apply word tokenization and part-of-speech tagging to the sentence.
from string import punctuation
def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

sent = preprocess(ex)
print("Preprocess tokenize sentence:\n ",sent) #got list of tuples containing the individual words in the
# sentence and their associated part-of-speech.
#implement noun phrase chunking to identify named entities using a regular expression
#  consisting of rules that indicate how sentences should be chunked.
"""
Our chunk pattern consists of one rule,
that a noun phrase, NP, should be formed whenever the chunker finds an optional determiner, DT,
 followed by any number of adjectives, JJ, and then a noun, NN.
"""

pattern = 'NP: {<DT>?<JJ>*<NN>}'
#Chunking
#Using pattern, we create a chunk parser and test it on our sentence
cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
print("Chunking of Sentence: \n",list(cs))

#the output can be read as a tree or a hierarchy with S as the first level, denoting sentence. we can also display it graphically.
#cs.draw()
#IOB tags have become the standard way to represent chunk structures in files, and we will also be using this format.
#inside,outside,begining

from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint
iob_tagged = tree2conlltags(cs)
print("IOB Tageed per line of token: \n ",iob_tagged) #there is one token per line, each with its part-of-speech tag
# and its named entity tag.

#With the function nltk.ne_chunk(), which recognize named entities using a classifier,
# the classifier adds category labels such as PERSON, ORGANIZATION, and GPE.
ne_tree = nltk.ne_chunk(pos_tag(word_tokenize(ex)))
print("Recognized Name ENtities Classifier: \n",ne_tree)