from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .models import Song


def index(req):
    return render(req, 'index.html', {})


@csrf_protect
@csrf_exempt
def put_picture(req):
    if req.method == 'POST':
        val = req.POST.get('get_name', None)
        tmp = Song.objects.get(name=val).url
        return JsonResponse({"url": tmp})
    return render(req, 'index.html', {})
