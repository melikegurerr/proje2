from django.shortcuts import render
from .models import Category, Book
from .forms import SearchForm
from django.http import Http404
from django.shortcuts import redirect

def home(request):
    data = {
        "kategoriler": Category.objects.all(),
        "kitaplar" : Book.objects.filter(anasayfa=True),
    }
    return render(request, "index.html", data)

def books(request):
    data = {
        "kategoriler": Category.objects.all(),
        "kitaplar" : Book.objects.all(),
    }
    return render(request, "books.html", data)

def bookdetails(request,id):
    data = {
        "book": Book.objects.get(id=id)
    }
    return render(request, "details.html", data)

def search_book(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['kitap_adi']
            
            book = Book.objects.filter(kitap_adi__icontains=title).first()
            if book:
                return redirect('bookdetails', id=book.id)
            else:
                
                return render(request, 'search_book.html', {'form': form, 'error': 'Book not found'})
    else:
        form = SearchForm()

    return render(request, 'search_book.html', {'form': form})


def category_books(request, id):
    try:
        category = Category.objects.get(id=id)  
    except Category.DoesNotExist:
        raise Http404("Category not found")  

    books = Book.objects.filter(category=category)  
    return render(request, 'category_books.html', {
        'category': category,
        'books': books
    })