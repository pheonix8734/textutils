# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


# code for video 6

# def index(request):
#     return HttpResponse('''<h1>Hello beta</h1> <a href="https://www.ceew.in/publications/what-smart-meters-can-tell-us"> django code with harry </a>''')
#
# def about(request):
#     return HttpResponse(" About Hello")

# code for video 7

def index(request):
    # params={'name':'harry','place':'Mars'}
    # return render(request,'index.html',params)

    return render(request, 'index.html')
    # return HttpResponse("Home")


def analyze(request):
    # get the text

    djtext = request.GET.get('text', 'default')

    # check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')

    # print(removepunc)
    # print(djtext)
    # analyzed=djtext

    # check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

    params = {'purpose': 'Removed punctuatuions', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)

elif (fullcaps == "on"):
analyzed = ""
for char in djtext:
    analyzed = analyzed + char.upper()
    params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}

    # analyze the text

    return render(request, 'analyze.html', params)
elif (newlineremover == "on"):
analyzed = ""
for char in djtext:
    if (char != "\n"):
        analyzed = analyzed + char
params = {'purpose': 'Removed new line', 'analyzed_text': analyzed}

# analyze the text

return render(request, 'analyze.html', params)
else:
return HttpResponse("Error")

# def removepunc(request):
#
#     #get the text
#
#     djtext = request.GET.get('text','default')
#     print(djtext)
#
#     #analyze the text
#
#     return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("Capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("new line remove")
#
# def spaceremove(request):
#     return HttpResponse("space remover")
#
# def charcount(request):
#     return HttpResponse("<a href='/'>back </a>")
