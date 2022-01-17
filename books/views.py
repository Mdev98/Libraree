from django.shortcuts import render
from .models import Book, BookType, BookList
# Create your views here.

def landing_page(request):
    return render(request, 'books/landing_page.html')

def home_page(request):
    books = Book.objects.all()

    return render(request, 'books/home_page.html', {'books':books})

def book_list(request):
    books = Book.objects.all()

    return render(request, 'books/book_list.html', {'books':books})

def book_detail(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        print(book)
        BookList.objects.create(book=book)
    return render(request, 'books/book_detail.html', {'book':book})

def mylist(request):
    books = BookList.objects.all()
    print(books)

    return render(request, 'books/mylist_page.html', {'books':books})