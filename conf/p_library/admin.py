from django.contrib import admin
from .models import Book, Author, PublishingHouse, Friend

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

@admin.register(Author)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    pass


@admin.register(Friend)
class AdminFriend(admin.ModelAdmin):
    pass