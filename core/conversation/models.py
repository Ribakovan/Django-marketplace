from django.db import models
from django.contrib.auth.models import User
from core.product.models import Product


class Conversation(models.Model):
    product = models.ForeignKey(Product, related_name='conversations', on_delete=models.CASCADE, verbose_name='Продукт')
    members = models.ManyToManyField(User, related_name='conversations', verbose_name='Участники')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.product

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Диалог'
        verbose_name_plural = 'Диалоги'


class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE, verbose_name='Диалог')
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    created_by = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE, verbose_name='Дата обновления')

    def __str__(self):
        return self.content

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
