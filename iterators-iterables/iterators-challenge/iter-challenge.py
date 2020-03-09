class Sentence:

    wordsIter = 0
    
    # initializing words list by splitting the words
    def __init__(self, words):
        self.words = words.split()
    
    def __iter__(self):
        return self

    def __next__(self):
        
        if self.wordsIter == len(self.words):
            raise StopIteration
        
        currentWord = self.words[self.wordsIter]
        self.wordsIter += 1
        return currentWord



rapGod = Sentence('Snap back to reality')

print(next(rapGod))

for word in rapGod:
    print(word)

# now, creating a function

def gen_function(words):

    wordsList = words.split()

    for word in wordsList:
        yield word


for word in gen_function('There goes gravity'):
    print(word)
