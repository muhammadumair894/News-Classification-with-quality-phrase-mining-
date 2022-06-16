#this is the main file and we import frequent patterns mining file into this file
from frequent_pattern_mining import *
import re
import sys

def main(argv):
    ENDINGS = ".!?,;:\"[]"
    
#giving te threshold value 10 and input the text file name as RawData
    threshold = 10
    rawTextInput = 'DBLP.5K.txt'
#this file generate the output file name as patterns.csv
    patternOutputFilename = 'patterns.csv'
    argc = len(argv)
    for i in range(argc):
        if argv[i] == "-raw" and i + 1 < argc:
            rawTextInput = argv[i + 1]
        elif argv[i] == "-thres" and i + 1 < argc:
            threshold = int(argv[i + 1])
        elif argv[i] == "-o" and i + 1 < argc:
            patternOutputFilename = argv[i + 1]
    
#read the input file name as RawData
    raw = open(rawTextInput, 'r', encoding='utf-8');
    tokens = []
    for line in raw:
        inside = 0
        chars = []
        for ch in line:
            if ch == '(':
                inside += 1
            elif ch == ')':
                inside -= 1
            elif inside == 0:
                if ch.isalpha():
                    chars.append(ch.lower())
                elif ch == '\'':
                    chars.append(ch)
                else:
                    if len(chars) > 0:
                        tokens.append(''.join(chars))
                    chars = []
            if ch in ENDINGS:
                tokens.append('$')
        if len(chars) > 0:
            tokens.append(''.join(chars))
            chars = []
#generate all the words within the text 
    print ("# tokens = ", len(tokens))

    frequentPatterns = frequentPatternMining(tokens, patternOutputFilename, threshold)
#generate all the frequent patterns and their frequency

    print ("# of frequent pattern = ", len(frequentPatterns))
    
if __name__ == "__main__":
    main(sys.argv[1 : ])
