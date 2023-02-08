from django.shortcuts import render 





def index(request):

    context = {}
    return render(request, 'project/index.html', context)