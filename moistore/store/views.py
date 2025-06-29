# store/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category,CartItem, WishlistItem
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .utils import get_session_key
from .forms import ProductForm

def home(request):
    categories = Category.objects.all()

    movies_category = Category.objects.filter(name__iexact='Movies').first()
    games_category = Category.objects.filter(name__iexact='Games').first()

    movie_products = Product.objects.filter(category=movies_category) if movies_category else []
    game_products = Product.objects.filter(category=games_category) if games_category else []

    return render(request, 'store/home.html', {
        'movie_products': movie_products,
        'game_products': game_products,
        'categories': categories
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

def search(request):
    query = request.GET.get('q', '')
    results = Product.objects.filter(name__icontains=query) if query else []
    return render(request, 'store/search_results.html', {'query': query, 'results': results})

def wishlist(request):
    return HttpResponse("Your wishlist page (to be implemented).")
def cart(request):
    return HttpResponse("Your cart page (to be implemented).")

#@login_required
def cart_view(request):
    session_key = get_session_key(request)
    cart_items = CartItem.objects.filter(session_key=session_key)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})

def add_to_cart(request, product_id):
    session_key = get_session_key(request)
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(session_key=session_key, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')


def wishlist_view(request):
    session_key = get_session_key(request)
    wishlist_items = WishlistItem.objects.filter(session_key=session_key)
    return render(request, 'store/wishlist.html', {'wishlist_items': wishlist_items})

def add_to_wishlist(request, product_id):
    session_key = get_session_key(request)
    product = get_object_or_404(Product, id=product_id)
    WishlistItem.objects.get_or_create(session_key=session_key, product=product)
    return redirect('wishlist')


def contact_view(request):
    return render(request, 'store/contact.html')

def privacy_view(request):
    return render(request, 'store/privacy.html')

def account_view(request):
    return HttpResponse("User account page (coming soon).")


def add_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()

    return render(request, 'store/add_product.html', {'form': form})
