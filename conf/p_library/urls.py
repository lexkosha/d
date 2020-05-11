from django.urls import path

from . import views

app_name = 'p_library'

urlpatterns = [
    path('author_book/create_many', views.books_authors_create_many, name='author_book_create_many'),
    path('author/create_many/', views.author_create_many, name='author_create_many'),
    path('', views.index),
    path('redacktions/', views.redaction),
    path('index/', views.index),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('author/create/', views.AuthorEdit.as_view(), name='author_create'),
    path('authors/', views.AuthorList.as_view(), name='author_list'),


]