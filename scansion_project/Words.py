import prosodic as p
import re
import nltk
from nltk.corpus import wordnet
import collections
# from PyDictionary import PyDictionary
# dictionary = PyDictionary()

#This method takes the original string/text input, gathers relevant corresponding data, and splits it into lines. 
def turnTextIntoObjects(text):
    # A global idNum object is created to keep track of the words id tags. This is required over simply using an array's index due to 
    # punctuation also technically being classed as 'word' object by the html.  
    id = idNum()
    text = text.replace('_', ' ')
    textForNltk = text.replace('-', ' ')
    # nltk provides the word classes such as nouns, verbs etc. It can only do this when the whole text is processed, rather than line by line, 
    # requiring coupling between the creation of lines and this bank of word classes for the whoel text. 
    tags = nltk.word_tokenize(textForNltk)
    pos_tags = nltk.pos_tag(tags)
    #This removes possessive endings, which are considered separate by nltk. 
    for tag in pos_tags:
        x = re.match('POS', tag[1])
        if x:
            pos_tags.remove(tag)
    x = 0
    lines = []
    textSplit = text.splitlines()
    #This creates each line object, with the string representation, the relevant portion of the wordclass list, and the idNUm object. 
    for line in textSplit:
        listForLength = re.findall(r"[\w']+|[-.,!?;]", line)
        length = len(listForLength)
        lineTags = pos_tags[x: x + length]
        x+=length
        # line += "\n";
        l1 = Line(line, lineTags, id)
        lines.append(l1)

    return lines

class idNum:
    def __init__(self):
        self.number = 0

    def increaseNumber(self):
        self.number += 1

#The class for the line object. As well as creating each Word object found in its string representation, it calculates the meter of the line
#based on its words' stress variations. 
class Line:
    def __init__(self, lineString, lineTags, idNum):
        self.string = lineString
        #Separates line into words and punctuation 
        self.list = re.findall(r"[\w']+|[-.,!?;]", lineString)

        classes = 0
        # For each element in self.list,if it's a word, replace with a Word object. 
        for x in range(0, len(self.list)):
            y = self.list[x]
            z = re.match("\w+", y)
            if z:
                #I think here is where I'll need error handling for UnknownWords to appear.
                try:
                    self.list[x] = Word(self.list[x], lineTags[classes], idNum)
                    classes += 1
                    idNum.increaseNumber()
                except AttributeError as error:
                    self.list[x] = UnknownWord(self.list[x], lineTags[classes], idNum)
                    classes += 1
                    idNum.increaseNumber()
            else: 
                #Punctuation is also given the 'word' tag for the html to capture it when refreshing the page with edits, but it is not
                # given an id from idNum to prevent errors during that process. 
                self.list[x] = "<span class=\"word\">" + self.list[x] + "</span>"
        #Number of words is calculated so when the edits are made, the lines keep their formatting and line breaks. 
        self.numOfWords = 0
        for item in self.list:
            self.numOfWords += 1
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
        #Scansion does not account for lines shorter than four syllables or longer than 24. Otherwise, is calculates the size of the 'foot'
        # based on how many regular feet a line could have, and then counts which (if any) fit a known pattern such as iambic or anapestic. 
        #A helper method is used to count the number of potential matches, and another to find any recurring patterns in those. 
        if patternLength < 4 or patternLength > 24:
            self.foot = "unknown"
            self.numOfFeet = " "
        elif patternLength % 2 == 0 and (patternLength != 6 or patternLength != 12) and patternLength < 17:
            self.countFeet(patternLength, 2)
            self.matchForDoubleSylls(patternLength, pattern)
            
        elif patternLength % 3 == 0 and (patternLength != 6 or patternLength != 12):
            self.countFeet(patternLength, 3)
            self.matchForTripleSylls(patternLength, pattern)

        elif patternLength == 6 or patternLength == 12:
            self.countFeet(patternLength, 3)
            self.matchForTripleSylls(patternLength, pattern)
            if self.foot == "unknown":
                self.countFeet(patternLength, 2)
                self.matchForDoubleSylls(patternLength, pattern)

        else:
            self.foot = "unknown"
        if self.foot == "unknown":
            self.numOfFeet == " "

    def separateIntoFeet(self, array, size):
        listOfFeet = []
        for i in range(0, len(array), size):
            listOfFeet.append(array[i:i + size])
        return listOfFeet   

    def countFeet(self, numOfSylls, divider):
        numOfFeet = numOfSylls/divider
        if numOfFeet == 2:
            self.numOfFeet = "dimeter"
        elif numOfFeet == 3:
            self.numOfFeet = "trimeter"
        elif numOfFeet == 4:
            self.numOfFeet = "tetrameter"
        elif numOfFeet == 5:
            self.numOfFeet = "pentameter"
        elif numOfFeet == 6:
            self.numOfFeet = "hexameter"
        elif numOfFeet == 7:
            self.numOfFeet = "heptameter"
        elif numOfFeet == 8:
            self.numOfFeet = "octometer"
        else:
            self.numOfFeet = "unknown"
    #The two 'match' functions are what count the patterns, and determines a line fits a regular meter if over half of the 
    # feet match the same pattern. 
    def matchForDoubleSylls(self, patternLength, pattern):
        listOfFeet = self.separateIntoFeet(pattern, 2)
        iambic = 0
        spondaic = 0
        trochaic = 0
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
            self.numOfFeet = " "

    def matchForTripleSylls(self, patternLength, pattern):
        listOfFeet = self.separateIntoFeet(pattern, 3)
        anapestic = 0
        dactylic = 0
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
            self.numOfFeet = " "

    def showFirstSyllStress(self):
        return self.list[0].sylls[0].stressed

    #This is a simple toString method written for testing purposes. 
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

    #The two following methods are what is used for the functionality of the site
    def syll_str_line(self):
        # The line must include its length for the editing process to retain lines. 
        outputLine = "<span class=\"line\" id=\"" + str(self.numOfWords) + "\">"
            #Each word in the line's string representation calls a specific method designed to hold all the relevant html code. 
        for x in range(0, len(self.list)):
            z = re.match("\w", self.list[x].__str__())
            if z and (x > 0):
                outputLine += " " + self.list[x].syll_str()
            if z and (x == 0):
                outputLine += self.list[x].syll_str()
                #If the object on the line is simply punctutation, it uses the regular __str__ method. 
            if z == None:
                outputLine += self.list[x].__str__()
        outputLine += "</span>"
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

