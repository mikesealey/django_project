from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about_me(request):
    return HttpResponse("This would be the about pageThis would be the about page")

def test1(request):
    return HttpResponse("<h1>This is a title</h1><br><h2>This is a subtitle</h2>")