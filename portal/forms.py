from django import forms
from portal.models import UserProfile
class UserProfileForm(forms.ModelForm):

    
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'profile_pic', 'ShoppingHistory')


