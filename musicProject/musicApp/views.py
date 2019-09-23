from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is a bad request, Start with the music route")
def music(request):
    return HttpResponse("lists of routes: ludacris, eminem, donTrip")
def ludacris(request):
    return HttpResponse("Top 10 rapper.")
def eminem(request):
    return HttpResponse("number 1 rapper")
def donTrip(request):
    return HttpResponse("top 3 out of memphis")