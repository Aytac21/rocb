from django import forms

from django.contrib.auth.forms import UserCreationForm

class Messageform(forms.ModelForm):

    class Meta:
        from oneapp.models import Message
        model = Message
        fields = ['full_name','subject','email','message','phone']
    
        
    def __init__(self,*args,**kvargs):
        super(Messageform,self).__init__(*args,**kvargs)


class Subscriberform(forms.ModelForm):

    class Meta:
        from oneapp.models import Subscriber
        model = Subscriber
        fields = ['email']
    
        
    def __init__(self,*args,**kvargs):
        super(Subscriberform,self).__init__(*args,**kvargs)