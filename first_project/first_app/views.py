from django.shortcuts import render
from django.http import HttpResponse
from .models import AccessRecord, Topic, WebPage


# Create your views here.
def any_response(request):
    return HttpResponse("Hi, Good day!")


def home_page(request):
    return HttpResponse("This is the home page!")


def index(request):
    context = {'name': 'Yebin'}
    return render(request, 'first_app/index.html', context)


def access_records(request):
    webpage_lists = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_lists}
    return render(request, 'first_app/records.html', context=date_dict)


def say_hello(request):
    return HttpResponse("Hello World!")