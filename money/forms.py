from django import forms
from .models import Account

class OFXUploadForm(forms.Form):
  ofxfile = forms.FileField(label="File")

class AccountModifyForm(forms.ModelForm):
  class Meta:
    model = Account
    fields =  ['account','sortcode', 'name', 'accounttype', 'currency']

  def __init__(self, *args, **kwargs):
    super(AccountModifyForm, self).__init__(*args, **kwargs)
    for field in iter(self.fields):
      self.fields[field].widget.attrs.update({
        'class': 'form-control'
      })