# The word class. It uses prosodic to determine its stress pattern, which informs the line's stress pattern. 
class Word:
    def __init__(self, stringOfWord, classList, idNum):
        self.string = stringOfWord
        t = p.Text(stringOfWord)
        t.parse()
        bestParses = t.bestParses()
        bestParse = str(bestParses[0])
        syllsList = bestParse.replace('|', ' ').replace('.', ' ').split()
        self.syllsActual = []
        self.sylls = []

        x = 0
        #Two syllable arrays, one for the 'actual' version from the string representation to be repeated and retain any 
        #irregular capital letters, and one for the Syllables objects used for pattern finding etc. 
        for syll in range(0, len(syllsList)):
            y = x
            x += len(syllsList[syll])
            self.syllsActual.append(stringOfWord[y:x])
        for syll in range(0, len(syllsList)):
            self.sylls.append(Syllable(syllsList[syll], self.syllsActual[syll]))
        self.getPattern() 
        self.known = True
        self.wordClass = ""
        self.getWordClass(classList)
        # self.synonyms = "Synonyms: "
        self.getSyns()#
        self.num = idNum.number
        # except AttributeError as error:
        #     self.pattern = "Scansion could not find a stress pattern for this word"
        #     self.sylls = UnknownWord(self.string, classList, idNum)
        #     self.known = False
        #     self.wordClass = "Unknown"
        #     # self.getDefinition()
        #     print(error)
        # except Exception as exception:
        #     self.pattern = "Scansion encountered an unexpected error"
        #     self.sylls = UnknownWord(self.string, classList, idNum)
        #     # self.getDefinition()
        #     self.known = False
        #     self.wordClass = "Unknown"
        #     print(exception)
    #This simply translates the word class proived by nltk into a recognisable term. 
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

    #This gathers each pattern provided by the Syllable object. 
    def getPattern(self):
        output = ""
        for x in range(0, len(self.sylls)-1):
            output += self.sylls[x].pattern + " | "
        output += self.sylls[len(self.sylls)-1].pattern
        self.pattern = output

    #The two methods below correspond to the simialr ones found in Line, and are used to provied the site with html data for the functionality. 
    def syll_str(self):
        #Words are given one class with an id using their 'num' and string representation, and one for their word class. 
        output = "<span class=\"word\" id=\""+ str(self.num) + " " +  self.__str__() + "\" onClick=\"getDefinitionOrEdit(event)\"><div class=\"" + self.wordClass + "\">"
        if self.known:
            for syll in self.sylls:
                output += syll.colours()
        else:
            output += self.sylls.colours()
        #They are also provided with the 'dropdown content'
        output += "</div><div class=\"dropdown-content\">" + self.__str__() + ": " + " <br> " + self.pattern + " <br> " + self.wordClass + " <br> "
        if self.synonyms != "none":
            output += str(self.synonyms) + " <br> "   
        #output += "<br>ID: " + str(self.num) #Included to check id-numbering was working properly. 
        output += "</div></span>"
        return output

    def syll_str_separated(self):
        output = "<span class=\"word\" id=\""+ str(self.num) + " " +  self.__str__() + "\" onClick=\"getDefinitionOrEdit(event)\"><div class=\"" + self.wordClass + "\">"
        if self.known:
            for syll in self.sylls:
                output += syll.colours() + " | "
        else:
            output += self.sylls.colours() + " | "
        output += "</div><div class=\"dropdown-content\" id=" + self.__str__() + ">" + self.__str__() + ": " "<br>" + self.pattern + "<br>" + self.wordClass + "<br></div></span>"
        return output
    #This uses nltk again to find synonyms for each word. This is used in the dropdown content and the editing functions. 
    def getSyns(self):
        synonyms = ""
        synCount = 0
        for syn in wordnet.synsets(self.string):
            for l in syn.lemmas():
                if self.string not in l.name() and synCount < 3:
                    synonyms += l.name() + " "
                    synCount += 1
        if synonyms != "":
            self.synonyms = "Synonyms: " + synonyms
        else:
            self.synonyms = "none"
        # self.synonyms += " " + synonyms

