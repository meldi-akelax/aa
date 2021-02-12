from django.shortcuts import render
from texte.models     import Texte, CategorieTexte

# Create your views here.
def index(request):
    intro_texte = Texte.objects.get(pk='1')
    return render(request, 'home/index.html', locals())