# #our file for writing function
# from django.http import HttpResponse
# def index(request):
#     f=open("abc.txt", "r")
#     return HttpResponse(f.read())
#     f.close()
#
# def about(request):
#     return HttpResponse("Django Started.... About page")
#
# def personalnav(request):
#     a='''<h1>Personal Nevigation</h1>
#         <a href="http://www.youtube.com">Youtube.com</a>
#         <a href="http://www.facebook.com">Facebook.com</a>
#         <a href="http://www.twitter.com">Twitter.com</a>'''
#
#     return HttpResponse(a)


#pipline
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     params={'name':"harry",'channnel':'code with harry'}
#     return render(request,'index.html',params)
#     # return HttpResponse("Home")
#
# def removepunc(request):
#     text1=(request.GET.get('text','default'))
#     print(text1)
#     return HttpResponse("remove punc")
#
#
# def capitalizefirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("New line remove")
#
# def spaceremove(request):
#     return HttpResponse("Space Remove")
#
# def charcount(request):
#     return HttpResponse("Character Counting")



def index(request):
    return render(request,'index.html')


def analyze(request):

    #taking values from index.html
    text1=(request.POST.get('text','default'))
    removepunc = (request.POST.get('removepunc', 'off'))
    capitalize = (request.POST.get('capitalize', 'off'))
    lowercase= (request.POST.get('lowercase', 'off'))
    newlineremover= (request.POST.get('newlineremover', 'off'))
    spaceremover = (request.POST.get('spaceremover', 'off'))
    charctercount = (request.POST.get('charctercount', 'off'))
    # print(removepunc)
    # print(text1)
    # analysed=text1

    #condtion for punctuation
    if removepunc=='on':
        punctuation='''!()-[]{};:' ''\,<>./?@#%^&*_~'''
        analyzed=""
        for char in text1:
            if char not in punctuation:
                analyzed=analyzed + char
        params={'purpose':'Remove Punctuation','analyzed_text':analyzed}
        text1=analyzed
        # return render(request,"analyse.html",params)

    # condtion for Capitalization
    if capitalize=='on':
        analyzed=""
        for char  in text1:
            analyzed= analyzed + char.upper()
        params = {'purpose': 'Capitalize All Words  ', 'analyzed_text': analyzed}
        text1 = analyzed
        # return render(request, "analyse.html", params)

    # condtion for lowercase
    if lowercase=='on':
        analyzed=""
        for char  in text1:
            analyzed= analyzed + char.lower()
        params = {'purpose': 'Lowercase All Words  ', 'analyzed_text': analyzed}
        text1 = analyzed
        # return render(request, "analyse.html", params)

    #New line remover
    if newlineremover=='on':
        analyzed=""
        for char  in text1:
            if char!="\n" and char!="\r":
                analyzed= analyzed + char
        params = {'purpose': 'New Line Remover  ', 'analyzed_text': analyzed}
        text1 = analyzed
        # return render(request, "analyse.html", params)

    #space remover
    if spaceremover =='on':
        analyzed = ""
        for index, char in enumerate(text1):
            if not (text1[index]==" " and text1[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Space Remover', 'analyzed_text': analyzed}
        text1 = analyzed
        # return render(request, "analyse.html", params)

    #character count
    if charctercount == 'on':
        analyzed = ""
        for char in text1:
            analyzed =(len(text1))
            analyzed=str(analyzed)

        params = {'purpose': 'Character Counting', 'analyzed_text': analyzed}
        text1 = analyzed+char

    if(capitalize!='on' and removepunc!='on' and lowercase!='on' and newlineremover!='on'
            and spaceremover !='on'and charctercount != 'on'):
        return HttpResponse("Please select operation")
        # return render(request, "analyse.html", params)
    #
    # else:
    #     return HttpResponse("Error")

    return render(request, "analyse.html", params)