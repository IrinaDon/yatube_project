from django.shortcuts import render
​
# Главная страница
def index(request):    
    template = 'posts/index.html'
    return render(request, template)
​
# Страницы сообществ 
def group_list(request):
    template = 'posts/group_list.html'
    return render(request, template)
