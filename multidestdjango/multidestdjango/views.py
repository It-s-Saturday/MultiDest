from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .logic import computefromdjango


def simple_function(request):
    choice = request.GET.get('optimize_for')
    if choice == "time":
        choice = "duration"
    method = request.GET.get('method')
    lst = request.GET.get('inner_list').split("\r\n")
    origin = lst[0]
    dest = lst[-1]
    print("*****************************************")
    print(choice, method, origin, lst, dest)
    print("*****************************************")
    computefromdjango.compute(choice, method, origin, dest, lst)
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")