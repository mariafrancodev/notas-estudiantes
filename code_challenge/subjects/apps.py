from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SubjectsConfig(AppConfig):
    name = "code_challenge.subjects"
    verbose_name = _("Subjects")

    def ready(self):
        try:
            import code_challenge.users.signals  # noqa F401
        except ImportError:
            pass
