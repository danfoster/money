from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
  template = loader.get_template('money/index.html')
  context = RequestContext(request, {
  })
  return HttpResponse(template.render(context))

def upload(request):
  template = loader.get_template('money/upload.html')
  context = RequestContext(request, {
  })
  return HttpResponse(template.render(context))
