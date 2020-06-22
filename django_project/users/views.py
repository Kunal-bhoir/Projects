from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from .forms import UserRegisterForm

def register(requests):
    if requests.method == 'POST':
        form = UserRegisterForm(requests.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(requests, f'Your account has been created! you can login now')
            return redirect('login')
    else:        
        form = UserRegisterForm()
    return render(requests, 'users/register.html', {'form': form})

@login_required
def profile(requests):
    return redirect(requests, 'users/profile.html')   


# Create your views here.
