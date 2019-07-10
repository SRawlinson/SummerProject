import prosodic as p
import re
#Building this into the structure all words will be put into - when a dictionary api works I'll store word type here as well. 

class Line:
    def __init__(self, lineString):
        self.string = lineString
        self.list = re.findall(r"[\w']+|[.,!?;]", lineString)
        for x in range(0, len(self.list)):
            y = self.list[x]
            z = re.match("\w+", y)
            if z:
                self.list[x] = Word(self.list[x])

    def __str__(self):
        stringRep = ""
        for x in range(0, len(self.list)):
            z = re.match("\w", self.list[x].__str__())
            if z and (x > 0):
                stringRep += " " + self.list[x].__str__()
            else:
                stringRep += self.list[x].__str__()
        return stringRep

    # def printTheList(self):
    #     stringRep = ""
    #     for x in range(0, len(self.list)):
    #         z = re.match("\w", self.list[x].__str__())
    #         if z and (x > 0):
    #             stringRep += " " + self.list[x].__str__()
    #         else:
    #             stringRep += self.list[x].__str__()
    #     return stringRep



        


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
            everything += self.sylls[x].string + self.sylls[x].stressed #Notes from meeting 10/7 --> + ": <span style=\"state: hidden;\">" + self.sylls[x].stressed + "</span>. "
        return everything

    def __str__(self):
        return self.string

class Syllable:
    def __init__(self, str):
        self.string = str.lower()
        regexMatcher = "[a-z]+"
        if(re.match(regexMatcher, str)):
            self.stressed = "unstressed"
        else:
            self.stressed = "stressed"

# l1 = Line("Shall I, compare '           thee")
# print(l1)
# print(len(l1.list))
# print(l1.list[3])
# print(l1.list[3].sylls[0].stressed)




# w1 = Word("banana")
# print(w1.string)
# for x in range(0, len(w1.sylls)):
#     print(w1.sylls[x].string + ": " + w1.sylls[x].stressed)

# print(w1.giveMeEverything())
