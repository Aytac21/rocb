from django.shortcuts import render
from .models import About, AboutSection, MiniTitle, Image, Tag, BlockQuote

# Create your views here.


def about(request):
    about_instance = About.objects.first()
    about_sections = AboutSection.objects.filter(about=about_instance)
    mini_titles = MiniTitle.objects.filter(aboutsection__in=about_sections)
    images = Image.objects.filter(aboutsection__in=about_sections)
    tags = Tag.objects.filter(about=about_instance)
    block_quotes = BlockQuote.objects.filter(
        aboutsection__about=about_instance)

    context = {
        'about': about_instance,
        'about_sections': about_sections,
        'mini_titles': mini_titles,
        'images': images,
        'tags': tags,
        'block_quotes': block_quotes,
    }
    return render(request, 'about.html', context)
