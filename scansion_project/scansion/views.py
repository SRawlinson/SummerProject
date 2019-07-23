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
            # prosodicLines = []
            # giveMeEverything = []
            # words = []
            # For loop splits text from the form into lines and parses them using prosodic
            # for line in text:
            #     t = p.Text(line)
            #     t.parse()

            #     for parse in t.bestParses():
            #         # This adds the top parse to the lines list.
            #         prosodicLines.append(parse)

            lines = []
            for line in text:
                l1 = Words.Line(line)
                lines.append(l1)
            info = []
            for line in lines:
                l1  ={'foot': line.foot, 'numOfFeet': line.numOfFeet}
                info.append(l1)
            # context_dict = {'prosodicLines': prosodicLines, 'lines': lines}
            foot = getBestMeter(lines)
            context_dict = {'lines': lines, 'info': info, 'foot': foot}
            return analyse(request, context_dict)
    else:
        form = TextForm()
    return render(request, 'scansion/index.html', {'form': form})

def getBestMeter(lines):
    biggest = 1
    foot = ""
    footLine = ""
    numLine = ""
    for line in lines:
        footLine = footLine + line.foot
        numLine = numLine + line.numOfFeet
    trochaic = footLine.count("trochaic")
    if trochaic >= biggest:
        biggest = trochaic
        foot = "trochaic"
    spondaic = footLine.count("spondaic")
    if spondaic >= biggest:
        biggest = spondaic
        foot = "spondaic"
    anapestic = footLine.count("anapestic")
    if anapestic >= biggest:
        biggest = anapestic
        foot = "anapestic"
    dactylic = footLine.count("dactylic")
    if dactylic >= biggest:
        biggest = dactylic
        foot = "dactylic"
    # unknown = footLine.count("unknown")
    # if unknown >= biggest:
    #     biggest = unknown
    #     foot = "unknown"
    iambic = footLine.count("iambic")
    if iambic >= biggest:
        biggest = iambic
        foot = "iambic"
    dimeter = numLine.count("dimeter")
    trimeter = numLine.count("trimeter")
    tetrameter = numLine.count("tetrameter")
    pentameter = numLine.count("pentameter")
    hexameter = numLine.count("hexameter")
    heptameter = numLine.count("heptameter")
    octometer = numLine.count("octometer")
    numOfFeetDict = {'dimeter': dimeter, 'trimeter': trimeter, 'tetrameter': tetrameter, 'pentameter': pentameter, 'hexameter': hexameter, 'heptameter': heptameter, 'octometer': octometer}
    numDictSorted = sorted(numOfFeetDict, key=numOfFeetDict.__getitem__)
    num = len(numDictSorted) -1
    numOfFeetForText = numDictSorted[num]
    foot = foot + " " + numOfFeetForText
    return foot
    
        


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
