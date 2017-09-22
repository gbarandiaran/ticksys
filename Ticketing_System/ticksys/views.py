# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from ticksys.forms import RegistrationForm, ProfielEditForm
from ticksys.models import Ticket
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy


def index(request):
    return render(request, 'ticksys/index.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ticksys/login')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'ticksys/register.html', args)


def warning(request):
    return render(request, 'ticksys/warning.html')


def dashboard(request):
    if request.user.groups.filter(name="TicketingSystem").exists():
        user = request.user
        all_tickets = user.ticket_set.all()
        context = {'all_tickets': all_tickets}
        return render(request, 'ticksys/dashboard.html', context)
    else:
        return render(request, 'ticksys/warning.html')


def profile_edit(request):
    if request.method == 'POST':
        form = ProfielEditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/ticksys/dashboard/')
    else:
        form = ProfielEditForm(instance=request.user)
        args = {'form': form}
        return render(request, 'ticksys/profile_edit.html', args)


class CreateTicket(CreateView):
    model = Ticket
    fields = [
        'title',
        'body',
        'status',
        'author',
        'assignee',
        'created'
    ]

class EditTicket(UpdateView):
    model = Ticket
    fields = [
        'title',
        'body',
        'status',
        'assignee'
    ]

def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'ticksys/ticket_detail.html', {'ticket': ticket})
