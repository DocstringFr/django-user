from django.contrib.auth.forms import UserCreationForm

from accounts.models import CustomUser


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "zip_code", )
