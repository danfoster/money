from django import forms

class OFXUploadForm(forms.Form):
  ofxfile = forms.FileField(label="File")
