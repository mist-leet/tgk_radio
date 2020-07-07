from django.shortcuts import render
from django.template import loader

def index(req):
    template = loader.get_template('index.html')
    return render(req, 'index.html', {})
