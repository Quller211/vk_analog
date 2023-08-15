from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from datetime import *
from .models import Login, MainPage, News
from .forms import MainPageForm, MainLoginForm, AddNewsForm

def main(request):
    # Вход в аккаунт
    if request.method == 'POST':
        form = MainLoginForm(request.POST)
        if form.is_valid():
            # Если пользователь есть, переходит на страницу
            if Login.objects.filter(user_login = form.cleaned_data['user_login']).exists():
                log_id = Login.objects.get(user_login = form.cleaned_data['user_login']).id
                return HttpResponseRedirect(reverse('login_page', args = [log_id]))
            else:
                # Если нет, заносится в базу данных и переходит на страницу для добавления доп инфы
                i = form.save()
                log_id = i.id
                return HttpResponseRedirect(reverse('mainpage', args = [log_id]))
    else:
        form = MainLoginForm()
    return render(request, 'mypage/main.html', {'form': form})

def mainpage(request, log_id):
    if request.method == 'POST':
        form = MainPageForm(request.POST)
        if form.is_valid():
            date_valid = form.cleaned_data['date_of_birth']
            if (datetime.date(datetime.today()) - date_valid).days < 0:
                message = 'Вы не могли родиться в будущем. Правильно введите дату рождения'
                form = MainPageForm()
                return render(request, 'mypage/mainpage.html', {'form': form, 'message': message})
            i = form.save(commit = False)
            i.login_in_id = log_id
            i.save()
            return HttpResponseRedirect(reverse('login_page', args = [log_id]))
    else:
        message = 'Вы новый пользователь. Введите, пожалуйста, дополнительные данные'
        form = MainPageForm()    
    return render(request, 'mypage/mainpage.html', {'form': form, 'message': message})

def login_page(request, log_id):
    data = MainPage.objects.get(login_in_id = log_id)
    return render(request, 'mypage/login_page.html', {'data': data, 'log_id': log_id})

def news_list(request, log_id):
    content = News.objects.filter(posted = True)[:5]
    return render(request, 'mypage/news.html', {'content': content, 'log_id': log_id})

def add_news(request, log_id):
    if request.method == 'POST':
        form = AddNewsForm(request.POST, request.FILES)
        if form.is_valid():
            print(True)
            i = form.save(commit = False)
            i.posted_by_id = log_id
            i.save()
            return HttpResponseRedirect(reverse('news_list', args = [log_id]))
    else:
        form = AddNewsForm()
        return render(request, 'mypage/add_news.html', {'form': form, 'log_id': log_id})
    
def news_detail(request, log_id, news_detail_id):
    content = News.objects.get(id = news_detail_id)
    return render(request, 'mypage/news_detail.html', {'content': content, 'log_id': log_id})
