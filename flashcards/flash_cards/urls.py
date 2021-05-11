from django.urls import path
from. import views


app_name = 'flash_cards'
urlpatterns = [
    path('flash_cards/', views.CardList.as_view()),
    path('collection/', views.CollectionList.as_view()),
    path('flash_cards/<int:pk>/', views.CardList.as_view())
]