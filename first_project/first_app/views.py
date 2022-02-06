from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def any_response(request):
    return HttpResponse("Hi, Good day!")


def index(request):
    context = {'name': 'Yebin'}
    return render(request, 'first_app/index.html', context)


def say_hello(request):
    return HttpResponse("Hello World!")