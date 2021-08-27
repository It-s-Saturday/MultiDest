from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def simple_function(request):
    print("\nThis is a simple function\n")
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")