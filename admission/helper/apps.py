from django.apps import AppConfig


class HelperConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'helper'

    def ready(self) -> None:
        from . import signals
