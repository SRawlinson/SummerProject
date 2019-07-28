import prosodic as p
import re
import nltk
from nltk.corpus import wordnet
# from PyDictionary import PyDictionary
# dictionary = PyDictionary()

# print(dictionary.meaning("indentation"))
class Line:
    def __init__(self, lineString):
        self.string = lineString
        #Separate line into words and punctuation 
        self.list = re.findall(r"[\w']+|[-.,!?;]", lineString)
        #Tokenizes using nltk
        text = nltk.word_tokenize(str(self.list))
        pos_tags = nltk.pos_tag(text)
        classes = 0
        # For each element in self.list,if it's a word, replace with a Word object. 
        for x in range(0, len(self.list)):
            y = self.list[x]
            z = re.match("\w+", y)
            if z:
                self.list[x] = Word(self.list[x], pos_tags[classes])
                classes += 1
        #Identify the overall pattern of stresses in the line. 
        self.linePattern = ""
        self.getPattern()
        self.identifyPattern()
    #getPattern is more for the display purposes, builds a html string similar to the below methods. 
    def getPattern(self):
        linePattern = "<pre>"
        for x in range(0, len(self.list)):
            z = re.match("\w+", self.list[x].__str__())
            if z:
                linePattern += self.list[x].pattern + "\t"
        self.linePattern = linePattern + "</pre>"

