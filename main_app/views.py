from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView

from .models import Genre, CreditCard
from .forms import CreditCardForm

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
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def addpayment(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    credit_card_form = CreditCardForm()
    try:
        user_credit_card = CreditCard.objects.filter(user=request.user.id)
    except Exception as e:
        user_credit_card = 0
        print(e)

    return render(request, 'main_app/creditcard_form.html', {'genre': genre, 'credit_card_form': credit_card_form, 'user_credit_card': user_credit_card})


class GenreList(ListView):
    model = Genre


class GenreDetail(DetailView):
    model = Genre


def create_creditcard(request):
    form = CreditCardForm(request.POST)
    if form.is_valid():
        new_creditcard = form.save(commit=False)
        new_creditcard.user_id = request.user.id
        new_creditcard.save()
    else:
        return redirect("/")
    return redirect("genres_index")


def profile(request, ):
    credit_card_form = CreditCardForm()
    try:
        user_credit_card = CreditCard.objects.filter(user=request.user.id)
    except Exception as e:
        user_credit_card = 0
        print(e)
    try:
        user_genre = Genre.objects.filter(subscribers=request.user.id)
    except Exception as e:
        user_genre = 0
    return render(request, 'profile.html', {
        'user_credit_card': user_credit_card,
        'user_genre': user_genre,
        'credit_card_form': credit_card_form
    })


def assoc_genre(request, genre_id, creditcard_id):
    creditcard = CreditCard.objects.get(id=creditcard_id)
    creditcard.genres.add(genre_id)
    genre = Genre.objects.get(id=genre_id)
    genre.subscribers.add(request.user.id)
    return redirect('profile')


def genre_remove(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    genre.subscribers.remove(request.user.id)
    creditcard = CreditCard.objects.filter(
        user=request.user.id).get(genres=genre_id)
    creditcard.genres.remove(genre_id)
    return redirect('profile')


def delete_credit_card(request, pk):
    if request.method == "POST":
        # we need to remove the logged in user from all the genres associated with the credit card
        # we find the credit card entry in the db
        credit_card = CreditCard.objects.get(id=pk)
        # we make a list of genre ids
        id_list = credit_card.genres.all().values_list('id')
        credit_card_genres = Genre.objects.filter(id__in=id_list)
        for genre in credit_card_genres:
            genre.subscribers.remove(request.user.id)
        CreditCard.objects.get(id=pk).delete()
        return redirect('profile')
    else:
        object = CreditCard.objects.get(id=pk)
        return render(request, "main_app/creditcard_confirm_delete.html",
                      {'object': object})
