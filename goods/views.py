from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

from goods.models import Products
# Create your views here.
def catalog(request, category_slug, page=1):
    
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))
        
    paginator = Paginator(goods, 2)
    current_page = paginator.page(page)
        
        
    context = {
        'title': 'Home - Каталог',
        'goods': current_page, 
        "slug_url": category_slug,
        "current_page": current_page,
        
    }
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
    
    product = Products.objects.get(slug=product_slug)
    
    context = {
        'product': product,
    }
    
    return render(request, 'goods/product.html', context=context)