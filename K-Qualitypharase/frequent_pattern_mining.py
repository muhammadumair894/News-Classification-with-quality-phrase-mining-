#this file is used to find frequent patterns within the given text 
#according to the given threshold value


set = set()
def frequentPatternMining(tokens, patternOutputFilename, threshold):
    dict = {}
#this code is used to generate token of all the words used within the text file

    tokensNumber = len(tokens)
    for i in range(tokensNumber):
        token = tokens[i]
        if token == '$':
            continue
        if token in dict:
            dict[token].append(i)
        else:
            dict[token] = [i]
    print ("# of distinct tokens = ", len(dict))

    patternOutput = open(patternOutputFilename, 'w')

#length of token should be 1 to 6 words

    frequentPatterns = []
    patternLength = 1
    while (len(dict) > 0):
        if patternLength > 6:
            break
        
        patternLength += 1
        newDict = {}
        for pattern, positions in dict.items():
            occurrence = len(positions)
            if occurrence >= threshold:
                frequentPatterns.append(pattern)
#count the number of occurances of a token within the text   
                patternOutput.write(pattern + "," + str(occurrence) + "\n")
                for i in positions:
                    if i + 1 < tokensNumber:
                        if tokens[i + 1] == '$':
                            continue
                        newPattern = pattern + " " + tokens[i + 1]
                        if newPattern in newDict:
                            newDict[newPattern].append(i + 1)
                        else:
                            newDict[newPattern] = [i + 1]
        dict.clear()
        dict = newDict
    patternOutput.close()
    return frequentPatterns
