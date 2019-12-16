# This file is created by SATHISH

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text from user
    djtext = request.POST.get('text', 'default')

    # Check Checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if extraspaceremover == "on":
        analyzed = ""
        for i, char in enumerate(djtext):
            if not (djtext[i] == " " and djtext[i + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}


    if removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on":
        return HttpResponse("Please Select any option and Try Again")

    return render(request, 'analyze.html', params)


def about(request):
    return render(request, 'about.html')


