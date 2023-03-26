from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'status', 'priority', 'description', 'deadline']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['status'].widget.attrs.update({
            'class': 'form-select'
        })
        self.fields['priority'].widget.attrs.update({
            'class': 'form-select'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'cols': '10',
            'rows': '3',
        })
        self.fields['deadline'].widget.attrs.update({
            'class': 'form-control'
        })
