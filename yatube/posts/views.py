from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_1(request):
    return HttpResponse('Список мороженого')


def group_posts(request, slug):
    return HttpResponse('Виды мороженого')
