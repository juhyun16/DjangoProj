from django import forms
from accounts.form_validators import phone_validator
from django.core.validators import MinLengthValidator
from accounts.models import Profile

class searchForm(forms.Form):
    phone_number=forms.CharField(validators=[phone_validator], label='휴대전화 번호',
                                 max_length=15, required=False)
    nickname = forms.CharField(max_length=20, label='닉네임',
                               validators=[MinLengthValidator(3)], required=False)


    def clean(self):
        self.cleaned_data=super().clean()
        querySet=Profile.objects.all()
        nickname=self.cleaned_data.get('nickname')
        phone_number=self.cleaned_data.get('phone_number')

        #       예외처리 시작.
        #       case 1) 사용자가 아무런 값을 입력하지 않았음
        if ((nickname == '') and (phone_number == '')):
            raise forms.ValidationError("아무런 값을 입력하지 않으셨습니다. 닉네임 또는 폰번호의 값을 입력해 검색해주세요.")

        if nickname != '':
            querySet=querySet.filter(nickname=nickname)
        if phone_number != '':
            querySet=querySet.filter(phone_number=phone_number)

        #       case 2) 사용자가 값을 입력했으나 DB에 없는 값이면...
        if (querySet.count() == 0):
            raise forms.ValidationError("그러한 사용자는 존재하지 않습니다.\n"
                                        "친구의 닉네임 및 폰번호 값을 다시 한번 확인해주세요.")

