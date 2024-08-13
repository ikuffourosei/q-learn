from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from quizzes.models import Questions, Topics, Choice


def questions(request, topic_name='sports'):
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
    print(result)
    return render(request, 'quiz.html', result)



def topics(reqeust):
    """Render all topics, allow user to choose a topic and after choosing, redirect to
    questions url (with desired topic name)
    """
