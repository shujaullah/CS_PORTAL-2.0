from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# this class extend the creation fomr class and ask aboit more infom email phone number etc

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="UMB email")
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
        fields = ["first_name", "last_name", "username", "email", "password1", "password2", "position"]

    def clean_password2(self, *args, **kwargs):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if not password1 == password2:
            raise forms.ValidationError("Both passwords are not same.")
        return password2

    def clean_email(self, *args, **kwargs):
        email1 = self.cleaned_data.get('email')
        substring1 = "@umb.edu"
        if substring1 not in  email1:
            raise forms.ValidationError("Use the UMB email address.")
        return email1
