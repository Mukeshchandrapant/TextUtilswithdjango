# I have created this file - Mukesh
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze_text(request):

    # get the text form textArea
    djtext = request.POST.get('text', 'default')

    # check the values of check boxes.
    remove_punc = request.POST.get('removepunc', 'off')
    full_caps = request.POST.get('fullcaps', 'off')
    new_line_remove = request.POST.get('newlineremove', 'off')
    extra_space_remove = request.POST.get('extraspaceremove', 'off')
    char_counter = request.POST.get('charcounter', 'off')

    # check if checkbox is ON
    if remove_punc == "on":
        # define punctuation
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~='''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        # Analyze the text
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    # Code to convert lowercase letters into upper case.
    if(full_caps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Uppercase letter', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    # NEW line remover..
    if (new_line_remove == "on"):

        analyzed = ""
        for char in djtext:
            if char !="\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'New Line Remove', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    # Remove Extra Space in between Characters
    if(extra_space_remove =="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Space Remove between letters', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    # Count total number of character in the text area.
    if (char_counter == "on"):
        count = 0
        for char in djtext:
            if char != "":
                count = count + 1
        params = {'purpose': 'Total count of the letters', 'analyzed_text': count}

    if (remove_punc != "on" and full_caps != "on" and new_line_remove != "on"
            and extra_space_remove !="on" and char_counter != "on"):
        return HttpResponse("Error on loading!!")

    return render(request, 'analyze.html', params)
