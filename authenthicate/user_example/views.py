from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from user_example.models import userPhone
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@csrf_exempt
def index(request):
    count = User.objects.count()        ### Count number of users that are login
    return render(request, 'user_example/index.html', { 'count' : count })

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            phone_number = form.cleaned_data.get('phone_number')

            userPhone.objects.create(user = username, phone = phone_number)

            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form })

@login_required
@csrf_exempt
def secret_page(request):
    return render(request, 'secret_page.html')
    
