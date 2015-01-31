from django.contrib import admin
from django.db import models


class EmailSubscription(models.Model):
    email = models.EmailField(unique=True)
    ip = models.IPAddressField()

    def __unicode__(self):
        return self.email

admin.site.register(EmailSubscription)
