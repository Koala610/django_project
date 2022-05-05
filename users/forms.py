from django import forms
from users.models import User

class ImageUploadModelForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar')