from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'date', 'note', 'category']
        widgets = {
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter amount',
                'step': '0.01'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'note': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Add a note (optional)'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
        labels = {
            'amount': 'Amount (₹)',
            'date': 'Date',
            'note': 'Note',
            'category': 'Category'
        }
