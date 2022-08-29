# Django
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

#Models
from .models import Students

# Forms
from .forms import StudentForm


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Students
    template_name = "students/students_list.html"


class CreateStudentView(LoginRequiredMixin, generic.CreateView):
    """Create a new student."""

    template_name = 'students/students_form.html'
    form_class = StudentForm
    success_url = reverse_lazy('students:list')


class UpdateStudentView(LoginRequiredMixin, generic.UpdateView):
    """Update a student."""
    model = Students
    fields = [
        "identification_type",
        "identification",
        "name",
        "last_name",
        "phone_number",
    ]
    template_name = 'students/students_update.html'
    success_url = reverse_lazy('students:list')
