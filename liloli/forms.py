from django import forms
from django.db.utils import IntegrityError

from liloli.models import EmailSubscription
from liloli.utils import ip_from_request


class EmailSubscriptionForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder':'Your Email',
            'class': 'form-control',
        }
    ))

    def save(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        try:
            EmailSubscription.objects.create(
                ip=ip_from_request(self.request),
                email=self.cleaned_data['email'],
            )
        except IntegrityError:
            return False
        return True
