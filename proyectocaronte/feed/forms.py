from django import forms
from .models import User, StatusOfUsers


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['level_name', 'status_of_users_name', 'name', 'passwd', 'email']


class StatusOfUserForm(forms.ModelForm):
    class Meta:
        model = StatusOfUsers
        fields = ['status_of_users_name']
        
