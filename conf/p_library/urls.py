from django.contrib import admin
from django.urls import path

#from p_library.views import AuthorEdit, AuthorList
from . import views

app_name = 'p_library'

urlpatterns = [
    path('author/create_many/', views.author_create_many, name='author_create_many'),
    path('', views.index),
    path('redacktions/', views.redaction),
    path('index/', views.index),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('author/create/', views.AuthorEdit.as_view(), name='author_create'),
    path('authors', views.AuthorList.as_view(), name='author_list'),


]