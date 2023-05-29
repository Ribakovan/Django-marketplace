from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from core.product.models import Product
from .models import Conversation
from .forms import ConversationMessageForm


class NewConversation(LoginRequiredMixin, View):

    def get(self, request, pk):
        form = ConversationMessageForm()
        product = Product.objects.get(id=pk)
        if product.created_by == request.user:
            return redirect('core:dashboard')
        conversations = Conversation.objects.filter(product=product).filter(members__in=[request.user])
        if conversations:
            return redirect('core:conversation-detail', pk=conversations.first().id)
        return render(request, 'conversation/new-conversation.html', {
            'form': form
        })

    def post(self, request, pk):
        product = Product.objects.get(id=pk)
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(product=product)
            conversation.members.add(request.user)
            conversation.members.add(product.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            return redirect('core:product-detail', pk=product.id)
        return render(request, 'conversation/new-conversation.html', {
            'form': form
        })


class ConversationDetail(LoginRequiredMixin, View):

    def get(self, request, pk):
        conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
        form = ConversationMessageForm()
        return render(request, 'conversation/conversation.html', {
            'conversation': conversation,
            'form': form
        })

    def post(self, request, pk):
        conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            conversation.save()
            return redirect('core:conversation-detail', pk=pk)
        return render(request, 'conversation/conversation.html', {
            'conversation': conversation,
            'form': form
        })


class Inbox(LoginRequiredMixin, View):

    def get(self, request):
        conversations = Conversation.objects.filter(members__in=[request.user.id])
        return render(request, 'conversation/inbox.html', {
            'conversations': conversations
        })
