from django import forms

class newForm(forms.Form):
    name = forms.CharField(label='Name', required=True)
    email = forms.EmailField(label='Email', required=True)
    content = forms.CharField(label='Content', required=True,widget=forms.Textarea)