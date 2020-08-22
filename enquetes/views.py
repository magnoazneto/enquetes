from django.shortcuts import render
from django.http import HttpResponse

def bemvindo(request):
    return render(request, 'bemvindo.html')