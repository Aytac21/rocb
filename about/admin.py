from django.contrib import admin
from .models import About, AboutSection, MiniTitle, Image, Tag, BlockQuote

# Register your models here.
admin.site.register(About)
admin.site.register(AboutSection)
admin.site.register(MiniTitle)
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(BlockQuote)
