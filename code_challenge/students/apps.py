from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StudentsConfig(AppConfig):
    name = "code_challenge.students"
    verbose_name = _("Students")

    def ready(self):
        try:
            import code_challenge.users.signals  # noqa F401
        except ImportError:
            pass
