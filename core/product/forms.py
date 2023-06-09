from django import forms
from .models import Product

INPUT_CLASSES = 'mt-3 w-full py-4 px-6 rounded-xl border'


class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'description', 'price', 'image')

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }


class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'description', 'city', 'price', 'image', 'is_sold')

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'required': False,
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'required': False,
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'required': False,
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'required': False,
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
                'required': False,
            }),
            'city': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'required': False,
            })
        }
