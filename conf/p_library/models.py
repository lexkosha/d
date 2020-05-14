from django.db import models


# Create your models here.

class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.full_name






class Friend(models.Model):
    full_name = models.CharField(max_length=150)


class PublishingHouse(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'

    def __str__(self):
        return self.title


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    book_img = models.ImageField(verbose_name='Изображение книги', blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    p_house = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE, blank=True, null=True)
    person = models.ManyToManyField(Friend, through='BetweenFriendBook', through_fields=('book', 'friend'))
    copy_count = models.SmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title


class BetweenFriendBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    dfb = models.ForeignKey(Friend, on_delete=models.CASCADE, related_name='between')
