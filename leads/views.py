from django.core.mail import send_mail
from django.shortcuts import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from agents.mixins import OrganizerAndLoginRequiredMixin
from .models import Lead
from .forms import LeadModelForm, CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')


class LeadListView(LoginRequiredMixin, ListView):
    template_name = 'leads/list.html'
    context_object_name = 'leads'

    def get_queryset(self):
        user = self.request.user

        # initial queryset of leads for the entire organization
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)
            # filter for the agent that is logged in
            queryset = queryset.filter(agent__user=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Leads'
        context['subtitle'] = 'Listado de leads'
        return context


class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = 'leads/detail.html'
    context_object_name = 'lead'

    def get_queryset(self):
        user = self.request.user

        # initial queryset of leads for the entire organization
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)
            # filter for the agent that is logged in
            queryset = queryset.filter(agent__user=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Leads'
        return context


class LeadCreateView(OrganizerAndLoginRequiredMixin, CreateView):
    template_name = 'leads/create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead_list')

    def form_valid(self, form):
        send_mail(
            subject='A lead has been created',
            message='Go to the site to see the new lead',
            from_email='ceo@creativa.dev',
            recipient_list=['ortegaj83@gmail.com']
        )
        return super(LeadCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Leads'
        context['subtitle'] = 'Crear nuevo lead'
        return context


class LeadUpdateView(OrganizerAndLoginRequiredMixin, UpdateView):
    template_name = 'leads/update.html'
    form_class = LeadModelForm

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)

    def get_success_url(self):
        return reverse('leads:lead_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Leads'
        context['subtitle'] = 'Actualizar lead'
        return context


class LeadDeleteView(OrganizerAndLoginRequiredMixin, DeleteView):
    template_name = 'leads/delete.html'

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)

    def get_success_url(self):
        return reverse('leads:lead_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Leads'
        context['subtitle'] = 'Eliminar lead'
        return context