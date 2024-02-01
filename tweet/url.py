from django.urls import path

from tweet import views

urlpatterns = [
    path('', views.TweetList.as_view()),
    path('<int:pk>/', views.TweetDetails.as_view())
]