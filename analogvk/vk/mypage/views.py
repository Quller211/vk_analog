from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from datetime import *
from django.contrib.auth import authenticate, login
from .models import News, UserDescripe
from django.contrib.auth.forms import UserCreationForm
from .forms import AddNewsForm, LoginForm, RegistrationForm

# def main(request):
#     # Вход в аккаунт
#     if request.method == 'POST':
#         form = MainLoginForm(request.POST)
#         if form.is_valid():
#             # Если пользователь есть, переходит на страницу
#             if Login.objects.filter(user_login = form.cleaned_data['user_login']).exists():
#                 log_id = Login.objects.get(user_login = form.cleaned_data['user_login']).id
#                 return HttpResponseRedirect(reverse('login_page', args = [log_id]))
#             else:
#                 # Если нет, заносится в базу данных и переходит на страницу для добавления доп инфы
#                 i = form.save()
#                 log_id = i.id
#                 return HttpResponseRedirect(reverse('mainpage', args = [log_id]))
#     else:
#         form = MainLoginForm()
#     return render(request, 'mypage/main.html', {'form': form})

# Страница авторизации
def main(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password = cd['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('login_page', args = [user.id]))
            else:
                err_mess = 'Неправильный логин или пароль'
                return render(request, 'mypage/main.html', {'form': form, 'err_mess': err_mess})
    else:
        form = LoginForm()
    return render(request, 'mypage/main.html', {'form': form})

# Страница регистрации
def registr_page(request):
    if request.method == 'POST':
        form1 = UserCreationForm(request.POST)
        form2 = RegistrationForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            k = form1.save()
            i = form2.save(commit = False)
            i.user_id = k.id
            i.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        form1 = UserCreationForm()
        form2 = RegistrationForm()
    return render(request, 'mypage/registr_page.html', {'form1': form1, 'form2': form2})

# def mainpage(request, log_id):
    if request.method == 'OST':
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
    data = UserDescripe.objects.get(user_id = log_id)
    user_news = News.objects.filter(posted_by_id = log_id)
    return render(request, 'mypage/login_page.html', {'data': data, 'log_id': log_id, 'user_news': user_news})

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
