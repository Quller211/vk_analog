from django.urls import path

from . import views


urlpatterns = [
    path('', views.main, name = 'main'),
    path('mainpage/<int:log_id>/', views.mainpage, name = 'mainpage'),
    path('login_page/<int:log_id>/', views.login_page, name = 'login_page'),
    path('login_page/<int:log_id>/news_page/', views.news_list, name = 'news_list'),
    path('login_page/<int:log_id>/news_page/add_news/', views.add_news, name = 'add_news'),
    path('login_page/<int:log_id>/news_page/<int:news_detail_id>/', views.news_detail, name = 'news_detail'),
]