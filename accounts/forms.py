from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Profile
from .form_validators import email_validator, phone_validator
from django.core.validators import MinLengthValidator


class SignupForm(UserCreationForm):
    username = forms.CharField(label='로그인에 사용할 아이디', validators=[MinLengthValidator(5), ],
                               help_text='특수문자 및 공백 입력 불가입니다. 최소 5자 이상 입력해주세요.',
                               widget=forms.TextInput(attrs={'pattern':'[a-zA-Z0-9]+'}))
    password1 = forms.CharField(label='비밀번호',
                                help_text='비밀번호는 최소 8자 이상 이어야 합니다. 비밀번호는 전부 숫자로 이루어질 수 없습니다.')
    phone_number=forms.CharField(max_length=15, label='휴대전화 번호',
                                 help_text='친구검색 기능에 활용됩니다. 필수 입력사항입니다.',
                                 validators=[phone_validator, ])
    nickname=forms.CharField(max_length=20, label='닉네임',
                             help_text='친구검색 기능에 활용됩니다. 필수 입력사항입니다. 좌우 공백없이 최소 세 글자 이상 입력해주세요.',
                             validators=[MinLengthValidator(3), ])
    address=forms.CharField(max_length=50, help_text='입력하지 않으셔도 무방합니다.', required=False)
    email=forms.CharField(max_length=50, help_text='입력하지 않으셔도 무방합니다.', required=False,
                          validators=[email_validator, ])


    class Meta(UserCreationForm.Meta):
        fields=UserCreationForm.Meta.fields


    #       validator로 일단 값의 유효성을 검사하고,
    #       clean_xxx 멤버함수로 무결성을 검사한다.(닉네임 중복, 휴대전화 중복 등)
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if(Profile.objects.filter(email=email).exists()):
            raise forms.ValidationError("해당 이메일은 사용중입니다. 다른 이메일을 입력해주세요.")
        return email


    def clean_phone_number(self):
        phone_number=self.cleaned_data.get('phone_number')
        if(Profile.objects.filter(phone_number=phone_number).exists()):
            raise forms.ValidationError("해당 전화번호는 이미 사용중입니다. 전화번호를 확인해주세요.")
        return phone_number


    def clean_nickname(self):
        nickname=self.cleaned_data.get('nickname')
        if(Profile.objects.filter(nickname=nickname).exists()):
            raise forms.ValidationError("해당 닉네임은 이미 사용중입니다. 다른 닉네임을 입력해주세요.")
        return nickname


    def save(self, commit=True):
        user=super().save()
        profile=Profile.objects.create(
            user=user,
            phone_number=self.cleaned_data["phone_number"],
            nickname=self.cleaned_data["nickname"],
            address=self.cleaned_data["address"],
            email=self.cleaned_data["email"]
        )
        return profile


class LoginForm(AuthenticationForm):
    pass