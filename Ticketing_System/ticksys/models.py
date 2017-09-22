# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.urlresolvers import reverse


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    body = models.CharField(max_length=100)
    status = models.BooleanField(default=1)
    author = models.CharField(max_length=40)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(("Date"), default=datetime.date.today)

    def get_absolute_url(self):
        return reverse('ticksys:ticket_detail', kwargs={'pk': self.id})