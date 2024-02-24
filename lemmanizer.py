import spacy
import timeit

#Using model to lemmatize words
np = spacy.load('en_core_web_sm')

#for removing any function words 
fs = open("functionwords.txt", "r")
#for reading files
f = open("tiny_wikipedia.txt", "r")
#for writing tokens out
unigramfile = open("unigrams.txt", "w")
#for writing words out
writetodict = open("dictionary.txt", "w")

#for storing each document
documents = []
#storing all stopwords in funcition word file
stopwords= []
#for storing tokens
worddict = {}

#for storing word key
wc = 0

#start time
start = timeit.timeit()

#O(sw)
for line in fs:
    stopwords.append(line[:-1].lower())

#O(l)
for line in f:
    documents.append(line)

#keeping track of document
i = 0

#iterate all docs
for document in documents:
    print(i)
    #load model
    doc = np(document)
    #iterate all words in one doc
    for word in doc:
        #not punctiation and stop words and not numeric
        if(str(word) not in '.,;:\'\\n\"[]-()' and str(word).isalpha() and str(word).lower() not in stopwords):
            lemmaword = word.lemma_.lower()
            if(lemmaword not in worddict):
                worddict[lemmaword] = ([wc, int(1), int(1), int(1)])
                wc+=1
            else:
                #if its a new document then add 1 to document frequency
                if(worddict[lemmaword][3] == 0):
                    worddict[lemmaword][1] += 1
                #add one if for document freq
                worddict[lemmaword][2] += 1
            
    for token in worddict:
        worddict[token][3] = 0

    i+=1

#sort alphabetically
myKeys = list(worddict.keys())
myKeys.sort()
sorted_dict = {i: worddict[i] for i in myKeys}

for word in sorted_dict:
    writetodict.write(str(word) + "\n")

#sort by global frequency
sorted_dict2 = sorted(worddict.items(), key=lambda x:x[1][2])

for sets in sorted_dict2:
    unigramfile.write(str(sets[1][0]) + " " + str(sets[0]) + " " + str(sets[1][1]) + " " + str(sets[1][2]) + "\n")

#runntime
end = timeit.timeit()
print('runntime: ' + str(end - start))


        


