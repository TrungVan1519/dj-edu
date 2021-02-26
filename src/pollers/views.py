from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

from .models import Question, Choice


def index(request):
    return render(request, 'pollers/index.html', {
        'questions': Question.objects.all().order_by('id').reverse(),
    })


def vote(request, id):
    question = get_object_or_404(Question, id=id)

    if request.method == 'POST':
        try:
            selected_choice = question.choice_set.get(
                id=request.POST.get('choice'))
            selected_choice.votes += 1
            selected_choice.save()

            return JsonResponse({
                'selected_choice_id': selected_choice.id,
                'selected_choice_text': selected_choice.text,
                'selected_choice_votes': selected_choice.votes,
            })
        except (KeyError, Choice.DoesNotExist):
            return JsonResponse({
                'error_message': "You didn't select a choice. Please try again.",
            })

    return render(request, 'pollers/vote.html', {
        'question': question,
    })
