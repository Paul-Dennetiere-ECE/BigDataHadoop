import re


def map(data): #Mapper : Will create an array of word from a text
    regex = re.compile("[A-z]+")
    words = regex.findall(data)
    result = []
    for word in words:
        result.append([word,1])
    return result # Return that array

def sortAndShuffle(data):
    result = {}
    for mapperResult in data:
        for word in mapperResult:
            if word[0] not in result.keys():
                result[word[0]] = [word[1]]
            else:
                result[word[0]].append(word[1])
    return result


def reduce(data):# Reducer : Will count words in this example
    result = {} # We use a dictionnary to structurize the result : keys = words, values = occurence
    for word in data: # completing the dictionnary
        if not word in result.keys():
            result[word] = len(data[word])
        else :
            result[word] += 1
    return result # Return the dictionnary


dataFile = open("text",'r')# Open a file
toSort = []
for line in dataFile:
    tmp = map (line)
    toSort.append(tmp)
toReduce = sortAndShuffle(toSort)
final = reduce(toReduce)
print final
