from django import forms
from charities.models import Charities, User

class CharityForm(forms.ModelForm):
    class Meta:
        model = Charities
        fields = ['name', 'email', 'phone_no', 'address', 'certificates', 'confirmed','image_url','description','full_description']



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'liked_charities']
