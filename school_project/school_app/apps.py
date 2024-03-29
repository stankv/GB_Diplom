from django.apps import AppConfig
from django.dispatch import Signal
from .utilities import send_activation_notification


class SchoolAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'school_app'
    verbose_name = 'Онлайн-школа'


#user_registered = Signal(providing_args=['instance'])    # устарело
user_registered = Signal(['instance'])


def user_registered_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])

user_registered.connect(user_registered_dispatcher)
