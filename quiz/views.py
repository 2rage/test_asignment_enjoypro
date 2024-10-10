from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Question


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("quiz_page")
        return render(request, "login.html", {"form": form})


@login_required
def quiz_page(request):
    return render(request, "quiz_page.html")


def question_list(request):
    questions = Question.objects.all()
    return render(request, "question_list.html", {"questions": questions})


def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, "question_detail.html", {"question": question})
