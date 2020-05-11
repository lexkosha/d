from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.forms import formset_factory

# Create your views here.
from django.views.generic.base import View

from .models import Author, Book, PublishingHouse
from .forms import AuthorForm, BookForm


# class HomeView(View):
#     """Главная страница сайта"""
#     def get(self, requests):
#         context = {'book': Book.objects.all(),
#                    'num': range(1, 101),
#                    }
#         return render(requests, 'main/index.html', context)
#
# class AddBookView(View):
#     """Добавляем книгу"""
#     def post(self, requests):
#         book = Book.objects.filter(id=book_id).first()


class AuthorEdit(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'main/author_edit.html'


class AuthorList(ListView):
    model = Author
    template_name = 'main/authors_list.html'


def books_authors_create_many(requests):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    BookFormSet = formset_factory(BookForm, extra=2)
    if requests.method == 'POST':
        author_formset = AuthorFormSet(requests.POST, requests.FILES, prefix='authors')
        book_formset = BookFormSet(requests.POST, requests.FILES, prefix='books')
        if author_formset.is_valid() and book_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            for book_form in book_formset:
                book_form.save()
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
        book_formset = BookFormSet(prefix='books')
        context = {
            'author_formset': author_formset,
            'book_formset': book_formset,
        }
        return render(requests, 'main/manage_books_authors.html', context)


def author_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)  # Первым делом, получим класс, который будет создавать наши формы. Обратите внимание на параметр `extra`, в данном случае он равен двум, это значит, что на странице с несколькими формами изначально будет появляться 2 формы создания авторов.
    if request.method == 'POST':  # Наш обработчик будет обрабатывать и GET и POST запросы. POST запрос будет содержать в себе уже заполненные данные формы
        author_formset = AuthorFormSet(request.POST, request.FILES,
                                       prefix='authors')  # Здесь мы заполняем формы формсета теми данными, которые пришли в запросе. Обратите внимание на параметр `prefix`. Мы можем иметь на странице не только несколько форм, но и разных формсетов, этот параметр позволяет их отличать в запросе.
        if author_formset.is_valid():  # Проверяем, валидны ли данные формы
            for author_form in author_formset:
                author_form.save()  # Сохраним каждую форму в формсете
            return HttpResponseRedirect(
                reverse_lazy('p_library:author_list'))  # После чего, переадресуем браузер на список всех авторов.
    else:  # Если обработчик получил GET запрос, значит в ответ нужно просто "нарисовать" формы.
        author_formset = AuthorFormSet(
            prefix='authors')  # Инициализируем формсет и ниже передаём его в контекст шаблона.
    return render(request, 'main/manage_authors.html', {'author_formset': author_formset})


def redaction(requests):
    context = {
        'redaction': PublishingHouse.objects.all(),
    }
    return render(requests, 'main/redactions.html', context)


def index(requests):
    context = {'book': Book.objects.all(),
               'num': range(1, 101),
               }
    return render(requests, 'main/index.html', context)


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')
