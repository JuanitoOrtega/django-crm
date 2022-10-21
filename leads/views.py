from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Lead
from .forms import LeadModelForm


class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('login')


class LeadListView(ListView):
    template_name = 'leads/list.html'
    queryset = Lead.objects.all().order_by('-id')
    context_object_name = 'leads'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Leads'
        context['subtitle'] = 'Listado de leads'
        return context


# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {
#         'leads': leads,
#         'subtitle': 'Leads',
#     }
#     return render(request, 'leads/list.html', context)


class LeadDetailView(DetailView):
    template_name = 'leads/detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'


# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {
#         'lead': lead,
#         'title': 'Lead'
#     }
#     return render(request, 'leads/detail.html', context)


class LeadCreateView(CreateView):
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


# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == 'POST':
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('leads:lead_list')
#     context = {
#         'form': form,
#         'subtitle': 'Crear nuevo lead',
#     }
#     return render(request, 'leads/create.html', context)


class LeadUpdateView(UpdateView):
    template_name = 'leads/update.html'
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Leads'
        context['subtitle'] = 'Actualizar lead'
        return context


# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)
#     if request.method == 'POST':
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect('leads:lead_list')
#     context = {
#         'form': form,
#         'lead': lead,
#         'subtitle': 'Editar lead',
#     }
#     return render(request, 'leads/update.html', context)


class LeadDeleteView(DeleteView):
    template_name = 'leads/delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Leads'
        context['subtitle'] = 'Eliminar lead'
        return context


# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect('leads:lead_list')