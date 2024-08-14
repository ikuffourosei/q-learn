from django.shortcuts import render, get_object_or_404, redirect
from quizzes.models import Questions, Topics, Choice, Results
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index(request):
    """Welcome page"""
    return render(request, 'index.html')


def login_check(request):
    """Function that authenticates a user"""



def logout_check(request):
    """Logs out the current user in session"""
    logout(request)
    redirect('index')



@login_required
def view_questions(request, topic_name='sports'):
    """Render quiz questions and choices in HTML template."""
    if topic_name:
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
    if request.user.is_authenticated:
        return render(request, 'quiz.html', result)
    else:
        redirect('index')



@login_required
def submit_quiz(request, topic_name):
    """Submit a quiz and save the results."""
    topic = get_object_or_404(Topics, name=topic_name)
    questions = Questions.objects.filter(topics=topic)
    total_questions = questions.count()
    if request.method == 'POST' and request.user.is_authenticated:
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



@login_required
def result(request, topic_name):
    """Displays results based on user_id
    If user took more than one result, display all

    #example
    Result1: User_1 scored 50% on sports
    Result2: User_1 scored 60% om sports
    """
    topic = get_object_or_404(Topics, name=topic_name)
    user = request.user
    results = Results.objects.filter(user=user, topics=topic)

    context = {'results': results}
    return render(request, 'result.html', context)
