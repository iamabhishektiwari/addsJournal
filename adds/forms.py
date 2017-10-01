from django import forms
from django.utils.timezone import now

class DocumentForm(forms.Form):
   
    Add_brand    = forms.CharField(label='Type your Brand name or title for your Poster')
    Add_about    = forms.CharField(label='Something which you would like people to read about you or your brand' ,required =False,widget=forms.Textarea)
    docfile      = forms.ImageField(label='Select the poster for display')
    Add_entry_dt = forms.DateTimeField(initial=now(), required=False,label='Current time')


