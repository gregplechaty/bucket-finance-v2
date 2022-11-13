from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def react_app(request):
    print('hitting react_app')
    index_contents = open('../client/build/index.html').read()
    
    return HttpResponse(index_contents)