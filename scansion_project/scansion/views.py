from django.shortcuts import render
from django.http import HttpResponse
from scansion.forms import TextForm
import prosodic as p
import re
import Words
import collections
# import syllabify
# from prosodic import syllabifier as syl 

def index(request):

    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            text = cd.get('text')
            # text = text.splitlines()

            lines = Words.turnTextIntoObjects(text)
            # for line in lines:
            #     l1  ={'foot': line.foot, 'numOfFeet': line.numOfFeet}
            foot = getBestMeter(lines)
            context_dict = {'lines': lines, 'foot': foot}
            return analyse(request, context_dict)
    else:
        form = TextForm()
    return render(request, 'scansion/index.html', {'form': form})

def getBestMeter(lines):
    allPatterns = []
    totalLines = len(lines)

    for line in lines:
        allPatterns.append(str(line.foot + " " + line.numOfFeet))
    
    counter = collections.Counter(allPatterns)
    data = counter.most_common(1)
    for meter, frequency in data:
        textMeter = meter
        count = frequency
    if re.match("unknown", textMeter):
        
        for meter, frequency in counter.most_common(2):
            textMeter = meter
            count = frequency
        info = {'meter': textMeter, 'count': count, 'total': totalLines, 'message': "Unknown"}
        return info
    else:
        info = {'meter': textMeter, 'count': count, 'total': totalLines}
        return info


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
