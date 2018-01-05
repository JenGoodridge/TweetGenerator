import config
from Fetch import *
from MarkovChain import *

def formatTweet(text):
    text = list(text.split(' '))
    if text[0].isalpha(): 
        text[0] = text[0].capitalize()
    text = ' '.join(text)
    text = text[0: len(text)-1]
    text += '.'
    return text
    
if __name__ == "__main__":
    f = Fetch()
    markov = Markov(f.returnTweets())
    print(formatTweet(markov.generateText(20)))
    
