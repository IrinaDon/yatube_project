from django.http import HttpResponse
# Импортируем загрузчик.
from django.template import loader


def index(request):
    # Загружаем шаблон;
    # шаблоны обычно хранят в отдельной директории.
    template = 'posts/index.html'
    # Формируем шаблон
    return render(request, template)

def group_posts (reguest, any_slug)   
    return HttpResponse ('posts, filtered by groups') 
