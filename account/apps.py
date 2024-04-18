from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
    verbose_name = "حساب های کاربری"

    def ready(self):
        from .signals import create_profile
