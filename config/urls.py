from django.contrib import admin
from django.urls import path
from quiz import views

urlpatterns = [
    path('adminmain/', admin.site.urls),

    # Кастомная админка
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('admin-panel/create_user/', views.create_user, name='create_user'),
    path('admin-panel/edit_question/<int:pk>/', views.edit_question, name='edit_question'),
    path('admin-panel/edit_answer/<int:question_pk>/<int:answer_pk>/', views.edit_answer, name='edit_answer'),
    path('admin-panel/statistics/', views.user_statistics, name='user_statistics'),
    path('admin-panel/questions/', views.admin_question_list, name='admin_question_list'),

    path('login/', views.LoginView.as_view(), name='login'),


    path('quiz/', views.quiz_page, name='quiz_page'),
    path('quiz/questions/', views.question_list, name='question_list'),  # Страница выбора вопросов
    path('quiz/questions/<int:pk>/', views.question_detail, name='question_detail'),  # Страница вопроса
    path('quiz/results/', views.quiz_results, name='quiz_results'),  # Страница итогов
]