from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.core import validators


class loginModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        labels = {"username": "نام کاربری", "password": "رمز"}
        help_texts = {"username": None}
        widgets = {
            "username": forms.TextInput(
                attrs={"placeholder": "لطفا نام کاربری خود را وارد کنبد"}
            ),
            "password": forms.PasswordInput(
                attrs={"placeholder": "لطفا رمز خود را وارد کنبد"}
            ),
        }


class RegisterModelForm(forms.Form):
    user_name = forms.CharField(
        validators=[validators.MaxLengthValidator(100)],
        widget=forms.TextInput(attrs={'placeholder':'نام کاربری','class':'center pop'}),
        label="نام کاربری",
    )
    password = forms.CharField(
        validators=[
            validators.MaxLengthValidator(100),
        ],
        widget=forms.PasswordInput(attrs={'placeholder':' رمز عبور','class':'center pop'}),
        label="رمز عبور",
    )
    confirm_password = forms.CharField(
        validators=[
            validators.MaxLengthValidator(100),
        ],
        widget=forms.PasswordInput(attrs={'placeholder':'تکرار رمز عبور ','class':'center pop'}),
        label="تکرار رمز عبور",
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password == confirm_password:
            return confirm_password
        raise ValidationError("کلمه عبور و تکرار کلمه عبور مغایرت دارند")
