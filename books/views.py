from django.shortcuts import render

# Create your views here.
# books/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

# 1. READ: Display all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

# 2. CREATE: Add new book details
def book_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        
        Book.objects.create(title=title, author=author, price=price)
        return redirect('book_list')
    return render(request, 'books/book_form.html')

# 3. UPDATE: Modify a book's price
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.price = request.POST.get('price')
        book.save()
        return redirect('book_list')
    return render(request, 'books/book_update.html', {'book': book})

# 4. DELETE: Remove a book record
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})