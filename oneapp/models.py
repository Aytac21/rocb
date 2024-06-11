from django.db import models
from django.contrib.auth import get_user, get_user_model
from oneapp.utils import *
from datetime import datetime
from django.urls import reverse

class BaseMixin(models.Model):
    slug = models.SlugField(unique=True,editable=False,blank=True,null=True)
    created_at = models.DateField(auto_now=True,blank=True,null=True,)
    seo_title = models.CharField(max_length=1200,null=True,blank=True,verbose_name='title for seo')
    seo_keyword = models.CharField(max_length=1200,null=True,blank=True,verbose_name='keyword for seo')
    seo_alt = models.CharField(max_length=1200,null=True,blank=True)
    seo_description = models.CharField(max_length=1200,null=True,blank=True,verbose_name='description for seo')
    
    class Meta:
        abstract = True

class Category(BaseMixin):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            new_slug = slugify(self.title)
            self.slug = new_slug
            if Category.objects.filter(slug=new_slug).exists():
                count = 0
                while Category.objects.filter(slug=new_slug).exists():
                    new_slug = f"{slugify(self.title)}-{count}"
                    count += 1
        super(Category, self).save(*args, **kwargs)

class Tag(BaseMixin):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            new_slug = slugify(self.title)
            self.slug = new_slug
            if Tag.objects.filter(slug=new_slug).exists():
                count = 0
                while Tag.objects.filter(slug=new_slug).exists():
                    new_slug = f"{slugify(self.title)}-{count}"
                    count += 1
        super(Tag, self).save(*args, **kwargs)

class Service(BaseMixin):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True,blank=True)
    icon = models.ImageField(null=True,blank=True)
    in_home = models.BooleanField(default=False)

    def __str__(self):
        return f'-{self.title}'

    def get_absolute_url(self):
        return reverse('service', kwargs={"slug": self.slug})


    def save(self, *args, **kwargs):
        if not self.slug:
            new_slug = slugify(self.title)
            self.slug = new_slug
            if Service.objects.filter(slug=new_slug).exists():
                count = 0
                while Service.objects.filter(slug=new_slug).exists():
                    new_slug = f"{slugify(self.title)}-{count}"
                    count += 1
        super(Service, self).save(*args, **kwargs)
    

class ServiceSection(models.Model):
    service = models.ForeignKey(Service,on_delete=models.CASCADE,related_name='service_sections')
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(null=True,blank=True)
    second_image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return f'-{self.title}'
    

class Blog(BaseMixin):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True,related_name='categoryBlogs')
    tag = models.ManyToManyField(Tag,related_name='tagBlogs')
    in_home = models.BooleanField(default=False)

    def __str__(self):
        return f'-{self.title}'

    def get_absolute_url(self):
        return reverse('blog', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            new_slug = slugify(self.title)
            self.slug = new_slug
            if Blog.objects.filter(slug=new_slug).exists():
                count = 0
                while Blog.objects.filter(slug=new_slug).exists():
                    new_slug = f"{slugify(self.title)}-{count}"
                    count += 1
        super(Blog, self).save(*args, **kwargs)

class BlogSection(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_sections')
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return f'-{self.title}'

class Portfolio(BaseMixin):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True,related_name='categoryPortfolios')
    in_home = models.BooleanField(default=False)

    def __str__(self):
        return f'-{self.title}'

    def get_absolute_url(self):
        return reverse('portfolio', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            new_slug = slugify(self.title)
            self.slug = new_slug
            if Portfolio.objects.filter(slug=new_slug).exists():
                count = 0
                while Portfolio.objects.filter(slug=new_slug).exists():
                    new_slug = f"{slugify(self.title)}-{count}"
                    count += 1
        super(Portfolio, self).save(*args, **kwargs)


class Customer(models.Model):
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE,null=True,blank=True,related_name='customers')
    company = models.CharField(max_length=300,null=True,blank=True)
    project = models.CharField(max_length=300)
    timeline = models.CharField(max_length=300,null=True,blank=True)   

    def __str__(self):
        return f'-{self.project}'        

class PortfolioSection(models.Model):
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE,related_name='portfolio_sections')
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(null=True,blank=True)
    second_image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return f'-{self.title}'

class Partner(models.Model):
    title = models.CharField(max_length=300,null=True,blank=True)
    image = models.ImageField()

    def __str__(self):
        return f'{self.title}'
    
    
class Testmonial(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(null=True,blank=True)
    full_name = models.CharField(max_length=300)
    field = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.title}'
    

class Message(models.Model):
    phone = models.CharField(max_length = 200)
    full_name = models.CharField(max_length = 200)
    subject = models.CharField(max_length = 200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email