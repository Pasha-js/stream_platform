from django.shortcuts import render 





def index(request):
    context = {}
    return render(request, 'templates/index.html', context)


def test(request):
    context = {}
    return render(request, 'templates/test.html', context)