from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from django.shortcuts import reverse
from leads.models import Agent
from agents.forms import AgentModelForm
from agents.mixins import OrganizerAndLoginRequiredMixin


class AgentListView(OrganizerAndLoginRequiredMixin, ListView):
    template_name = 'agents/list.html'

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agentes'
        context['subtitle'] = 'Listado de agentes'
        return context


class AgentCreateView(OrganizerAndLoginRequiredMixin, CreateView):
    template_name = 'agents/create.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent_list')

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organization = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agentes'
        context['subtitle'] = 'Registrar nuevo agente'
        return context


class AgentDetailView(OrganizerAndLoginRequiredMixin, DetailView):
    template_name = 'agents/detail.html'
    context_object_name = 'agent'

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agentes'
        return context


class AgentUpdateView(OrganizerAndLoginRequiredMixin, UpdateView):
    template_name = 'agents/update.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent_list')

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agentes'
        context['subtitle'] = 'Editar agente'
        return context


class AgentDeleteView(OrganizerAndLoginRequiredMixin, DeleteView):
    template_name = 'agents/delete.html'
    context_object_name = 'agent'

    def get_success_url(self):
        return reverse('agents:agent_list')

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agentes'
        context['subtitle'] = 'Eliminar agente'
        return context