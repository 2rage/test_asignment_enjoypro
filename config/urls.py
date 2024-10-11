from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.shortcuts import redirect
from quiz import views

urlpatterns = [
    path('', lambda request: redirect('login', permanent=False)),

    path('adminmain/', admin.site.urls),

    # Кастомная админка
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('admin-panel/create_user/', views.create_user, name='create_user'),
    path('admin-panel/edit_question/<int:pk>/', views.edit_question, name='edit_question'),
    path('admin-panel/edit_answer/<int:question_pk>/<int:answer_pk>/', views.edit_answer, name='edit_answer'),
    path('admin-panel/statistics/', views.user_statistics, name='user_statistics'),
    path('admin-panel/questions/', views.admin_question_list, name='admin_question_list'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),


    path('quiz/', views.quiz_page, name='quiz_page'),
    path('quiz/questions/', views.question_list, name='question_list'),
    path('quiz/questions/<int:pk>/', views.question_detail, name='question_detail'),
    path('quiz/results/', views.quiz_results, name='quiz_results'),
]