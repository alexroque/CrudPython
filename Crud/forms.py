from django.forms import ModelForm
from Crud.models import Carro

# Create the form class.
class CarroForm(ModelForm):
     class Meta:
         model = Carro
         fields = ['modelo', 'marca', 'ano']
