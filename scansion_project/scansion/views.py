from django.shortcuts import render
from django.http import HttpResponse
# import prosodic as p

def index(request):
    return render(request, 'scansion/index.html')

def about(request):
    return render(request, 'scansion/about.html')

def how_to(request):
    return render(request, 'scansion/how_to.html')

# def analyse(request):
#     # text_input = "Shall I compare thee to a summer's day?"
#     # try:
#     #     context_dict = {'sonnet': text_input}
#     # except text_input.DoesNotExist:
#     #     context_dict = {'sonnet': "Shall I compare thee to a summer's day?"}
#     return render(request, 'scansion/analyse.html')
def analyse(request):
    return render(request, 'scansion/analyse.html')
    
def analyse_how_to(request):
    return render(request, 'scansion/analyse_how_to.html')

def writing(request):
    return render(request, 'scansion/writing.html')

def writing_how_to(request):
    return render(request, 'scansion/writing_how_to.html')
