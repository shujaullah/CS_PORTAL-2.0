from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# this class extend the creation fomr class and ask aboit more infom email phone number etc

class RegistrationForm(UserCreationForm):
    UMB_email = forms.EmailField()
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    POSITION_CHOICES = (
    ('ugrad', 'Undergraduate'), ('grad', 'Graduate'), ('alumni', 'Alumni'), ('faculty', 'Faculty'), ('staff', 'Staff'),
    ('crtsy', 'Courtesy'),)
    position = forms.ChoiceField(choices=POSITION_CHOICES, required=True)

    # this class make sure that this user form will save in the users database
    class Meta:
        model = User
        # we are creatinh the fields if dont do that it will not appear on the form.
        fields = ["username", "password1", "password2"]
