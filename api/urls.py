from django.urls import path

from . import views

urlpatterns = [
    path("health", views.index, name="index"),
    path("get-emotions", views.get_emotions, name="get_emotions"),
    path("get-irony", views.get_irony, name="get_irony"),
    path("get-sentiment", views.get_sentiment, name="get_sentiment"),
    path("get-bot", views.get_bot, name="get_bot")

]