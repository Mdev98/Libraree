from dataclasses import field
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms

# Create your models here.

class BookType(models.Model):
    type_of_book = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.type_of_book}"


class Autor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class PublishingHouse(models.Model):
    name = models.CharField(max_length=100)
    publish_date = models.IntegerField(validators=[MinValueValidator(1800), MaxValueValidator(2022)])

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    pages = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(500)])
    type  = models.ManyToManyField(BookType)
    autor = models.ManyToManyField(Autor) 
    edition = models.ForeignKey(PublishingHouse, null=True, on_delete=models.SET_NULL)
    cover = models.FileField(upload_to='covers/', null=True)

    def types(self):
        return ",".join([str(p) for p in self.type.all()])

    def autors(self):
        return ",".join([str(p) for p in self.autor.all()])


    def __str__(self):
        return f"{self.title}"

class BookList(models.Model):
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book}"

class BookListForm(forms.ModelForm):
    class Meta:
        model = BookList
        fields = '__all__'