#The Syllable class simply separates the finding of each stress within words to make it easier to test and provide the html. It is provided
#the 'stringActual' from prosodic, which will be capitalised if the syllable is to be stressed. 
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
    #This is the method that corresponds to the output method for the site. Each syllable is given it's own class, again for the html functionaliy 
    def colours(self):
        if self.stressed:
            return "<output-font class=\"stress\">"+ self.__str__() + "</output-font>"
        else:
            return "<output-font class=\"unstressed\">" + self.__str__() + "</output-font>"
    
    def __str__(self):
        return self.string

#This was to prevent any problems from prosodic not knowing a word, although it has not been effectively implemented as of yet. 
class UnknownWord(Word):
    def __init__(self, stringRep, classList, idNum):
        self.string = stringRep
        self.pattern = "?"
        self.num = idNum.number
        self.known = False
        self.wordClass = "unknown"
        # self.getWordClass(classList)

    def syll_str(self):
        output = "<span class=\"word\" id=\"" + str(self.num) + " " +  self.__str__() + "\" onClick=\"getDefinitionOrEdit(event)\"><div class=\"" + self.wordClass + "\"><output-font class=\"unknown\">" + self.__str__()
        output += "</output-font></div><div class=\"dropdown-content\">" + self.__str__() + ": " + "<br>" + self.pattern + "<br>" + self.wordClass + "<br>"
        output += "</div></span>"
        return output

    def syll_str_separated(self):
        return self.syll_str()

    
    def colours(self):
        return "<output-font class=\"word\" id=\""+ str(self.num) + " " +  self.__str__() + "\" onClick=\"getDefinitionOrEdit(event)\"><div class=\"" + self.wordClass + "\">" + self.__str__() 

    
    def __str__(self):
        return self.string


# text = "If the dull substance of my flesh were thought, \n Injurious distance should not stop my way; \n For then despite of space I would be brought, \n From limits far remote where thou dost stay. \n No matter then although my foot did stand \n Upon the farthest earth removed from thee; \n For nimble thought can jump both sea and land \n As soon as think the place where he would be. \n But ah! thought kills me that I am not thought, \n To leap large lengths of miles when thou art gone, \n But that so much of earth and water wrought \n I must attend time's leisure with my moan, \n Receiving nought by elements so slow \n But heavy tears, badges of either's woe. \n "
# lines = []
# textSplit =text.splitlines()
# for line in textSplit:
#     l1 = Line(line)
#     lines.append(l1)
# listForTags = re.findall(r"[\w']+|[-.,!?;]", text)
# #Tokenizes using nltk
# tags = nltk.word_tokenize(text)
# pos_tags = nltk.pos_tag(tags)
# # print(pos_tags)
# for tag in pos_tags:
#     x = re.match('POS', tag[1])
#     if x:
#         pos_tags.remove(tag)
# # # print(pos_tags)
# x = 0
# for line in textSplit:
#     listForLength = re.findall(r"[\w']+|[-.,!?;]", line)
#     length = len(listForLength)
#     lineTags = pos_tags[x: x + length]
#     x += length

# t = turnTextIntoObjects("dog")
# print(t[0].list[0].synonyms)


# l1 = Line("Shall, I compare thee?")
# print(l1.syll_str_line())
# print(l1.list[0].syll_str())
# print(l1.list[0].sylls[0].colours())
# w1 = Word("Shallow")
# print(w1)
# l1 = Line("I whirled out wings that spell")
# print(l1.linePattern)
# print(l1.foot + " " + l1.numOfFeet)

# t = turnTextIntoObjects("Shall I compare thee to a summer's day?")