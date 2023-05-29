from django.apps import AppConfig


class ConversationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.conversation'
    label = 'core_conversation'
    verbose_name = 'Сообщения'

