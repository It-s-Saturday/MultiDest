from django.conf.urls import url
from django.middleware.csrf import get_token
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie

from .logic import computefromdjango


def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})


def ping(request):
    return JsonResponse({'result': 'OK'})


def parse_function(request):
    """
    This function parses the information from the react form into our computation script using a GET request.
    """
    choice = request.GET.get('optimize_for')
    if choice == "time":
        choice = "duration"
    method = request.GET.get('method')
    lst = request.GET.getlist('stop')  # note that lst contains every entry from the textarea
    print(lst)
    origin = lst[0]
    dest = lst[-1]
    # print("*****************************************")
    # print(choice, method, origin, lst, dest)
    # print("*****************************************")
    computed = computefromdjango.compute(choice, method, origin, dest, lst)
    context = {'path': str(computed[0]), 'metric': computed[1]}

    return render(request, 'results.html', context)
