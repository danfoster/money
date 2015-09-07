from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .forms import OFXUploadForm

from ofxparse import OfxParser

def index(request):
  template = loader.get_template('money/index.html')
  context = RequestContext(request, {
  })
  return HttpResponse(template.render(context))

def upload(request):
  # if this is a POST request we need to process the form data
  if request.method == 'POST':
      # create a form instance and populate it with data from the request:
      form = OFXUploadForm(request.POST, request.FILES)
      # check whether it's valid:
      if form.is_valid():
          # process the data in form.cleaned_data as required
          ofx = OfxParser.parse(request.FILES['ofxfile'])
          for account in ofx.accounts:
            print account.number
          # ...
          # redirect to a new URL:
          return render(request, 'money/upload_done.html', {'output': ofx.account.number })

  # if a GET (or any other method) we'll create a blank form
  else:
      form = OFXUploadForm()

  return render(request, 'money/upload.html', {'form': form})
