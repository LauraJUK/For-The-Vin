from wineries.models import InterestedUser
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = InterestedUser
        