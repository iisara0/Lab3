

from django.http import HttpResponse
from django.shortcuts import render

def index(request):                     #Task1
    return render("Hello, world!")


def index(request):                      #Task2
    name = request.GET.get("name") or "world!"  #add this line
    return render("Hello, "+name) #replace the word “world!” with the variable name


def index(request):                     #Task3
    name = request.GET.get("name") or "world!"
    return render("Hello, "+name)

def index2(request, val1 = 0):   #add the view function (index2)
    return render("value1 = "+str(val1))

def index(request):   #Task4
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})


def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context)
