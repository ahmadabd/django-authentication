from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    count = User.objects.count()        ### Count number of users that are login
    return render(request, 'user_example/index.html', { 'count' : count})


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)

            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'registration/register.html', context)
