from django.urls import path

from django.views import generic

app_name = 'twitter'
urlpatterns = [
    path('', generic.TemplateView.as_view(template_name='twitter/index.html'),
         name='index'),
]