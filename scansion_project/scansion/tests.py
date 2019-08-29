from django.test import TestCase
import unittest
import Words
from scansion import views
import re
import collections

class TestInput(TestCase):
    # Full text of Shakespeare's sonnet 44
    # text = "If the dull substance of my flesh were thought, \n Injurious distance should not stop my way; \n For then despite of space I would be brought, \n From limits far remote where thou dost stay. \n No matter then although my foot did stand \n Upon the farthest earth removed from thee; \n For nimble thought can jump both sea and land \n As soon as think the place where he would be. \n But ah! thought kills me that I am not thought, \n To leap large lengths of miles when thou art gone, \n But that so much of earth and water wrought \n I must attend time's leisure with my moan, \n Receiving nought by elements so slow \n But heavy tears, badges of either's woe. \n "
    # lines = Words.turnTextIntoObjects(text)
    # # print(lines[0])
    # #line == the first line of above
    # line = lines[0].syll_str_line()
    # # print(line)
    # #firstWord == the first word's string output for the site
    # firstWord = lines[0].list[1].syll_str()
    # print(firstWord)
    # # firstSyll == the first syllable of the first word - in this case it inclludes the whole word of 'If'
    # firstSyll = lines[0].list[0].sylls[0].colours()
    # # print(firstSyll)
    def test_turnTextIntoObjects_works_with_unproblematic_inputs(self):
        expectedFirstWordOutput = "<span class=\"word\" id=\"0 If\" onClick=\"getDefinitionOrEdit(event)\"><div class=\"Preposition or suburdinating conjunction\"><output-font class=\"unstressed\">If</output-font></div><div class=\"dropdown-content\">If:  <br> x <br> Preposition or suburdinating conjunction <br> </div></span>"
        text = "If the dull substance of my flesh were thought,"
        lines = Words.turnTextIntoObjects(text)
        # line = lines[0].syll_str_line()
        firstWord = lines[0].list[0].syll_str()
        self.assertEqual(firstWord, expectedFirstWordOutput)
    
    def test_unproblematic_but_word_number_two(self):
        expectedSecondWordOutput = "<span class=\"word\" id=\"1 the\" onClick=\"getDefinitionOrEdit(event)\"><div class=\"Determiner\"><output-font class=\"unstressed\">the</output-font></div><div class=\"dropdown-content\">the:  <br> x <br> Determiner <br> </div></span>"
        text = "If the dull substance of my flesh were thought,"
        lines = Words.turnTextIntoObjects(text)
        secondWord = lines[0].list[1].syll_str()
        self.assertEqual(secondWord, expectedSecondWordOutput)

    def test_inputs_with_all_capitals(self):
        expectedFirstWordOutput = "<span class=\"word\" id=\"0 IF\" onClick=\"getDefinitionOrEdit(event)\"><div class=\"Preposition or suburdinating conjunction\"><output-font class=\"unstressed\">IF</output-font></div><div class=\"dropdown-content\">IF:  <br> x <br> Preposition or suburdinating conjunction <br> </div></span>"
        text = "IF THE DULL SUBSTANCE OF MY FLESH WERE THOUGHT,"
        lines = Words.turnTextIntoObjects(text)
        firstWord = lines[0].list[0].syll_str()
        self.assertEqual(firstWord, expectedFirstWordOutput)
    
    def test_input_with_underscores(self):
        expectedFirstWordOutput = "<span class=\"word\" id=\"0 If\" onClick=\"getDefinitionOrEdit(event)\"><div class=\"Preposition or suburdinating conjunction\"><output-font class=\"unstressed\">If</output-font></div><div class=\"dropdown-content\">If:  <br> x <br> Preposition or suburdinating conjunction <br> </div></span>"
        text = "If_the_dull_substance_of_my_flesh_were_thought,"
        lines = Words.turnTextIntoObjects(text)
        firstWord = lines[0].list[0].syll_str()
        self.assertEqual(firstWord, expectedFirstWordOutput)

    def test_second_word_with_underscores(self):
        expectedSecondWordOutput = "<span class=\"word\" id=\"1 the\" onClick=\"getDefinitionOrEdit(event)\"><div class=\"Determiner\"><output-font class=\"unstressed\">the</output-font></div><div class=\"dropdown-content\">the:  <br> x <br> Determiner <br> </div></span>"
        text = "If_the_dull_substance_of_my_flesh_were_thought,"
        lines = Words.turnTextIntoObjects(text)
        secondWord = lines[0].list[1].syll_str()
        self.assertEqual(secondWord, expectedSecondWordOutput)
    
    #Failing as of 10/08
    def test_input_with_dashes(self):
        expectedFirstWordOutput = "<span class=\"word\" id=\"0 If\" onClick=\"getDefinitionOrEdit(event)\"><div class=\"Preposition or suburdinating conjunction\"><output-font class=\"unstressed\">If</output-font></div><div class=\"dropdown-content\">If:  <br> x <br> Preposition or suburdinating conjunction <br> </div></span>"
        text = "If-the-dull-substance-of-my-flesh-were-thought,"
        lines = Words.turnTextIntoObjects(text)
        firstWord = lines[0].list[0].syll_str()
        self.assertEqual(firstWord, expectedFirstWordOutput)

    def test_input_with_mix_of_dashes_and_spaces(self):
        expectedFirstWordOutput = "<span class=\"word\" id=\"0 If\" onClick=\"getDefinitionOrEdit(event)\"><div class=\"Preposition or suburdinating conjunction\"><output-font class=\"unstressed\">If</output-font></div><div class=\"dropdown-content\">If:  <br> x <br> Preposition or suburdinating conjunction <br> </div></span>"
        text = "If-the-dull substance of my-flesh-were thought,"
        lines = Words.turnTextIntoObjects(text)
        firstWord = lines[0].list[0].syll_str()
        self.assertEqual(firstWord, expectedFirstWordOutput)

    def test_mix_of_dashes_on_full_poem(self):
        expectedFirstWordOutput = "<span class=\"word\" id=\"0 If\" onClick=\"getDefinitionOrEdit(event)\"><div class=\"Preposition or suburdinating conjunction\"><output-font class=\"unstressed\">If</output-font></div><div class=\"dropdown-content\">If:  <br> x <br> Preposition or suburdinating conjunction <br> </div></span>"
        text = "If the dull-substance of my flesh-were thought, \n Injurious distance should not stop my way; \n For then despite of space I would be brought, \n From limits far remote where thou dost stay. \n No matter then although my foot did stand \n Upon the farthest earth removed from thee; \n For nimble thought can jump both sea and land \n As soon as think the place where he would be. \n But ah! thought kills me that I am not thought, \n To leap large lengths of miles when thou art gone, \n But that so much of earth and water wrought \n I must attend time's leisure with my moan, \n Receiving nought by elements so slow \n But heavy tears, badges of either's woe. \n "
        lines = Words.turnTextIntoObjects(text)
        firstWord = lines[0].list[0].syll_str()
        self.assertEquals(firstWord, expectedFirstWordOutput)

        #Failing as of 10/08
    def test_inputs_with_misspellings(self):
        expectedUnknownWordOutput = "<span class=\"word\" id=\"0 Afrg\" onClick=\"getDefinitionOrEdit(event)\"><div class=\"unknown\"><output-font class=\"unknown\">Afrg</output-font></div><div class=\"dropdown-content\">Afrg: <br>?<br>unknown<br></div></span>"
        text = "Afrg the dull substance of my flesh were thought,"
        lines = Words.turnTextIntoObjects(text)
        firstWord = lines[0].list[0].syll_str()
        self.assertEqual(firstWord, expectedUnknownWordOutput)

    def test_whole_text_misspelled(self):
        expectedUnknownWordOutput = "<span class=\"word\" id=\"0 oijityfytf\" onClick=\"getDefinitionOrEdit(event)\"><div class=\"unknown\"><output-font class=\"unknown\">oijityfytf</output-font></div><div class=\"dropdown-content\">oijityfytf: <br>?<br>unknown<br></div></span>"
        text = "oijityfytf ugiugty uyigytf"
        lines = Words.turnTextIntoObjects(text)
        firstWord = lines[0].list[0].syll_str()
        self.assertEqual(firstWord, expectedUnknownWordOutput)

    def test_word_after_a_misspelling(self):
        expectedSecondWordOutput = "<span class=\"word\" id=\"1 the\" onClick=\"getDefinitionOrEdit(event)\"><div class=\"Determiner\"><output-font class=\"unstressed\">the</output-font></div><div class=\"dropdown-content\">the:  <br> x <br> Determiner <br> </div></span>"
        text = "Afrg the dull substance of my flesh were thought,"
        lines = Words.turnTextIntoObjects(text)
        secondWord = lines[0].list[1].syll_str()
        self.assertEqual(secondWord, expectedSecondWordOutput)

    def test_foreign_words(self):
        expectedFirstWordOutput = "<span class=\"word\" id=\"0 oeuf\" onClick=\"getDefinitionOrEdit(event)\"><div class=\"unknown\"><output-font class=\"unknown\">oeuf</output-font></div><div class=\"dropdown-content\">oeuf: <br>?<br>unknown<br></div></span>"
        text = "oeuf something else in French"
        lines = Words.turnTextIntoObjects(text)
        firstWord = lines[0].list[0].syll_str()
        self.assertEquals(firstWord, expectedFirstWordOutput)
    
    def test_multiple_punctuation(self):
        expectedFirstWordOutput = "<span class=\"word\" id=\"0 If\" onClick=\"getDefinitionOrEdit(event)\"><div class=\"Preposition or suburdinating conjunction\"><output-font class=\"unstressed\">If</output-font></div><div class=\"dropdown-content\">If:  <br> x <br> Preposition or suburdinating conjunction <br> </div></span>"
        text = "If the dull-substance,, of my. flesh were thought,"
        lines = Words.turnTextIntoObjects(text)
        # line = lines[0].syll_str_line()
        firstWord = lines[0].list[0].syll_str()
        self.assertEqual(firstWord, expectedFirstWordOutput)

        

