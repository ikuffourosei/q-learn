from django.shortcuts import render, get_object_or_404, redirect
from quizzes.models import Questions, Topics, Choice, Results
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from quizzes.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    """Welcome page"""
    return render(request, 'quizzes/home.html')


def register(request):
    """View for user registration"""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
    else:
        form = RegisterForm()
    return render(request, 'quizzes/register.html', {'form': form})


def login_check(request):
    """Function that authenticates a user"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('questions')
    else:
        form = AuthenticationForm()
    return render(request, 'quizzes/login.html', {'form': form})


def logout_check(request):
    """Logs out current user"""
    logout(request)
    return redirect('index')

@login_required
def view_questions(request, topic_name='sports'):
    """Render quiz questions and choices in HTML template."""
    topic = get_object_or_404(Topics, name=topic_name)
    questions = Questions.objects.filter(topics=topic)

    result = {
        'topic_name': topic_name,
        'questions': []
    }

    for question in questions:
        choices = Choice.objects.filter(question=question)
        question_data = {
            'question': question.question_text,
            'choices': [choice.choice_text for choice in choices]
        }
        result['questions'].append(question_data)

    return render(request, 'quizzes/quiz.html', result)


@login_required(login_url='/quiz/login/')
def submit_quiz(request, topic_name):
    """Submit a quiz and save the results."""
    topic = get_object_or_404(Topics, name=topic_name)
    questions = Questions.objects.filter(topics=topic)
    total_questions = questions.count()
    
    if request.method == 'POST':
        score = 0
        for question in questions:
            selected_choice_id = request.POST.get(str(question.id))
            if selected_choice_id:
                selected_choice = Choice.objects.get(id=selected_choice_id)
                if selected_choice.is_correct:
                    score += 1

        scores = (score / total_questions) * 100
        result = Results.objects.create(user=request.user, score=scores, topics=topic)
        result.save()

        return redirect('result', topic_name=topic_name)

    return view_questions(request, topic_name=topic_name)


@login_required(login_url='/quiz/login/')
def result(request, topic_name):
    """Displays results based on user_id"""
    topic = get_object_or_404(Topics, name=topic_name)
    user = request.user
    results = Results.objects.filter(user=user, topics=topic)

    context = {'results': results}
    return render(request, 'quizzes/results.html', context)