#identifyPattern also gathers a string representation of the patterns of each word and then 
#evaluates if it is a close enough match to a known metric pattern. 
    def identifyPattern(self):
        linePattern = ""
        for x in range(0, len(self.list)):
            z = re.match("\w+", self.list[x].__str__())
            if z:
                if self.list[x].pattern == None:
                    linePattern += '?'
                else:
                    linePattern += self.list[x].pattern
                    # print(self.list[x].__str__() + ": " + self.list[x].pattern)
        pattern = linePattern.replace('|', ' ').replace(' ', '')
        pattern = pattern.replace('/', 's')
        patternLength = len(pattern)
        self.foot = ""
        self.numOfFeet = ""
        if patternLength < 4 or patternLength > 24:
            self.foot = "unknown"
            self.numOfFeet = "unknown"
        elif patternLength % 2 == 0 and (patternLength != 6 or patternLength != 12) and patternLength < 17:
            iambic = 0
            spondaic = 0
            trochaic = 0
            if patternLength == 4:
                self.numOfFeet = "dimeter"
            elif patternLength == 8:
                self.numOfFeet = "tetrameter"
            elif patternLength == 10:
                self.numOfFeet = "pentameter"
            elif patternLength == 14:
                self.numOfFeet = "heptamter"
            elif patternLength == 16:
                self.numOfFeet = "octometer"
            else:
                self.numOfFeet = "unknown"
            
            listOfFeet = self.separateIntoFeet(pattern, 2)
            for foot in listOfFeet:
                z = re.match("xs", foot)
                if z:
                    iambic = iambic + 1
                y = re.match("sx", foot)
                if y:
                    trochaic = trochaic + 1
                x = re.match("ss", foot)
                if x:
                    spondaic = spondaic + 1
            if (iambic >= spondaic) and (iambic >= trochaic) and (iambic >= (patternLength/4)):
                self.foot = "iambic"
            elif (trochaic >= iambic) and (trochaic >= spondaic) and (trochaic >= (patternLength/4)):
                self.foot = "trochaic"
            elif (spondaic >= iambic) and (spondaic >= trochaic) and (spondaic >= (patternLength/4)):
                self.foot = "spondaic"
            else:
                self.foot = "unknown"
                self.numOfFeet = "unknown"
        elif patternLength % 3 == 0 and (patternLength != 6 or patternLength != 12):
            dactylic = 0
            anapestic = 0
            if patternLength == 9:
                self.numOfFeet = "trimeter"
            elif patternLength == 15:
                self.numOfFeet = "pentameter"
            elif patternLength == 18:
                self.numOfFeet = "hexameter"
            elif patternLength == 21:
                self.numOfFeet = "heptameter"
            elif patternLength == 24:
                self.numOfFeet = "octometer"
            listOfFeet = self.separateIntoFeet(pattern, 3)
            for foot in listOfFeet:
                z = re.match("xxs", foot)
                if z:
                    anapestic = anapestic + 1
                y = re.match("sxx", foot)
                if y:
                    dactylic = dactylic + 1
            if (anapestic >= dactylic and anapestic >= ((patternLength/3)/2)):
                self.foot = "anapestic"
            elif (dactylic >= anapestic and dactylic >= ((patternLength/3)/2)):
                self.foot = "dactylic"
            else:
                self.foot = "unknown"
                self.numOfFeet = "unknown"
        elif patternLength == 6:
            listOfFeet = self.separateIntoFeet(pattern, 3)
            for foot in listOfFeet:
                z = re.match("xxs", foot)
                if z:
                    anapestic = anapestic + 1
                y = re.match("sxx", foot)
                if y:
                    dactylic = dactylic + 1
            if anapestic == 2:
                self.foot = "anapestic"
                self.numOfFeet = "dimeter"
            elif dactylic == 2:
                self.foot = "dactylic"
                self.numOfFeet = "dimeter"
            else:
                listOfFeet = self.separateIntoFeet(pattern, 2)
                for foot in listOfFeet:
                    z = re.match("xs", foot)
                    if z:
                        iambic = iambic + 1
                    y = re.match("sx", foot)
                    if y:
                        trochaic = trochaic + 1
                    x = re.match("ss", foot)
                    if x:
                        spondaic = spondaic + 1
                if (iambic >= 2):
                    self.foot = "iambic"
                    self.numOfFeet = "trimeter"
                elif (trochaic >= 2):
                    self.foot = "trochaic"
                    self.numOfFeet = "trimeter"
                elif (spondaic >= 2):
                    self.foot = "spondaic"
                    self.numOfFeet = "trimeter"
                else:
                    self.foot = "unknown"
                    self.foot = "unknown"
        elif patternLength == 12:
            listOfFeet = self.separateIntoFeet(pattern, 3)
            for foot in listOfFeet:
                z = re.match("xxs", foot)
                if z:
                    anapestic = anapestic + 1
                y = re.match("sxx", foot)
                if y:
                    dactylic = dactylic + 1
            if anapestic >= 2:
                self.foot = "anapestic"
                self.numOfFeet = "dimeter"
            elif dactylic >= 2:
                self.foot = "dactylic"
                self.numOfFeet = "dimeter"
            else:
                listOfFeet = self.separateIntoFeet(pattern, 2)
                for foot in listOfFeet:
                    z = re.match("xs", foot)
                    if z:
                        iambic = iambic + 1
                    y = re.match("sx", foot)
                    if y:
                        trochaic = trochaic + 1
                    x = re.match("ss", foot)
                    if x:
                        spondaic = spondaic + 1
                if (iambic >= 3):
                    self.foot = "iambic"
                    self.numOfFeet = "trimeter"
                elif (trochaic >= 3):
                    self.foot = "trochaic"
                    self.numOfFeet = "trimeter"
                elif (spondaic >= 3):
                    self.foot = "spondaic"
                    self.numOfFeet = "trimeter"
                else:
                    self.foot = "unknown"
                    self.foot = "unknown"
        else:
            self.foot = "unknown"
            self.numOfFeet = "unknown"



        
                


    def separateIntoFeet(self, array, size):
        listOfFeet = []
        for i in range(0, len(array), size):
            listOfFeet.append(array[i:i + size])
        return listOfFeet            

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

    def syll_str_sep_line(self):
        outputLine = "| "
        for x in range(0, len(self.list)):
            z = re.match("\w", self.list[x].__str__())
            if z and (x > 0):
                outputLine += " " + self.list[x].syll_str_separated()
            if z and (x == 0):
                outputLine += self.list[x].syll_str_separated()
            if z == None:
                outputLine += self.list[x].__str__()
        outputLine += ""
        return outputLine

