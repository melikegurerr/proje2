from django.shortcuts import render
from .models import Category, Book
from .forms import SearchForm
from django.http import Http404
from django.shortcuts import redirect

# Anasayfa için view fonksiyonu
def home(request):
    # Tüm kategorileri ve ana sayfada gösterilmesi gereken kitapları getirir
    data = {
        "kategoriler": Category.objects.all(),
        "kitaplar" : Book.objects.filter(anasayfa=True),
    }
    # 'index.html' şablonuna bu verileri render eder
    return render(request, "index.html", data)

# Tüm kitapların listelendiği view fonksiyonu
def books(request):
    # Tüm kategorileri ve tüm kitapları getirir
    data = {
        "kategoriler": Category.objects.all(),
        "kitaplar" : Book.objects.all(),
    }
    # 'books.html' şablonuna bu verileri render eder
    return render(request, "books.html", data)

# Belirli bir kitabın detaylarını gösteren view fonksiyonu
def bookdetails(request, id):
    # Verilen ID'ye göre ilgili kitabı getirir
    data = {
        "book": Book.objects.get(id=id)
    }
    # 'details.html' şablonuna bu kitabı render eder
    return render(request, "details.html", data)

# Kitap arama işlemi için view fonksiyonu
def search_book(request):
    if request.method == 'POST':
        # Formdan gelen verileri alır
        form = SearchForm(request.POST)
        if form.is_valid():
            # Formdan alınan kitap adını alır
            title = form.cleaned_data['kitap_adi']
            
            # Kitap adını içeren ilk kitabı arar
            book = Book.objects.filter(kitap_adi__icontains=title).first()
            if book:
                # Eğer kitap bulunursa, ilgili kitap detaylarına yönlendirir
                return redirect('bookdetails', id=book.id)
            else:
                # Kitap bulunamazsa, arama formu ve hata mesajı ile birlikte sayfayı tekrar render eder
                return render(request, 'search_book.html', {'form': form, 'error': 'Book not found'})
    else:
        # Eğer GET isteği ile gelinmişse boş bir form oluşturur
        form = SearchForm()

    # Arama formunu 'search_book.html' şablonuna render eder
    return render(request, 'search_book.html', {'form': form})

# Belirli bir kategorideki kitapları listeleyen view fonksiyonu
def category_books(request, id):
    try:
        # Verilen ID'ye göre ilgili kategoriyi getirir
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        # Eğer kategori bulunamazsa 404 hatası fırlatır
        raise Http404("Category not found")

    # İlgili kategorideki kitapları getirir
    books = Book.objects.filter(category=category)
    # 'category_books.html' şablonuna bu kategoriyi ve kitapları render eder
    return render(request, 'category_books.html', {
        'category': category,
        'books': books
    })
