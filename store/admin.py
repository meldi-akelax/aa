from django.contrib import admin
from .models        import Section, Texte, Image

# Register your models here.
admin.site.register(Section)
admin.site.register(Texte)
admin.site.register(Image)