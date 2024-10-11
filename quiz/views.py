import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.models import User
from .forms import UserCreationForm, QuestionForm, AnswerForm
from .models import Question, Answer, UserAnswer
from django.contrib.auth.decorators import user_passes_test


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.is_superuser:
                return redirect("admin_panel")
            else:
                return redirect("question_list")

        return render(request, "login.html", {"form": form})


@login_required
def quiz_page(request):
    return render(request, "quiz_page.html")


@login_required
def question_list(request):
    if "quiz_id" not in request.session:
        request.session["quiz_id"] = str(uuid.uuid4())

    questions = Question.objects.all()
    answered_questions = request.session.get("answered_questions", [])
    all_answered = all(question.pk in answered_questions for question in questions)

    return render(
        request,
        "question_list.html",
        {
            "questions": questions,
            "answered_questions": answered_questions,
            "all_answered": all_answered,
        },
    )


@login_required
def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if "quiz_id" not in request.session:
        request.session["quiz_id"] = str(uuid.uuid4())

    if request.method == "POST":
        selected_answer_id = request.POST.get("answer")
        if selected_answer_id:
            selected_answer = Answer.objects.get(id=selected_answer_id)

            is_correct = selected_answer.is_correct

            answered_questions = request.session.get("answered_questions", [])
            if pk not in answered_questions:
                UserAnswer.objects.create(
                    user=request.user,
                    question=question,
                    answer=selected_answer,
                    is_correct=is_correct,
                    quiz_id=request.session["quiz_id"],
                )
                answered_questions.append(pk)
                request.session["answered_questions"] = answered_questions

            return redirect("question_list")

    return render(request, "question_detail.html", {"question": question})

@login_required
def quiz_results(request):
    total_questions = Question.objects.count()

    quiz_id = request.session.get("quiz_id")
    correct_answers = UserAnswer.objects.filter(
        user=request.user, quiz_id=quiz_id, is_correct=True
    ).count()

    request.session.flush()

    return render(
        request,
        "quiz_results.html",
        {"total_questions": total_questions, "score": correct_answers},
    )


def admin_required(view_func):
    decorated_view_func = user_passes_test(
        lambda user: user.is_superuser, login_url="/login/"
    )(view_func)
    return decorated_view_func


@admin_required
def admin_panel(request):
    questions = Question.objects.all()
    return render(request, "admin_panel.html", {"questions": questions})


@admin_required
def create_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin_panel")
    else:
        form = UserCreationForm()

    return render(request, "create_user.html", {"form": form})


@admin_required
def admin_question_list(request):
    questions = Question.objects.all()
    return render(request, "admin_question_list.html", {"questions": questions})


@admin_required
def edit_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect("admin_panel")
    else:
        form = QuestionForm(instance=question)

    return render(request, "edit_question.html", {"form": form, "question": question})


@admin_required
def edit_answer(request, question_pk, answer_pk):
    answer = get_object_or_404(Answer, pk=answer_pk, question__pk=question_pk)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            form.save()
            return redirect("edit_question", pk=question_pk)
    else:
        form = AnswerForm(instance=answer)

    return render(request, "edit_answer.html", {"form": form, "answer": answer})


@admin_required
def user_statistics(request):
    users = User.objects.all()
    statistics = []
    for user in users:
        total_answers = UserAnswer.objects.filter(user=user).count()
        correct_answers = UserAnswer.objects.filter(user=user, is_correct=True).count()
        if total_answers > 0:
            correct_percentage = round((correct_answers / total_answers) * 100, 2)
        else:
            correct_percentage = 0
        statistics.append(
            {
                "user": user,
                "total_answers": total_answers,
                "correct_answers": correct_answers,
                "correct_percentage": correct_percentage,
            }
        )

    return render(request, "user_statistics.html", {"statistics": statistics})
