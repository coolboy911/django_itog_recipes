from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class CreateRecipe(forms.Form):
    name = forms.CharField(min_length=2, max_length=50)
    description = forms.CharField(widget=forms.Textarea())
    cooking_steps = forms.CharField(widget=forms.Textarea())
    cooking_time = forms.CharField(min_length=2, max_length=50)
    image = forms.ImageField()
