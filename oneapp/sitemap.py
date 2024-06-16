from django.contrib.sitemaps import Sitemap
from oneapp.models import *
from django.urls import reverse, NoReverseMatch


class BlogSiteMap(Sitemap):
    changefreq = "daily"
    priority = 0.6
    protocol = 'https'
    i18n = True 
    
    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj: Blog) -> str:
        return obj.get_absolute_url()

class ServiceSiteMap(Sitemap):
    changefreq = "daily"
    priority = 0.6
    protocol = 'https'
    i18n = True 
    
    def items(self):
        return Service.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj: Service) -> str:
        return obj.get_absolute_url()

class StaticSitemap(Sitemap):
    protocol = 'https'
    priority = 0.5
    changefreq = "daily"
    i18n = True 

    def items(self):
        return [
            'home', 'about', 'portfolios',
            'blogs',  'contact',
        ]

    def location(self, item):
        try:
            return reverse(item)
        except NoReverseMatch:
            return reverse('home')

