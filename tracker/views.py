from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum
from django.db.models.functions import TruncMonth

def expense_list(request):
    expenses = Expense.objects.all().order_by('-date')

    # --- Filters ---
    category = request.GET.get('category')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if category and category != "All":
        expenses = expenses.filter(category=category)
    if start_date:
        expenses = expenses.filter(date__gte=start_date)
    if end_date:
        expenses = expenses.filter(date__lte=end_date)

    # --- Summary ---
    total = expenses.aggregate(total=Sum('amount'))['total'] or 0

    summary_by_category = (
        expenses.values('category')
        .annotate(total=Sum('amount'))
        .order_by('-total')
    )

    summary_by_month = (
        expenses.annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(total=Sum('amount'))
        .order_by('month')
    )

    # Categories for filter dropdown
    categories = Expense.objects.values_list('category', flat=True).distinct()
    categories = ["All"] + list(categories)

    context = {
        'expenses': expenses,
        'total': total,
        'summary_by_category': summary_by_category,
        'summary_by_month': summary_by_month,
        'categories': categories,
        'selected_category': category or "All",
        'start_date': start_date or "",
        'end_date': end_date or ""
    }
    return render(request, 'tracker/expense_list.html', context)


def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'tracker/expense_form.html', {'form': form})


def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'tracker/expense_form.html', {'form': form})


def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'tracker/expense_confirm_delete.html', {'expense': expense})
