from django.contrib.sitemaps import Sitemap
from django.urls import reverse, NoReverseMatch


class BlogSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'
    i18n = True 
    
    def items(self):
        from oneapp.models import Blog
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj: Blog) -> str:
        return obj.get_absolute_url()

class ServiceSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 1.0
    protocol = 'https'
    i18n = True 
    
    def items(self):
        from oneapp.models import Service
        return Service.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj: Service) -> str:
        return obj.get_absolute_url()

class StaticSitemap(Sitemap):
    protocol = 'https'
    priority = 0.9
    changefreq = "monthly"
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