class TestAccuracy(TestCase):
    
    def test_all_sonnets(self):
        result = helper_test_a_file_of_poems("all_sonnets")
        self.assertEquals("PASS", result)
    
    def test_mis_of_contemporary(self):
        result = helper_test_a_file_of_poems("mix_of_contemporary")
        self.assertEquals("PASS", result)

    def test_mix_of_older(self):
        result = helper_test_a_file_of_poems("mix_of_older_poems")
        self.assertEquals("PASS", result)

def helper_test_a_file_of_poems(fileName):
    finalFileName = fileName + ".txt"
    fileContents = open(finalFileName, "r")
    fileText = fileContents.read()
    fileContents.close()
    fails = 0
    correctGuesses = 0
    result = ""

    poems_array = fileText.split("\n\n\n")
    textFileName = "Accuracy_results_for__" + fileName + "__.txt"
    textFile = open(textFileName, "w+")
    for poem in poems_array:
        poemFailed = False
        expectedMeter = poem.partition("\n")[0]
        poemText = poem.partition("\n")[2]
        poemObject = Words.turnTextIntoObjects(poemText)
        scansionMeter = views.getBestMeter(poemObject)
        z = re.match(expectedMeter, scansionMeter['meter'])
        if z and scansionMeter['count'] >= scansionMeter['total']/2:
            textFile.write("PASS")
            textFile.write("\t\"" + poemText.split("\n")[0] + "\", Expected: " + expectedMeter + ", Scansion's: " + scansionMeter['meter'])
        else:
            textFile.write("FAIL")
            poemFailed = True
            fails+=1
            textFile.write("\t\"" + poemText.split("\n")[0] + "\", Expected: " + expectedMeter + ", Scansion's best guess: " + scansionMeter['meter'])
            if z:
                correctGuesses +=1
        # if poemFailed:
        #     textFile.write(" (Best guess: " + scansionMeter['secondMeter'] + ")")
        textFile.write("\n")
    if (fails <= len(poems_array)/10):
        stringForTextFile = "\nPASS"
        result = "PASS"
    else:
        stringForTextFile = "\nFAIL"
        result = "FAIL"
    stringForTextFile += ": "
    stringForTextFile += str(fails)
    stringForTextFile += " fails out of " + str(len(poems_array)) + " poems. " + str(correctGuesses) + " correct 'best guesses'."
    textFile.write(stringForTextFile)
    textFile.close()
    return result    


        
        
