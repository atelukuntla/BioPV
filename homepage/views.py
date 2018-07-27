from django.shortcuts import render


def index(request):
    return render(request, 'homepage/index.html')


def contact_us(request):
    return render(request, 'homepage/contact_us.html', {})


def about_us(request):
    return render(request, 'homepage/about_us.html', {})


def our_team(request):
    return render(request, 'homepage/our_team.html', {})
