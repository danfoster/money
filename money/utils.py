from ofxparse import OfxParser
from .models import Account, Transaction

def parseofx(ofxfile):
  newaccounts = []
  newtransactions = []
  skippedtransactions = []

  ofx = OfxParser.parse(ofxfile)
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
      newaccounts.append(accountmodel)
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
  return [newaccounts,newtransactions,skippedtransactions]
