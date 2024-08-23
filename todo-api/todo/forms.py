from django import forms


class TodoForm(forms.Form):
    title = forms.CharField(required=True, max_length=250)
