from django import forms


class TodoItemForm(forms.Form):
    title = forms.CharField(min_length=8, max_length=128)
