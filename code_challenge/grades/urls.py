from django.urls import path

from . import views

app_name = "grades"
urlpatterns = [
    path('<pk>/update/', views.UpdateGradesView.as_view(), name="update"),
    path('students/<pk>/', views.IndexView.as_view(), name="list"),
    path('students/<pk>/create/', views.CreateGradeView.as_view(), name="create"),
]
