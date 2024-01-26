from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q 
from .models import Product, Category


# Create your views here.
def all_products(request):
    ''' A view to return all products, including sorting and search queries'''

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:  # if category is in the request.GET dictionary
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)  # filter the products by the categories
            categories = Category.objects.filter(name__in=categories)  # filter the categories by the categories

        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)  # Q is a complex query
            products = products.filter(queries)


    context = {
        'products': products,
        'search_term': query,  # this is for the search bar to keep the search term in the search bar
        'current_categories': categories,  # this is for the category filter to keep the category in the search bar
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    ''' A view to show individual product details '''

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
