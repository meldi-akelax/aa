from   django.shortcuts import render
from   store.models  import Section, Texte, Image

# Create your views here.
def index(request):
    sec = Section.objects.filter(page="home")
    try:
        intro = sec[0]
        intro_texte = intro.texte_set.all()[0]
        intro_image = intro.image_set.all()[0]
    except :
        intro = ''

    try:
        quid = sec[1]
        quid_texte = quid.texte_set.all()[0]
        quid_image = quid.image_set.all()[0]
    except :
        quid = '#'

    try:
        pf = sec[2]
        pf_texte = pf.texte_set.all()
        pf_image = pf.image_set.all()[0]
    except :
        quid = '#'
    return render(request, 'home/index.html', locals())