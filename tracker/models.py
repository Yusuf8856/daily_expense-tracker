from django.db import models

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Bills', 'Bills'),
        ('Other', 'Other'),
    ]
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    note = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')

    def __str__(self):
        return f"{self.date} - {self.note} - {self.amount}"
