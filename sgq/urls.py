from django.urls import path
from .views import SchemaCertificativoListView, SchemaCertificativoDetailView, AuditorListView

urlpatterns = [
    path('schema_certificativo/', SchemaCertificativoListView.as_view(), name='schema_certificativo_list'),
    path('schema_certificativo/<int:pk>/', SchemaCertificativoDetailView.as_view(), name='schema_certificativo_detail'),
    path('auditor_list/', AuditorListView.as_view(), name='auditor_list'),
    
]
