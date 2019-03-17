from django.urls import path

from twitter import views

app_name = 'twitter'
urlpatterns = [
    path('', views.TweetListView.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('compose/', views.ComposeView.as_view(), name='compose'),
    path('tweet/<int:pk>/', views.TweetDetailView.as_view(),
         name='tweet-detail'),
    path('user/<int:pk>/', views.AuthorDetailView.as_view(),
         name='author-detail'),
    path('messages/', views.MessageListView.as_view(), name='messages'),
    path('messages/new/', views.ComposeMessageView.as_view(),
         name='compose-message'),
]