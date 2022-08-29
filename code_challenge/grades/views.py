from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from code_challenge.students.models import Students
from .models import Grades

# Forms
from .forms import GradeForm


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Grades
    template_name = "grades/grades_list.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        student = Students.objects.get(id=self.kwargs["pk"])
        context_data["student"] = student
        return context_data

    def get_queryset(self, *args, **kwargs):
        return Grades.objects.filter(student=self.kwargs["pk"])


class CreateGradeView(LoginRequiredMixin, generic.CreateView):
    """Create a new grade."""
    template_name = "grades/grades_form.html"
    form_class = GradeForm
    success_url = reverse_lazy('grades:list')

    def get_success_url(self):
        return reverse('grades:list', kwargs={'pk': self.kwargs["pk"]})

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        student = Students.objects.get(id=self.kwargs["pk"])
        context_data["student"] = student
        return context_data

    def form_valid(self, form):
        form.instance.student = Students.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)


class UpdateGradesView(LoginRequiredMixin, generic.UpdateView):
    """Update a grade."""
    model = Grades
    fields = [
        "grade",
        "subject",
        "description",
    ]
    template_name = 'grades/grades_update.html'
    success_url = reverse_lazy('grades:list')

    def get_success_url(self):
        grade = self.get_object()
        return reverse('grades:list', kwargs={'pk': grade.student.id})

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        grade = self.get_object()
        context_data["student"] = grade.student
        return context_data
