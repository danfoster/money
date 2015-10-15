from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .forms import OFXUploadForm, AccountModifyForm
from .models import Account, Transaction
from ofxparse import OfxParser

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
          ofx = OfxParser.parse(request.FILES['ofxfile'])

         
          newaccounts = []
          newtransactions = []
          skippedtransactions = []
          for account in ofx.accounts:
            # Check that all account exist, if not create them.
            if account.account_type == 'SAVINGS':
              accounttype = 'SAV'
            elif account.account_type == 'CHECKING':
              accounttype = 'CUR'
            else:
              accounttype = 'CUR'
            results = Account.objects.filter(account=account.number,sortcode=account.routing_number)
            if len(results) == 0:
              # No existing account exists, lets create one
              accountmodel = Account(account=account.number,sortcode=account.routing_number,accounttype=accounttype)
              accountmodel.save()
              accountform = AccountModifyForm(instance=accountmodel)
              newaccounts.append(accountform)
            else:
              accountmodel = results[0]

            #Load transactions.  
            for transaction in account.statement.transactions:
              results = Transaction.objects.filter(account=accountmodel,transid=transaction.id)
              if len(results) == 0:
                # No existing transaction exists, lets create one
                transactionmodel = Transaction(account=accountmodel,memo=transaction.memo,payee=transaction.payee,amount=transaction.amount,transtype=transaction.type,transid=transaction.id)
                transactionmodel.save()
                newtransactions.append(transactionmodel)
              else:
                transactionmodel = results[0]
                skippedtransactions.append(transactionmodel)
            
          return render(request, 'money/upload_done.html', {'newaccounts': newaccounts,
                                                            'newtransactions': newtransactions,
                                                            'skippedtransactions': skippedtransactions})

  # if a GET (or any other method) we'll create a blank form
  else:
      form = OFXUploadForm()

  return render(request, 'money/upload.html', {'form': form})
