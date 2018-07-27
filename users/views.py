from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'registration/login.html', {'message': 'Registration completed successfully. You can sign in now.'})
    else:
        form = SignUpForm()
    return render(request, 'users/create_user.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
