from django.shortcuts import render
from django.http import HttpResponse
from scansion.forms import TextForm
import prosodic as p
import re
import Words
# import syllabify
# from prosodic import syllabifier as syl 

def index(request):

    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            text = cd.get('text')
            text = text.splitlines()
            prosodicLines = []
            giveMeEverything = []
            words = []
            # For loop splits text from the form into lines and parses them using prosodic
            for line in text:
                t = p.Text(line)
                t.parse()

                for parse in t.bestParses():
                    # This adds the top parse to the lines list.
                    prosodicLines.append(parse)
            # This loops through the lines list and breaks each one into words, then Words. 
            # It then calls giveMeEverything and adds that data to a list
            for x in range(0, len(prosodicLines)):
                line = prosodicLines[x].words()
                for y in range(0, len(line)):
                    stringWord = line[y].__str__() # This returns more than just the string of the word - hence using split() etc to just retrieve what I need.
                    stringWord = stringWord.split()
                    word = Words.Word(stringWord[0])
                    words.append(word)
                    giveMeEverything.append(word.giveMeEverything())
            lines = []
            for line in text:
                l1 = Words.Line(line)
                lines.append(l1)
            
            context_dict = {'prosodicLines': prosodicLines, 'original': text, 'everything': giveMeEverything, 'words': words, 'lines': lines}
            return analyse(request, context_dict)
    else:
        form = TextForm()
    return render(request, 'scansion/index.html', {'form': form})


def about(request):
    return render(request, 'scansion/about.html')

def how_to(request):
    return render(request, 'scansion/how_to.html')

def analyse(request, context_dict):
    return render(request, 'scansion/analyse.html', context_dict)
    
def analyse_how_to(request):
    return render(request, 'scansion/analyse_how_to.html')

def writing(request):
    return render(request, 'scansion/writing.html')

def writing_how_to(request):
    return render(request, 'scansion/writing_how_to.html')
