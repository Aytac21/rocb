from modeltranslation.translator import TranslationOptions,register, translator
from oneapp.models import Blog,BlogSection,Service,ServiceSection,Portfolio,PortfolioSection,Testmonial,Tag,Category,Customer,MetaInfo

class MetaTranslationOption(TranslationOptions):
    fields = ('meta_title','meta_description')

translator.register(MetaInfo, MetaTranslationOption)

class BlogTranslationOption(TranslationOptions):
    fields = ('title','description','meta_title','meta_description')

class BlogSectionTranslationOption(TranslationOptions):
    fields = ('title','description')

translator.register(Blog, BlogTranslationOption)
translator.register(BlogSection, BlogSectionTranslationOption)

class ServiceTranslationOption(TranslationOptions):
    fields = ('title','description','meta_title','meta_description')

class ServiceSectionTranslationOption(TranslationOptions):
    fields = ('title','description')

translator.register(Service, ServiceTranslationOption)
translator.register(ServiceSection, ServiceSectionTranslationOption)

class PortfolioTranslationOption(TranslationOptions):
    fields = ('title','description','meta_title','meta_description')

class PortfolioSectionTranslationOption(TranslationOptions):
    fields = ('title','description')

translator.register(Portfolio, PortfolioTranslationOption)
translator.register(PortfolioSection, PortfolioSectionTranslationOption)

class TestimonialTranslationOption(TranslationOptions):
    fields = ('title','description','field')

translator.register(Testmonial,TestimonialTranslationOption)

class CategoryTagTranslationOption(TranslationOptions):
    fields = ('title',)

translator.register(Tag,CategoryTagTranslationOption)
translator.register(Category,CategoryTagTranslationOption)

class CustomerTranslationOption(TranslationOptions):
    fields = ('project','timeline','company')

translator.register(Customer,CustomerTranslationOption)