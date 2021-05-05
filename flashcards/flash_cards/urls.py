from django.urls import path
from. import views


app_name = 'flash_cards'
urlpatterns = [
    path('', views.CardList.as_view())
]