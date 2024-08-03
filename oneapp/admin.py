from django.contrib import admin
from .models import MetaInfo,Blog,Service,ServiceSection,BlogSection,Customer,PortfolioSection,Partner,Portfolio,Testmonial,Tag,Category,Message,Subscriber
from modeltranslation.admin import TranslationAdmin,TranslationStackedInline

class BlogModelInline(TranslationStackedInline):  
    model = BlogSection
    extra = 0

    class Media:
        group_fieldsets = True 

        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class BlogAdmin(TranslationAdmin):
    list_display = ("title",)
    inlines = [BlogModelInline]

    class Media:
        group_fieldsets = True 

        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(Blog,BlogAdmin)


class ServiceModelInline(TranslationStackedInline):  
    model = ServiceSection
    extra = 0

    class Media:
        group_fieldsets = True 

        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class ServiceAdmin(TranslationAdmin):
    list_display = ("title",)
    inlines = [ServiceModelInline]

    class Media:
        group_fieldsets = True 

        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(Service,ServiceAdmin)


class CustomerModelInline(TranslationStackedInline):  
    model = Customer
    extra = 0

    class Media:
        group_fieldsets = True 

        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class PortfolioModelInline(TranslationStackedInline):  
    model = PortfolioSection
    extra = 0

    class Media:
        group_fieldsets = True 

        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class PortfolioAdmin(TranslationAdmin):
    list_display = ("title",)
    inlines = [PortfolioModelInline,CustomerModelInline]

    class Media:
        group_fieldsets = True 

        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(Portfolio,PortfolioAdmin)
admin.site.register(Partner)

class TestimonialAdmin(TranslationAdmin):
    list_display = ("title",)

    class Media:
        group_fieldsets = True 

        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(Testmonial,TestimonialAdmin)

class TagCategoryAdmin(TranslationAdmin):
    list_display = ("title",)

    class Media:
        group_fieldsets = True 

        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class MetaInfoAdmin(TranslationAdmin):
    list_display = ("page_name",)

    def has_delete_permission(self, request, obj=None):
        return False

    class Media:
        group_fieldsets = True 

        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(Category,TagCategoryAdmin)
admin.site.register(Tag,TagCategoryAdmin)
admin.site.register(Message)
admin.site.register(Subscriber)
admin.site.register(MetaInfo,MetaInfoAdmin)