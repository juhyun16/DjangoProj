import re
from django.forms import ValidationError

EMAIL_REGEX=re.compile(r'[^@]+@[^@]+\.[^@]+$')
PHONE_REGEX=re.compile(r'(\d+)[-](\d+)[-](\d+)$')


def email_validator(email):
    email=email.strip()
    if(len(email) != 0):
        if not EMAIL_REGEX.match(email):
            raise ValidationError("{}는 적절한 이메일 형식이 아닙니다.".format(email))


def phone_validator(phone):
    if not PHONE_REGEX.match(phone):
        raise ValidationError("{}는 적절한 전화번호 형식이 아닙니다.".format(phone))

