from django.shortcuts import render


def description(request):
    template = 'about/description.html'
    title = 'О проекте'
    context = {
        'title': title
    }
    return render(request, template, context)
