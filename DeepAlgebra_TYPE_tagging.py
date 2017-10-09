# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 11:20:23 2017

@author: Derek
"""



import gensim, os, nltk
from nltk import word_tokenize, data



class MySentences(object):
    """Stream in sentences for training one at a time to avoid memory issues. Note the 
    .replace() function."""
    
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                    yield line.replace('\r\n', ' ').split()
    

def tokenize_sentences(sentences):
    """Tokenize sentences into parts of speech. Run nltk.help.upenn_tagset()
    to see the different parts of speech in NLTK."""
    
    tagged_sentences = {}
    
    for sentence in sentences:
        tagged = nltk.pos_tag(word_tokenize(sentence))
        tagged_sentences[sentence] = tagged
        
    return tagged_sentences


def tag_TYPES(sentences, possibleTypes):
    """Beta version of tagged TYPES - all it does is returned nouns."""
    
    taggedSentences = tokenize_sentences(sentences)
    typeDict = {}
    
    for sentence in taggedSentences:
        typeDict[sentence] = {}
        taggedSentence = taggedSentences[sentence]
        
        for tagged in taggedSentence:
            word = tagged[0]
            pos = tagged[1]
            
            if pos in possibleTypes:
                typeDict[sentence][word] = {}
                typeDict[sentence][word]['POS'] = pos
    return typeDict


def build_model(folderName, trainingSentences, minCount):
    """Build a genism model froma  text file in a folder called folderName. If None, use sentences. Note
    that gensim requires sentences to be split first."""
    
    if folderName:
        sentences = MySentences(folderName) 
    else:
        sentences = trainingSentences
        
    return gensim.models.Word2Vec(sentences, min_count = minCount)


def get_similar_words_from_typeDict(model, typeDict):
    """Given tagged word TYPEs, print out most similar words from the gensim model."""
    
    for sentence in typeDict:
        for word in typeDict[sentence]:
            typeDict[sentence][word]['MostSimilar'] = {}
            try:
                for similarWord in model.most_similar(word):
                    typeDict[sentence][word]['MostSimilar'][similarWord[0]] = similarWord[1]
            except:
                pass
    return typeDict


def tokenize_from_txt(filename, tokenized):
    """Needs some work - or at least, should onyl be done after some preprocessing."""
    
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    fp = open(r'varieties.txt')
    data = fp.read()
    tokenized.append(' '.join(tokenizer.tokenize(data)))
    return tokenized



if __name__ == "__main__":
    folderName = r'TrainingDocs' #folder contianing .txt files to work on
    minCount = 5 #minimum number of instances a word needs to have to be considered in the gensim model
    possibeTypes = ['NN', 'NNS'] #parts of speech to pick out (type nltk.help.upenn_tagset() in the console window to see all possibitlies)
    toTokenize = ['Let $X$ be a noetherian scheme over an algebracally closed field $k$.',\
                  'Let $X$ and $Y$ be varieties.',\
                  'For a variety $X$, let $\mathcal{O}_X$ denote its structure sheaf.',\
                  'We say a sheaf $\mathcal{F}$ is coherent if it satisfies the condtions above.'] #some test sentences to play around with
    trainingSentences = [] #instead of training the model on docs in folderName, can use this
    
    model = build_model(folderName, trainingSentences, minCount)
    tagged = tokenize_sentences(toTokenize)
    typeDict = get_similar_words_from_typeDict(model, tag_TYPES(toTokenize, possibeTypes))