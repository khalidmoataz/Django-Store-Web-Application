from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class myform(forms.Form):
    FullName = forms.CharField(
                widget=forms.TextInput(
                    attrs=
                    {
                    "class":"form-control",
                    "placeholder":"name"
                    }
                    ))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}))
    def checkemail(self):
        email = self.cleaned_data.get("email")
        if not "gmail" in email:
            raise forms.ValidationError("Email must be gmail")
        return email

class loginForm(forms.Form):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={"class":"login_page_input","placeholder": "Username"}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={"class":"login_page_input","placeholder": "Password"}))

class SignUpForm(forms.Form):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={"class":"register_page_input","placeholder": "Username"}))
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={"class":"register_page_input","placeholder": "Email"}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={"class":"register_page_input","placeholder": "Password"}))
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={"class":"register_page_input","placeholder": "Confirm Password"}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        query = User.objects.filter(username=username)
        if query.exists():
            raise forms.ValidationError("Username Is Taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        query = User.objects.filter(email=email)
        if query.exists():
            raise forms.ValidationError("Email is taken")
        return email

    def clean(self):
        thedata = self.cleaned_data.get
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password1:
            raise forms.ValidationError("Passwords Not Match")
        return thedata
