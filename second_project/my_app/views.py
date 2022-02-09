from django.shortcuts import render
from .models import User
from .forms import NewUser


# Create your views here.
def index(request):
    return render(request, 'my_app/index.html')


def user(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'my_app/user.html', context=user_dict)


def sign_up(request):

    form = NewUser()

    if request.method == 'POST':
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error form invalid')

    return render(request, 'my_app/sign_up.html', {'form': form})

