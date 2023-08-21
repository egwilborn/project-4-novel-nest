from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView

from .models import Genre

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    error_message = '' 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Log a user in 
            login(request, user)
            return redirect('login')
        else:
            error_message = 'Invalid sign up'
            
    form = UserCreationForm()
    context = {'form' : form, 'error_message': error_message}
    return render (request, 'registration/signup.html', context)

def addpayment(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    return render (request, 'main_app/creditcard.html', { 'genre': genre})

class GenreList(ListView):
    model = Genre

class GenreDetail(DetailView):
    model = Genre