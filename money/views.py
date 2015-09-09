from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .forms import OFXUploadForm, AccountModifyForm
from .models import Account

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

          # Check that all account exist, if not create them.
          newaccounts = []
          for account in ofx.accounts:
            if account.account_type == 'SAVINGS':
              accounttype = 'SAV'
            elif account.account_type == 'CHECKING':
              accounttype = 'CUR'
            else:
              accounttype = 'CUR'
            results = Account.objects.filter(account=account.number,sortcode=account.routing_number)
            if len(results) == 0:
              newaccount = Account(account=account.number,sortcode=account.routing_number,accounttype=accounttype)
              accountform = AccountModifyForm(instance=newaccount)
              newaccounts.append(accountform)
              newaccount.save()
          return render(request, 'money/upload_done.html', {'newaccounts': newaccounts })

  # if a GET (or any other method) we'll create a blank form
  else:
      form = OFXUploadForm()

  return render(request, 'money/upload.html', {'form': form})
