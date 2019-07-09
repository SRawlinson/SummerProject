import prosodic as p
import re
#Building this into the structure all words will be put into - when a dictionary api works I'll store word type here as well. 

class Word:
    def __init__(self, stringOfWord):
        self.string = stringOfWord
        t = p.Text(stringOfWord)
        t.parse()
        bestParses = t.bestParses()
        bestParse = str(bestParses[0])
        syllsList = bestParse.replace('|', ' ').replace('.', ' ').split()
        self.sylls = []
        for syll in range(0, len(syllsList)):
            self.sylls.append(Syllable(syllsList[syll]))
    
    def giveMeEverything(self):
        everything = self.string + " = "
        for x in range(0, len(self.sylls)):
            everything += self.sylls[x].string + ": " + self.sylls[x].stressed + ". "
        return everything


class Syllable:
    def __init__(self, str):
        self.string = str.lower()
        regexMatcher = "[a-z]+"
        if(re.match(regexMatcher, str)):
            self.stressed = "unstressed"
        else:
            self.stressed = "stressed"

w1 = Word("banana")
print(w1.string)
# for x in range(0, len(w1.sylls)):
#     print(w1.sylls[x].string + ": " + w1.sylls[x].stressed)

print(w1.giveMeEverything())
