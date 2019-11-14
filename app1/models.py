from django.db import models

# Create your models here.
class book(models.Model):
    bookid=models.IntegerField(primary_key=True)
    bookname=models.CharField(max_length=35)

    def __str__(self):
        return self.bookname

    class Meta:
        db_table='book'

class author(models.Model):
    authorid=models.IntegerField(primary_key=True)
    author_name=models.CharField(max_length=35)
    books=models.ManyToManyField(book)

    def __str__(self):
        return self.author_name

    class Meta:
        db_table='author'

