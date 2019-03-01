from django import forms
from django_registration.forms import RegistrationFormUniqueEmail
# from django.contrib.auth.models import User
from .models import User

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible


class RegistrationFormUniqueEmailWithCaptcha(RegistrationFormUniqueEmail):
    captcha = ReCaptchaField()

    class Meta(RegistrationFormUniqueEmail.Meta):
        model = User