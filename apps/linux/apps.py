import os

from django.apps import AppConfig


class LinuxConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.linux"

    def ready(self) -> None:
        print(os.system("waybar"))
