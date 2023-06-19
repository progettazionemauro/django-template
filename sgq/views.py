from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import SchemaCertificativo, Auditor

class SchemaCertificativoListView(ListView):
    model = SchemaCertificativo
    template_name = 'schema_certificativo_list.html'

class SchemaCertificativoDetailView(DetailView):
    model = SchemaCertificativo
    template_name = 'schema_certificativo_detail.html'
    
class AuditorListView(ListView):
    model=Auditor
    template_name='auditor_list.html'