from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'odp_demo/index.html', {})


def dashboard(request):
    return render(request, 'odp_demo/dashboard.html', {})

def energy(request):
    return render(request, 'odp_demo/energy.html', {})

def transport(request):
    return render(request, 'odp_demo/transport.html', {})

def env(request):
    return render(request, 'odp_demo/env.html', {})

def agriculture(request):
    return render(request, 'odp_demo/agriculture.html', {})

def kelec(request):
    return render(request, 'odp_demo/kelec.html', {})

def monum(request):
    return render(request, 'odp_demo/monum.html', {})

def upload(request):
    return render(request, 'odp_demo/upload.html', {})
