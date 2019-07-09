from django.shortcuts import render
from django.http import HttpResponse
from scansion.forms import TextForm
import prosodic as p
import re
# import syllabify
# from prosodic import syllabifier as syl 

def index(request):

    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            text = cd.get('text')
            text = text.splitlines()
            lines = []
            for line in text:
                t = p.Text(line)
                t.parse()

                for parse in t.bestParses():
                    # print(parse)
                    lines.append(parse)
            for line in lines:
                print(line.str_stress)
            sylls = []
            # for word in words:
            #     sylls.append(word.syllables())
            
            context_dict = {'lines': lines, 'original': text, 'sylls': sylls}
            return analyse(request, context_dict)
    else:
        form = TextForm()
    return render(request, 'scansion/index.html', {'form': form})


#Hopefully a helper function to detect stressed syllables in a word
#Syllable objects don't  behave as I'd expect - can't treat them like strings?
def stressedSylls(word):
    sylls = word.syllables()
    shapes=[syll.getShape() for syll in sylls]
    for syl in sylls:
        print(syl)
    
    # for shape in shapes:
    #     print(shape)

    return True

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
