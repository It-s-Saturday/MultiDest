from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# from logic import computewithapi
# Create your views here.

def simple_function(request):
    list = []
    # print("cunt baby")
    computewithapi.compute(list)
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")