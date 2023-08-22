from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('genres/', views.GenreList.as_view(), name='genres_index'),
    path('genres/<int:pk>/', views.GenreDetail.as_view(), name='genres_detail'),
    path('genres/<int:genre_id>/payment/', views.addpayment, name='creditcard'),
    path('creditcards/create', views.create_creditcard, name='creditcard_create'),
    path('profile/', views.profile, name='profile'),
    path('genres/<int:genre_id>/creditcards/<int:creditcard_id>', views.assoc_genre, name='assoc_genre'),
]
