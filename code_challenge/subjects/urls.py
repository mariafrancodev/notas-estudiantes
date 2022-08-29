from django.urls import path

from . import views

app_name = "subjects"
urlpatterns = [
    path("", views.IndexView.as_view(), name="list"),
    path("create", views.CreateSubjectView.as_view(), name="create"),
    path('<pk>/update', views.UpdateSubjectView.as_view(), name="update"),
]
