from django.shortcuts import render
from django.views.generic import View
from core.product.models import Product, Category


class Home(View):

    def get(self, request):
        products = Product.objects.filter(is_sold=False).order_by('-created_at')[:3]
        categories = Category.objects.all()
        return render(request, 'shop/home.html', {
            'products': products,
            'categories': categories
        })



