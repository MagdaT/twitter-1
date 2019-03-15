from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from twitter import models
from twitter import forms


class TweetListView(View):

    def get(self, request):
        tweets = models.Tweet.objects.all().order_by('-creation_date')
        return render(request, 'twitter/index.html', {'tweets': tweets})


class RegisterView(View):

    def get(self, request):
        return render(request, 'twitter/register.html',
                      {'form': forms.UserRegisterForm()})


class ProfileView(LoginRequiredMixin, View):

    def get(self, request):
        tweets = models.Tweet.objects.filter(
            author=request.user).order_by('-creation_date')
        return render(request, 'twitter/profile.html', {'tweets': tweets})


class ComposeView(LoginRequiredMixin, CreateView):
    model = models.Tweet
    form_class = forms.TweetForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TweetDetailView(View):

    def get(self, request, pk):
        tweet = models.Tweet.objects.get(pk=pk)
        return render(request, 'twitter/tweet_detail.html', {'tweet': tweet})
