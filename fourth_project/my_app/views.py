from django.shortcuts import render


# Create your views here.
def index(request):
    content_dict = {'text': 'hello world',
                    'number': 100}
    return render(request, 'my_app/index.html', content_dict)


def other(request):
    return render(request, 'my_app/other.html')


def relative(request):
    return render(request, 'my_app/relative.html')