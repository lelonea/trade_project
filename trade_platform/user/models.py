from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from djmoney.models.fields import MoneyField


class User(AbstractUser):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField("Email", unique=True)
    balance = MoneyField(max_digits=14, decimal_places=2, default=0, default_currency='USD')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", 'password']

    def __str__(self):
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def create_password_send_email(self):
        subject = loader.render_to_string('authentication/confirmation-email.txt')
        subject = ''.join(subject.splitlines())

        body = loader.render_to_string('authentication/confirmation-email.html', {
            'uid': urlsafe_base64_encode(force_bytes(self.pk)),
            'token': default_token_generator.make_token(self),
            'user': self,
        })

        self.email_user(subject, body)
