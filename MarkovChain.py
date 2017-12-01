import random
from operator import itemgetter

class MarkovDictionary():
    class Word():
        def __init__(self, string, count=1, beginning_of_sentence=False):
            self.string = string
            self.count = count
            self.beginning_of_sentence = beginning_of_sentence
            
        def getWord(self):
            return self.string
        def __repr__(self):
            return "({}, {})".format(self.count, self.string)
            
    class Chain():
        def __init__(self):
            self.chain = []
            
        def insert(self, word):
            found = False
            for (i, entry) in enumerate(self.chain):
                if entry.string == word:
                    entry.count += 1
                    found = True
                    break 
                    
            if not found:
                self.chain.append(MarkovDictionary.Word(word))
                    
            self.chain.sort(key=lambda w: w.count, reverse=True)
        
        def getWordFromChain(self):
            return self.chain[0].getWord()
            
            
            
            
        def __repr__(self):
            return repr(self.chain)
        
    def __init__(self, text=None, dictionary=None):
        self.dictionary = {}
        # If text is submitted with object declaration
        if text != None:
            self.addText(text.lower())
        
    def __repr__(self):
        return repr(self.dictionary)
        
    def addText(self, newText):
        newText = list(newText.split(' '))
        for i in range(0, len(newText) - 1):
            if newText[i] not in self.dictionary:
                self.dictionary[newText[i]] = MarkovDictionary.Chain()
                
            self.dictionary[newText[i]].insert(newText[i + 1])
    
    def getRandomWord(self):
        return random.choice(list(self.dictionary.keys()))
        
    def getWordFromChain(self, word):
        return self.dictionary[word].getWordFromChain()
        

class Markov(): 
    def __init__(self, text):
        self.dictionary = MarkovDictionary(text)
        
    def printRandomWord(self):
        print(self.dictionary.getRandomWord())
    
    def addText(self, text):
        self.dictionary.addText(text)
    
    def generateText(self, n):
        word1 = self.dictionary.getRandomWord()
        generatedText = "" 
        for i in range(0, n):
            try:
                word1 = self.dictionary.getWordFromChain(word1)
                generatedText += word1 + " "
            except:
                word1 = self.dictionary.getRandomWord()
                generatedText += word1 + " "
        return generatedText
   

class TestMarkov(): 
    text = " well this is just a simple song to say what you done I told you about all those fears and away they did run you sure must be strong and you feel like an ocean being warmed by the sun i am all those men you fear "
    n = Markov(text)
    n.printRandomWord()
    print(n.generateText(15))
    


