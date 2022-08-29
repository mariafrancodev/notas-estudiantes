from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GradesConfig(AppConfig):
    name = "code_challenge.grades"
    verbose_name = _("grades")

    def ready(self):
        try:
            import code_challenge.users.signals  # noqa F401
        except ImportError:
            pass
