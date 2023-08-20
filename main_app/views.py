from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    error_message = '' 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
        else:
            error_message = 'Invalid sign up'
            
    form = UserCreationForm()
    context = {'form' : form, 'error_message': error_message}
    return render (request, 'registration/signup.html', context)