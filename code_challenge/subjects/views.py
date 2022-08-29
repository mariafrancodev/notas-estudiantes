# Django
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from .models import Subjects

# Forms
from .forms import SubjectsForm


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Subjects
    template_name = "subjects/subjects_list.html"


class CreateSubjectView(LoginRequiredMixin, generic.CreateView):
    """Create a new subject."""

    template_name = 'subjects/subjects_form.html'
    form_class = SubjectsForm
    success_url = reverse_lazy('subjects:list')


class UpdateSubjectView(LoginRequiredMixin, generic.UpdateView):
    """Update a subject name."""
    model = Subjects
    fields = [
        "name",
    ]
    template_name = 'subjects/subjects_update.html'
    success_url = reverse_lazy('subjects:list')
