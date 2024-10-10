from django.contrib import admin
from django.urls import path
from quiz import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", views.LoginView.as_view(), name="login"),
    path("quiz/", views.quiz_page, name="quiz_page"),
    path(
        "quiz/questions/", views.question_list, name="question_list"
    ),
    path(
        "quiz/questions/<int:pk>/", views.question_detail, name="question_detail"
    ),
]
