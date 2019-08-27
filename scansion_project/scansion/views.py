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
    # simple view, either presenting an input screen or the analysis version. 
    if request.method == 'POST':
        form = TextForm(request.POST)

        text = request.POST.get('text')
        lines = Words.turnTextIntoObjects(text)
        foot = getBestMeter(lines)
        context_dict = {'lines': lines, 'foot': foot}
        return analyse(request, context_dict)
    else:
        form = TextForm()
    return render(request, 'scansion/index.html', {'form': form})

# Helper method which counts each lines analysis to determine which is the most recurring. 
def getBestMeter(lines):
    allPatterns = []
    totalLines = 0

    for line in lines:
        if line.hasWords:
            totalLines += 1
            allPatterns.append(str(line.foot + " " + line.numOfFeet))
    
    counter = collections.Counter(allPatterns)
    data = counter.most_common(1)
    for meter, frequency in data:
        textMeter = meter
        count = frequency
    if re.match("unknown", textMeter):
        print("Text meter: " + textMeter + " Count: " + str(count))

        
        for meter, frequency in counter.most_common(2):
            textMeter = meter
            count = frequency
            print("New textMeter: " + textMeter + " count: " + str(count))
        info = {'meter': textMeter, 'count': count, 'total': totalLines, 'message': "Unknown"}
        return info
    elif count < totalLines/2:
        info = {'meter': textMeter, 'count': count, 'total': totalLines, 'message': "Unknown"}

    else:
        info = {'meter': textMeter, 'count': count, 'total': totalLines}
        return info


def about(request):
    return render(request, 'scansion/about.html')

def analyse(request, context_dict):
    return render(request, 'scansion/analyse.html', context_dict)

