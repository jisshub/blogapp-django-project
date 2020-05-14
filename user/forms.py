from django import forms
# import User Model
from django.contrib.auth.models import User
# import Usercreationform
from django.contrib.auth.forms import UserCreationForm

# create a new form that inherits the UserCreationForm
class RegisterForm(UserCreationForm):
    # specify the field email
    email = forms.EmailField(required=True)

    # Specify Meta class to configure the form with the user model.
    class Meta: 
        # model to be interacted with form
        model = User
        # form fields
        fields = ['username', 'email', 'password1', 'password2']
