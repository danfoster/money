from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .forms import OFXUploadForm, AccountModifyForm

from .utils import parseofx

def index(request):
  template = loader.get_template('money/index.html')
  accounts = Account.objects.all()
  context = RequestContext(request, {
    'accounts': accounts
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
        [newaccounts,newtransactions,skippedtransactions] = parseofx(request.FILES['ofxfile'])
          
        # create account forms 
        accountforms = []
        for account in newaccounts:
          accountforms.append(AccountModifyForm(instance=account))
          
        return render(request, 'money/upload_done.html', {'newaccounts': newaccounts,
                                                             'newtransactions': newtransactions,
                                                             'skippedtransactions': skippedtransactions})

  # if a GET (or any other method) we'll create a blank form
  else:
    form = OFXUploadForm()
  return render(request, 'money/upload.html', {'form': form})
