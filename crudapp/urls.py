from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import login_view,index

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login_page"),
    path("",views.login_view, name="login"),
    path("index/", views.index, name="home"),
    path("add/", views.add_patient, name="add"),
    path("edit/<int:id>/", views.edit_patient, name="edit"),
    path("delete/<int:id>/", views.delete_patient, name="delete"),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
]