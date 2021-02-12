from    django.urls     import  path
from    .               import  views


urlpatterns =   [
    # les urls de l'application home
    path('', views.index, name = 'compte'),
]