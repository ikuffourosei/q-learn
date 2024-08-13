from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from quizzes.models import Questions, Topics, Choice


def questions(request, topic_name='sports'):
    """Render quiz questions and choices in HTML template."""
    if topic_name:
        try:
            topic = Topics.objects.get(name=topic_name)
            questions = Questions.objects.filter(topics=topic)
        except Topics.DoesNotExist:
            return render(request, 'error.html', {'message': 'Topic not found'})

    context = {'questions': []}
    for question in questions:
        choices = Choice.objects.filter(question=question)
        question_data = {
            'question': question.question_text,
            'choices': [choice.choice_text for choice in choices]
        }
        context['questions'].append(question_data)
    return JsonResponse(context)


def topics(reqeust):
    """Render all topics, allow user to choose a topic and after choosing, redirect to
    questions url (with desired topic name)
    """
