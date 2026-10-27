from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news_list, name='news'),
    path('teachers/', views.teacher_list, name='teachers'),
    path('books/', views.book_list, name='books'),
    path('schedule/', views.schedule_list, name='schedule'),
]