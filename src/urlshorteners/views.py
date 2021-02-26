import uuid

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import ShortenedUrl


def index(request):
    return render(request, 'urlshorteners/index.html',  {
        'urls': ShortenedUrl.objects.all().order_by('id').reverse(),
    })


def new(request):
    if request.method == 'POST':
        uid = str(uuid.uuid4())[:5]
        link = request.POST.get('link')

        shortened_url = ShortenedUrl(uuid=uid, link=link)
        shortened_url.save()

        return HttpResponse(uid)


def go(request, uid):
    shortened_url = get_object_or_404(ShortenedUrl, uuid=uid)
    return redirect(shortened_url.link)


def delete(request, id):
    shortened_url = get_object_or_404(ShortenedUrl, id=id)
    shortened_url.delete()

    return HttpResponse('Delete successfully.')
