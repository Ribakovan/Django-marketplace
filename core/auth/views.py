from django.shortcuts import render, redirect
from django.views.generic import CreateView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from core.product.models import Product
from .forms import SignUpForm, LoginForm, ProfileUpdateForm, UserUpdateForm
from .models import Profile


class ProfileView(LoginRequiredMixin, View):

    def get(self, request):
        products = Product.objects.filter(created_by=request.user)
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        return render(request, 'auth/profile.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'products': products
        })

    def post(self, request):
        products = Product.objects.filter(created_by=request.user)
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('core:profile')
        return render(request, 'auth/profile.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'products': products
        })


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'auth/signup.html'
    success_url = reverse_lazy('core:shop')

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(
            self.request,
            username=username,
            password=password
        )
        Profile.objects.create(user=user)
        login(request=self.request, user=user)
        return response


class Login(LoginView):
    form_class = LoginForm
    template_name = 'auth/login.html'


class Logout(LogoutView):
    pass


