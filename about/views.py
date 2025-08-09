from django.shortcuts import render, get_object_or_404
from .models import About, Tab


def about_page(request, tab_slug=None):
    tabs = Tab.objects.select_related('about').order_by('order')

    if not tabs.exists():
        return render(request, "about.html", {"tabs": [], "selected_tab": None, "about": None})

    if tab_slug:
        selected_tab = get_object_or_404(
            Tab, slug=tab_slug
        )
    else:
        selected_tab = tabs.first()

    about = selected_tab.about

    sections = about.sections.prefetch_related(
        'mini_titles', 'images', 'block_quotes').all()
    tags = about.tags.all()

    return render(request, "about.html", {
        "tabs": tabs,
        "selected_tab": selected_tab,
        "about": about,
        "sections": sections,
        "tags": tags
    })
