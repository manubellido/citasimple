from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db.models.fields import EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from citasimple.common.models import BaseModel

from .managers import UserManager


class User(AbstractUser):
    """Default user for CitaSimple."""

    email = EmailField(
        unique=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"email": self.email})
