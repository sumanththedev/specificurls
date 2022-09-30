from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def pirate(request):
    return HttpResponse("<center><h1>hello pirates</center></h1>")