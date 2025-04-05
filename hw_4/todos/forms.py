from django import forms
from .models import Todo

class TodoListForm(forms.Form):
    title= forms.CharField(min_length=5, max_length=200, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder':'Enter category name '
    }))

class TodoCreationForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'status']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class EditProductForm(forms.ModelForm):
    title = forms.CharField(min_length=5, max_length=200, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter category title '
    }))
    description = forms.CharField(min_length=5, max_length=200, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter category description '
    }))
    category_id = forms.CharField(min_length=5, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Select category '
    }))
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'status']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }