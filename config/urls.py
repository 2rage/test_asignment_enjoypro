from django.contrib import admin
from django.urls import path
from quiz import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", views.LoginView.as_view(), name="login"),
    path("quiz/", views.quiz_page, name="quiz_page"),
]
