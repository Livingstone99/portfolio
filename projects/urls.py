from .import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'project'),
path("<int:pk>/", views.project_detail, name="project_detail"),
]