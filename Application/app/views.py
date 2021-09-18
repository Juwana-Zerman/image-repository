"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime
from .forms import imageForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


def login(request):
    """Renders the login page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'login.html',
        {
            'title': 'Login',
            'message': 'Your application login page.',
            'year': datetime.now().year,
        }
    )

def img_view(request):
    if request.method == 'POST':
        form = imageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            form = imageForm()
        return render(request, 'index.html', {'form': form})