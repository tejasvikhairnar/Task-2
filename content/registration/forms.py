from django import forms


class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':"form-control",'id':'name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control",'id':'email'}))
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data('name')

        if name and len(name) < 9:
            self.add_error('name','name should be atleast 9 characters')