class Word:
    def __init__(self, stringOfWord, classList):
        self.string = stringOfWord
        try:
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
            # self.getDefinition()
            self.known = True
            self.wordClass = ""
            self.getWordClass(classList)
        except AttributeError as error:
            self.pattern = "Scansion could not find a stress pattern for this word"
            self.sylls = UnknownWord(self.string)
            self.known = False
            self.wordClass = "Unknown"
            # self.getDefinition()
            print(error)
        except Exception as exception:
            self.pattern = "Scansion encountered an unexpected error"
            self.sylls = UnknownWord(self.string)
            # self.getDefinition()
            self.known = False
            self.wordClass = "Unknown"
            print(exception)



    # def getDefinition(self):
    #     definition_dict = dictionary.meaning(self.string)
    #     if definition_dict == None:
    #         self.definition = "Scansion could not find a dictionary definition for " + self.string
    #     else:
    #         definition_str = ""
    #         for x in definition_dict:
    #             definition_str += str(x) + ": " + str(definition_dict[x]) + "<br>"
    #         self.definition = definition_str

    def getWordClass(self, classList):
        if classList[1] == "JJ" or classList[1] == "JJR" or classList[1] == "JJS":
            self.wordClass = "Adjective"
        elif classList[1] == "RB" or classList[1] == "RBR" or classList[1] == "RBS":
            self.wordClass = "Adverb"
        elif classList[1] == "NN" or classList[1] == "NNP" or classList[1] == "NNPS":
            self.wordClass = "Noun"
        elif classList[1] == "VB" or classList[1] == "VBD" or classList[1] == "VBG" or classList[1] == "VBN" or classList[1] == "VBP" or classList[1] == "VBZ":
            self.wordClass = "Verb"
        elif classList[1] == "CC":
            self.wordClass = "Coordinating conjunction"
        elif classList[1] == "CD":
            self.wordClass = "Cardinal number"
        elif classList[1] == "DT":
            self.wordClass = "Determiner"
        elif classList[1] == "EX":
            self.wordClass = "Existential 'there'"
        elif classList[1] == "FW":
            self.wordClass = "Foreign Word"
        elif classList[1] == "IN":
            self.wordClass = "Preposition or suburdinating conjunction"
        elif classList[1] == "LS":
            self.wordClass = "List item marker"
        elif classList[1] == "MD":
            self.wordClass = "Modal"
        elif classList[1] == "PDT":
            self.wordClass = "Predeterminer"
        elif classList[1] == "POS":
            self.wordClass = "Possessive ending"
        elif classList[1] == "PRP":
            self.wordClass = "Personal Pronoun"
        elif classList[1] == "PRP$":
            self.wordClass = "Possessive Pronoun"
        elif classList[1] == "RP":
            self.wordClass = "Particle"
        elif classList[1] == "SYM":
            self.wordClass = "Symbol"
        elif classList[1] == "TO":
            self.wordClass = "'to'"
        elif classList[1] == "UH":
            self.wordClass = "Interjection"
        elif classList[1] == "WDT":
            self.wordClass = "Wh-determiner"
        elif classList[1] == "WP":
            self.wordClass = "Wh-pronoun"
        elif classList[1] == "WP$":
            self.wordClass = "Possessive wh-pronoun"
        elif classList[1] =="WRB":
            self.wordClass = "wh-adverb"
        else:
            self.wordClass = "Unknown"

    def __str__(self):
        return self.string

    def getPattern(self):
        output = ""
        for x in range(0, len(self.sylls)-1):
            output += self.sylls[x].pattern + " | "
        output += self.sylls[len(self.sylls)-1].pattern
        self.pattern = output

    def syll_str(self):
        output = "<span class=\"word\" onClick=\"getDefinition(event)\"><div class=\"" + self.wordClass + "\" id=\""+ self.__str__() + "\">"
        if self.known:
            for syll in self.sylls:
                output += syll.colours()
        else:
            output += self.sylls.colours()
        output += "</div><div class=\"dropdown-content\">" + self.__str__() + ": " "<br>" + self.pattern + "<br>" + self.wordClass + "<br></div></span>"
        return output

    def syll_str_separated(self):
        output = "<span class=\"word\">"
        if self.known:
            for syll in self.sylls:
                output += syll.colours() + " | "
        else:
            output += self.sylls.colours() + " | "
        output += "<div class=\"dropdown-content\">" + self.__str__() + ": " "<br>" + self.pattern + "<br>" + self.wordClass + "<br></div></span>"
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
    
    def __str__(self):
        return self.string

class UnknownWord:
    def __init__(self, stringRep):
        self.string = stringRep
        self.pattern = "?"

    def colours(self):
        return "<output-font class=\"unknown\">" + self.__str__() + "</output-font>"
    
    def __str__(self):
        return self.string


# l1 = Line("Shall, I compare thee?")
# print(l1.syll_str_line())
# print(l1.list[0].syll_str())
# print(l1.list[0].sylls[0].colours())
# w1 = Word("Shallow")
# print(w1)
