from django import forms


class TraceRoute(forms.Form):
    url = forms.CharField(label='Host URL', max_length=200)