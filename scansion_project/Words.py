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
    
    def showFirstSyllStress(self):
        return self.list[0].sylls[0].stressed

    def __str__(self):
        stringRep = ""
        for x in range(0, len(self.list)):
            z = re.match("\w", self.list[x].__str__())
            if z and (x > 0):
                stringRep += " " + self.list[x].__str__()
            else:
                stringRep += self.list[x].__str__()
        stringRep += "\n"
        return stringRep      

    def syll_str_line(self):
        outputLine = ""
        for x in range(0, len(self.list)):
            z = re.match("\w", self.list[x].__str__())
            if z and (x > 0):
                outputLine += " " + self.list[x].syll_str()
            if z and (x == 0):
                outputLine += self.list[x].syll_str()
            if z == None:
                outputLine += self.list[x].__str__()
        outputLine += ""
        return outputLine

class Word:
    def __init__(self, stringOfWord):
        self.string = stringOfWord
        t = p.Text(stringOfWord)
        t.parse()
        bestParses = t.bestParses()
        bestParse = str(bestParses[0])
        syllsList = bestParse.replace('|', ' ').replace('.', ' ').split()
        self.syllsActual = []
        self.sylls = []
        x = 0
        for syll in range(0, len(syllsList)):
            y = x
            x += len(syllsList[syll])
            self.syllsActual.append(stringOfWord[y:x])
        for syll in range(0, len(syllsList)):
            self.sylls.append(Syllable(syllsList[syll], self.syllsActual[syll]))
        self.getPattern() 
    
    def giveMeEverything(self):
        everything = self.string + " = "
        for x in range(0, len(self.sylls)):
            everything += self.sylls[x].string + ": " 
            if self.sylls[x].stressed:
                everything += "stressed"
            else:
                everything += "unstressed"
        return everything

    def __str__(self):
        return self.string

    def getPattern(self):
        output = ""
        for x in range(0, len(self.sylls)-1):
            output += self.sylls[x].pattern + " | "
        output += self.sylls[len(self.sylls)-1].pattern
        self.pattern = output

    def syll_str(self):
        output = "<span class=\"word\">"
        for syll in self.sylls:
            output += syll.colours()
        output += "<div class=\"dropdown-content\">" + self.__str__() + ": " "<br>" + self.pattern + "<br>And here is the definition...</div></span>"
        return output

class Syllable:
    def __init__(self, stringRep, stringActual):
        self.stressed = True
        self.string = stringActual
        regexMatcher = "[a-z]+"
        if(re.match(regexMatcher, stringRep)):
            self.stressed = False
        if self.stressed:
            self.pattern = "/"
        else:
            self.pattern = "x"
            

    def colours(self):
        if self.stressed:
            return "<output-font class=\"stress\">"+ self.__str__() + "</output-font>"
        else:
            return "<output-font class=\"unstressed\">" + self.__str__() + "</output-font>"
    
    def syllPattern(self):
        if self.stressed:
            return "/"
        else:
            return "x"
    
    def __str__(self):
        return self.string

# l1 = Line("Shall, I compare thee?")
# print(l1)
# print(l1.syll_str_line())
# print(l1.list[0].syll_str())
# print(l1.list[0].sylls[0].colours())