import json

from PyDictionary import PyDictionary

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import Word


def index(request):
    return render(request, 'dictionaries/index.html', {
        'words': Word.objects.all().order_by('id').reverse(),
    })


def search(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')

        return JsonResponse({
            'keyword': keyword,
            'meaning': PyDictionary().meaning(keyword),
            'synonym': PyDictionary().synonym(keyword),
            'antonym': PyDictionary().antonym(keyword),
        })


def new(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')

        try:
            word = Word.objects.get(keyword=keyword)
            return HttpResponse(f'\'{word.keyword }\' is already saved.')
        except Word.DoesNotExist:
            if not PyDictionary().meaning(keyword):
                return HttpResponse(f'\'{keyword}\' is meaningless. Please try again.')

            meaningStr = ''
            noun = PyDictionary().meaning(keyword).get('Noun')
            meaningStr += f'- Noun: {str(noun)[1:-1]}\n' if noun else ''
            meaningStr = meaningStr.replace('\'', '')

            verb = PyDictionary().meaning(keyword).get('Verb')
            meaningStr += f'- Verb: {str(verb)[1:-1]}' if verb else ''
            meaningStr = meaningStr.replace('\'', '')

            synonym = PyDictionary().synonym(keyword)
            synonymStr = str(synonym)[1:-1].replace('\'', '') if synonym else ''

            antonym = PyDictionary().antonym(keyword)
            antonymStr = str(antonym)[1:-1].replace('\'', '') if antonym else ''

            new_word = Word(keyword=keyword, meaning=meaningStr,
                            synonym=synonymStr, antonym=antonymStr)
            new_word.save()

            return HttpResponse('Save successfully.')


def delete(request, id):
    word = get_object_or_404(Word, id=id)
    word.delete()

    return HttpResponse('Delete successfully.')
