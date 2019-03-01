from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from .validators import UsernameValidator
from django.core.validators import MinLengthValidator
from social_django.models import UserSocialAuth

import shortuuid

class User(AbstractUser):

    username_validator = UsernameValidator()

    def uuid():
        return 'iw-{}'.format(shortuuid.ShortUUID().random(length=12))

    username = models.CharField(
        _('username'),
        max_length=12,
        unique=True,
        help_text=_('Required. At least 8 characters, at most 12 characters. Letters and digits only.'),
        validators=[username_validator, MinLengthValidator(8)],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    assigned_id = models.CharField(
        _('assigned id'),
        max_length=15,
        unique=True,
        default=uuid
    )

    @property
    def is_social_user(self):
        if UserSocialAuth.objects.filter(user=self):
            return True
        return False

class Assignment(models.Model):
    title = models.CharField(_('title'), max_length=512)
    description = models.TextField(_('description'))
    created_date = models.DateTimeField(_('created date'), auto_now_add=True)
    expire_date = models.DateTimeField(_('expire date'))
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('creator'))
    earning = models.DecimalField(_('earning'), max_digits=11, decimal_places=2, default=0)

    class Meta:
        verbose_name = _('assignment')
        verbose_name_plural = _('assignments')

    def __str__(self):
        return self.title