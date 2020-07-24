from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .models import Song
from .models import Cover

def index(req):
    return render(req, 'index.html', {})


@csrf_protect
@csrf_exempt
def put_picture(req):
    if req.method == 'POST':
        val = req.POST.get('get_name', None)
        song_object = Song.objects.get(name=val)
        cover_object = Cover.objects.filter(songs__name__contains=song_object)
        return JsonResponse({"url": cover_object[0].img.name})
    return render(req, 'index.html', {})
