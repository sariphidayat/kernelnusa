from django.shortcuts import render

from django.http import JsonResponse


def home(req):
    return JsonResponse({'detail': 'Welcome'})


def foobar(req):
    data = {'detail': 'Hello World'}
    return JsonResponse(data)
