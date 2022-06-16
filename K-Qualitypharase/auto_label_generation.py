import sys
from random import shuffle
from math import sqrt
from sklearn import cluster
#this file generates the positive and negative lebels and all the positive lebel
#are called quality phrases and lebels as 1 
#knowledge base small means the given quality phrases to train the algorithm
#knowledge base large means rawData file
#feature table means final.csv file that was generated from features extraction file 
#patterns mean file which was generated from frequent patterns file
#generated_lebel means output file of this code 
if len(sys.argv) != 1:
    print ('[usage] <knowledge base small> <knowledge base large> <feature table> <patterns> <generated label>')
    sys.exit(-1)

knowledge_base = 'QualityPhrases.txt'
knowledge_base_large = 'RawData.txt'
feature_table = 'final.csv'
patterns = 'patterns.csv'
generated_label = 'generated_label.csv'

def normalizeMatrix(matrix):
    for i in xrange(dimension):
        sum = 0
        sum2 = 0
        for j in xrange(len(matrix)):
            sum += matrix[j][i]
            sum2 += matrix[j][i] * matrix[j][i]
        avg = sum / len(matrix)
        avg2 = sum2 / len(matrix)
        variance = avg2 - avg * avg
        stderror = sqrt(variance)
        for j in xrange(len(matrix)):
            matrix[j][i] = (matrix[j][i] - avg)
            if stderror > 1e-8:
                matrix[j][i] /= stderror
    return matrix

def normalize(word):
    word = word.lower()
    result = []
    for i in xrange(len(word)):
        if word[i].isalpha() or word[i] == '\'':
            result.append(word[i])
        else:
            result.append(' ')
    word = ''.join(result)
    return ' '.join(word.split())

groundtruth = {}
for line in open('QualityPhrases.txt', 'r'):
    word = line.strip()
    #word = normalize(word)
    groundtruth[word] = True
kb_phrases_all= set()
for line in open('RawData.txt', 'r'):
    word = line.strip()
    word = normalize(word)
    kb_phrases_all.add(word) 

patterns_support = list()
for line in open('patterns.csv', 'r'):
    tokens = line.split(',')
    patterns_support.append((tokens[0].strip(), int(tokens[1])))
sorted_patterns = sorted(patterns_support, key=lambda tup: -tup[1])
patterns_candidates = set([tup[0] for tup in sorted_patterns[:len(sorted_patterns) / 2]])

# loading
#loading final.csv
dimension = 0
attributes = []
forbid = ['outsideSentence', 'log_occur_feature' , 'constant', 'frequency']
matrixWiki = []
phraseWiki = []
matrixOther = []
phraseOther = []
for line in open('final.csv', 'r'):
    tokens = line.split(',')
    if tokens[0] == 'pattern':
        attributes = tokens
        #print attributes
        continue
    coordinates = []
    for i in xrange(1, len(tokens)):
        if attributes[i] in forbid:
            continue
        coordinates.append(float(tokens[i]))
    dimension = len(coordinates)
    if tokens[0] in groundtruth and tokens[0] in patterns_candidates:
        matrixWiki.append(coordinates)
        phraseWiki.append(tokens[0])
    else:
        matrixOther.append(coordinates)
        phraseOther.append(tokens[0])

# normalization
matrixWiki = normalizeMatrix(matrixWiki)
matrixOther = normalizeMatrix(matrixOther)

# k-means
kmeans = cluster.MiniBatchKMeans(n_clusters = min(200, len(matrixWiki)), max_iter = 300, batch_size = 5000)
kmeans.fit(matrixWiki)
labelsWiki = kmeans.labels_
bins = []
for i in xrange(1000):
    bins.append([])

for i in xrange(len(labelsWiki)):
    bins[labelsWiki[i]].append(phraseWiki[i])

labels = []
for bin in bins:
    shuffle(bin)
    if len(bin) > 0:
        labels.append(bin[0] + '\t1\n')
npos = len(labels)
# k-means
kmeans = cluster.MiniBatchKMeans(n_clusters = min(npos * 2, len(matrixOther)), max_iter = 300, batch_size = 5000)
kmeans.fit(matrixOther)
labelsOther = kmeans.labels_
bins = []
for i in xrange(min(npos * 2, len(matrixOther))):
    bins.append([])

for i in xrange(len(labelsOther)):
    bins[labelsOther[i]].append(phraseOther[i])

for bin in bins:
    shuffle(bin)
    if len(bin) > 0:
        for i in xrange(len(bin)):
            if bin[i] not in kb_phrases_all:
                labels.append(bin[i] + '\t0\n')
                break
#generating output file
out = open('generated_label.csv', 'w')
out.write(''.join(labels))
out.close()

print (len(labels), 'generated,', npos, 'positive')

