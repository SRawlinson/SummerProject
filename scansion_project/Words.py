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
        return stringRep      

    def syll_str_line(self):
        outputLine = """<html>"""
        for x in range(0, len(self.list)):
            z = re.match("\w", self.list[x].__str__())
            if z and (x > 0):
                outputLine += " " + self.list[x].syll_str()
            if z and (x == 0):
                outputLine += self.list[x].syll_str()
            # else:
            #     outputLine += self.list[x].__str__()
        outputLine += """</html>"""
        return outputLine

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
            everything += self.sylls[x].string + ": " #Notes from meeting 10/7 --> + ": <span style=\"state: hidden;\">" + self.sylls[x].stressed + "</span>. "
            if self.sylls[x].stressed:
                everything += "stressed"
            else:
                everything += "unstressed"
        return everything

    def __str__(self):
        return self.string

    def syll_str(self):
        output = ""
        for syll in self.sylls:
            output += syll.colours()
        return output

class Syllable:
    def __init__(self, str):
        self.stressed = True
        self.string = str.lower()
        regexMatcher = "[a-z]+"
        if(re.match(regexMatcher, str)):
            self.stressed = False
            

    def colours(self):
        if self.stressed:
            return "<p class=\"stress\">"+ self.__str__() + "</p>"
        else:
            return "<p class=\"unstressed\">" + self.__str__() + "</p>"
    
    def __str__(self):
        return self.string

# l1 = Line("Shall I compare thee")
# print(l1)
# print(l1.syll_str_line())
# print(l1.list[0].syll_str())
# print(l1.list[0].sylls[0].colours())