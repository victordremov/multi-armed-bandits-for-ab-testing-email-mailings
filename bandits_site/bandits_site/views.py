from django.shortcuts import render, redirect


def home(request):
    return render(request, 'bandits_site/home.html')


def visualization(request):
    return render(request, 'bandits_site/visualization.html')

def classic_ab_tests(request):
    return render(request, 'bandits_site/classic-ab-tests.html')


def multi_armed_bandits(request):
    return render(request, 'bandits_site/multi-armed-bandits.html')