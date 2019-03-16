from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib.auth.models import User

from twitter import models
from twitter import forms


class TweetListView(View):

    def get(self, request):
        tweets = models.Tweet.objects.all().order_by('-creation_date')
        return render(request, 'twitter/index.html', {'tweets': tweets})


class RegisterView(View):
    form_class = forms.UserRegisterForm
    template_name = 'twitter/register.html'

    def get(self, request):
        return render(request, 'twitter/register.html',
                      {'form': forms.UserRegisterForm()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            return redirect('/')

        return render(request, self.template_name, {'form': form})


class ProfileView(LoginRequiredMixin, View):

    def get(self, request):
        tweets = models.Tweet.objects.filter(
            author=request.user).order_by('-creation_date')
        return render(request, 'twitter/profile.html', {'tweets': tweets})


class ComposeView(LoginRequiredMixin, CreateView):
    model = models.Tweet
    form_class = forms.TweetForm
    success_url = reverse_lazy('twitter:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TweetDetailView(View):

    def get(self, request, pk):
        tweet = models.Tweet.objects.get(pk=pk)
        return render(request, 'twitter/tweet_detail.html', {'tweet': tweet})


class AuthorDetailView(View):

    def get(self, request, pk):
        author = User.objects.get(pk=pk)
        tweets = models.Tweet.objects.filter(
            author=author).order_by('-creation_date')
        return render(request, 'twitter/user_detail.html',
                      {'tweets': tweets, 'author': author})
