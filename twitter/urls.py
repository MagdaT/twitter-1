from django.urls import path

from twitter import views

app_name = 'twitter'
urlpatterns = [
    path('', views.TweetListView.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('compose/', views.ComposeView.as_view(), name='compose'),
]