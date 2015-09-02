# vim: set fileencoding=UTF-8 :
from django.db import models

class Account(models.Model):
  CURRENCIES = (
    ('S', '£'),
  )

  ACCOUNT_TYPES = (
    ('CUR','Current'),
    ('SAV','Savings'),
    ('CR','Credit Card')
  )

  name = models.CharField(max_length=50)
  sortcode = models.CharField(max_length=8)
  account = models.CharField(max_length=8)
  accounttype = models.CharField(max_length=3,verbose_name="Account Type",default='CUR',choices=ACCOUNT_TYPES)
  currency = models.CharField(max_length=1,default='S',choices=CURRENCIES)

  def __unicode__(self):
    return self.name + " " + self.sortcode + " - " + self.account
    

class Transaction(models.Model):
  account = models.ForeignKey(Account)

