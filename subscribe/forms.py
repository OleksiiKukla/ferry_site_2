from django import forms
from .models import Subscribers

class SubscribeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['destination'].empty_label = 'Choose your destination'

    class Meta:
        model = Subscribers
        fields = '__all__'
