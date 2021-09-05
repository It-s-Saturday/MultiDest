from django.conf.urls import url
from django.middleware.csrf import get_token
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import ensure_csrf_cookie

from .logic import computefromdjango



def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})


def ping(request):
    return JsonResponse({'result': 'OK'})


def show_results(request):
    return HttpResponse('results')


# @ensure_csrf_cookie
def parse_function(request):
    """
    This function parses the information from the react form into our computation script using a GET request.
    """
    choice = request.GET.get('optimize_for')
    if choice == "time":
        choice = "duration"
    method = request.GET.get('method')
    lst = request.GET.get('inner_list').split("\r\n")  # note that lst contains every entry from the textarea
    print(lst)
    origin = lst[0]
    dest = lst[-1]
    # print("*****************************************")
    # print(choice, method, origin, lst, dest)
    # print("*****************************************")
    computefromdjango.compute(choice, method, origin, dest, lst)
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")
