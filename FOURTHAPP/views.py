from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fourth(request):
    return HttpResponse("<marquee><i>THIS IS MY FOURTH PROJECT<i><marquee>")
