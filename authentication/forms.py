from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from authentication.models import Profile


class CustomUserCreationForm(UserCreationForm):
    group = forms.ChoiceField(choices=[(group.pk, group.name) for group in Group.objects.all()])

    class Meta:
        model = Profile
        fields = ('username', 'email', 'password1', 'password2', 'group')
