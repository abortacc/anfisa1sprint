from django.shortcuts import render


def index(request):
    template = 'homepage/index.html'
    title = 'Главная страница'
    context = {
        'title': title
    }
    return render(request, template, context)
