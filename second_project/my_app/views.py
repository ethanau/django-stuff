from django.shortcuts import render
from .models import User


# Create your views here.
def index(request):
    return render(request, 'my_app/index.html')


def user(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'my_app/user.html', context=user_dict)
