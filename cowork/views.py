from django.shortcuts import render


def index(request):
    return render(request, 'cowork/index.html')

def error_404(request, exception):
    return render(request, '404.html')

def error_400(request, exception):
    return render(request, '400.html')
