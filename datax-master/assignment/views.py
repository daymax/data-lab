from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required

from .forms import RegistrationFormUniqueEmailWithCaptcha
from .models import Assignment

def index(request):
    assignments = Assignment.objects.order_by('-created_date')
    context = {'assignments': assignments}
    return render(request, 'index.html', context)

@login_required
def search(request):
    keyword = request.GET.get('keyword')
    if keyword:
        assignments = Assignment.objects.filter(title__contains=keyword)
    else:
        assignments = Assignment.objects.all()

    return render(request, 'search.html', {'assignments': assignments})

@login_required
def account(request):
    return render(request, 'my_account.html', {'user': request.user})

# this view is just for demostration...nothing else.
def about(request):
    context = {
        'title': _('about'),
        'content': _('DataX is a project about collecting data for Machine Learning?')
    }
    return render(request, 'about.html', context)

