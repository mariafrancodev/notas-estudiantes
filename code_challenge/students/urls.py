from django.urls import path

from . import views

app_name = "students"
urlpatterns = [
    path("", views.IndexView.as_view(), name="list"),
    path("create", views.CreateStudentView.as_view(), name="create"),
    path('<pk>/update', views.UpdateStudentView.as_view(), name="update"),
]
