from django.forms import ModelForm
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = '__all__'
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.fields['name'].widget.attrs.update(
            {'class':'text-l p-2 my-auto w-full rounded-l-md outline-none','placeholder':'City Name'}
        )
    