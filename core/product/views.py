from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from core.product.models import City
from .models import Product, Category
from .forms import NewProductForm, EditProductForm
import os


class ProductDetailView(View):

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        print(product)
        is_favourite = False
        if product.favourite.filter(id=request.user.id).exists():
            is_favourite = True
        related_products = Product.objects.filter(category=product.category, is_sold=False).exclude(pk=pk)[:3]
        return render(request, 'product/product.html', {
            'product': product,
            'is_favourite': is_favourite,
            'related_products': related_products
        })


class NewProductView(LoginRequiredMixin, View):

    def get(self, request):
        form = NewProductForm()
        return render(request, 'product/form.html', {
            'form': form,
            'title': 'New Product'
        })

    def post(self, request):
        form = NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.city = request.user.profile.city
            product.save()
            return redirect(reverse_lazy('core:product-detail', kwargs={'pk': product.id}))
        return render(request, 'product/form.html', {
            'form': form,
            'title': 'New product'
        })


class EditProductView(LoginRequiredMixin, View):

    def get(self, request, pk):
        product = Product.objects.get(pk=pk, created_by=request.user)
        form = EditProductForm(instance=product)
        return render(request, 'product/form.html', {
            'form': form,
            'title': 'Edit product'
        })

    def post(self, request, pk):
        product = Product.objects.get(pk=pk, created_by=request.user)
        form = EditProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect(reverse_lazy('core:product-detail', kwargs={'pk': product.id}))
        return render(request, 'product/form.html', {
            'form': form,
            'title': 'Edit product'
        })


class DeleteProduct(LoginRequiredMixin, View):

    def get(self, request, pk):
        item = Product.objects.filter(pk=pk, created_by=request.user)
        item.delete()
        return redirect(reverse_lazy('core:dashboard'))


class Products(View):

    def get(self, request):
        print(request.GET)
        query = request.GET.get('query', '')
        category_id = int(request.GET.get('category_id', 0))
        city_id = int(request.GET.get('city_id', 0))
        categories = Category.objects.all()
        cities = City.objects.all()
        products = Product.objects.filter(is_sold=False)
        user = User.objects.get(id=request.user.id)
        if user:
            favourite_products = user.favourite.all()
            print(favourite_products)
        if query:
            products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
        if city_id:
            products = products.filter(city=city_id)
        if category_id:
            products = products.filter(category=category_id)

        return render(request, 'product/products.html', {
            'products': products,
            'categories': categories,
            'cities': cities,
            'category_id': int(category_id),
            'city_id': int(city_id),
            'query': query,
            'favourite_products': favourite_products
        })


class FavoriteListView(LoginRequiredMixin, View):
    def get(self, request):
        favorite_products = request.user.favourite.all()
        print(favorite_products)
        return render(
            request, 'product/favorite-list.html', {
                'favorite_products': favorite_products
            })


class FavoriteProduct(LoginRequiredMixin, View):

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        if product.favourite.filter(id=request.user.id).exists():
            product.favourite.remove(request.user)
        else:
            product.favourite.add(request.user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

