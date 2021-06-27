from django.urls import path

from . import views

app_name = "todo"
urlpatterns = [
    path('', views.TasksListView.as_view(), name="index"),
    path('add', views.TasksCreateView.as_view(), name="add"),
    path('update/<int:pk>', views.TasksUpdateView.as_view(), name="update"),
    path("delete", views.TasksDeleteView.as_view(), name="delete_form"),
    path("delete/<int:pk>", views.TaskDeleteView.as_view(), name="delete"),
]