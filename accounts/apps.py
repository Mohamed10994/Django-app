from django.apps import AppConfig


class QuickstartConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals
