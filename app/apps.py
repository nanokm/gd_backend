from django.apps import AppConfig as AC  # To keep mypy happy


class AppConfig(AC):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"
