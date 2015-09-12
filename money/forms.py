from django import forms
from .models import Account

class OFXUploadForm(forms.Form):
  ofxfile = forms.FileField(label="File")

class AccountModifyForm(forms.ModelForm):
  modelid =  forms.IntegerField(widget=forms.HiddenInput())

  class Meta:
    model = Account
    fields =  ['account','sortcode', 'name', 'accounttype', 'currency']

  def __init__(self, *args, **kwargs):
    super(AccountModifyForm, self).__init__(*args, **kwargs)
    for field in iter(self.fields):
      self.fields[field].widget.attrs.update({
        'class': 'form-control'
      })
    self.initial['modelid'] = self.instance.id
