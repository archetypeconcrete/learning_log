"""Определяет схемы URL для learning_logs."""
from django.urls import path, re_path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Домашняя страница
    # url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),

    # Вывод всех тем
    path('topics/', views.topics, name='topics'),

    # Страница с подробной информацией по отдельной теме
    # re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    path('topics/<topic_id>/', views.topic, name='topic'),

    # Страница для добавления новой темы
    path('new_topic/', views.new_topic, name='new_topic'),

    # Страница для добавления новой записи
    path('new_entry/<topic_id>/', views.new_entry, name='new_entry'),

    # Страница для редактирования записи
    path('edit_entry/<entry_id>/', views.edit_entry, name='edit_entry'),
]



