from msilib.schema import RadioButton
from tkinter import Button, Radiobutton
from django.forms import ModelForm, TextInput
from form.models import contactFormModel

class ContactForm(ModelForm):
    class Meta:
        model = contactFormModel
        fields = ['username', 'email', 'message','rating1','rating2']
        widgets = {
            'username' : TextInput(attrs= {
                'class' : 'input',
            }),
              'email' : TextInput(attrs= {
                'class' : 'input',
            }),
              'message' : TextInput(attrs= {
                'class' : 'textarea',
            }),
                'rating1' : TextInput(attrs= {
                'class' : 'input',
            }),
                'rating2' : TextInput(attrs= {
                'class' : 'input',
            }),   
        }



