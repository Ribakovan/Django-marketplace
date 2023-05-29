from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from core.product.models import City


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город', null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars', default='avatar.jpg', verbose_name='Аватар')
    phone_num = models.CharField(max_length=12, blank=True, verbose_name='Номер телефона')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.avatar.path)

        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ('user',)
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
