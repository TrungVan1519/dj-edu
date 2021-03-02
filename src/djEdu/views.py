from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def handle_404(request, exception):
    return render(request, '404.html')
