from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Exchange_Room, User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model = Exchange_Room
        fields = '__all__'
        exclude=['host','participants']

class UserForm(ModelForm):
    class Meta:
        model=User
        fields=['avatar','name','username','email','bio']