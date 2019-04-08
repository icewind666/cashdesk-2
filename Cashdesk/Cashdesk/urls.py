from django.conf.urls import include, url
from django.contrib import admin
from desk.views import FinancialOperationListView, \
    AllOperationsView, AllOperationsRelView, addrecord, edit_operation, GlobexView, \
    RelLccView, GlobexExportView, PromelectronicaView, AllOperationsExportView,\
    AllOperationsElectroView, PromsoldinvoicesView,AllOperationsPromSoldInvoicesView,Converter
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', FinancialOperationListView.as_view(), name='list'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', name='log_in'),
    url(r'^addrecord/$', addrecord, name='addrecord'),
    url(r'^edit_operation/$', edit_operation, name='edit_operation'),
    url(r'^globex/$', GlobexView.as_view(), name='GlobexView'),
    url(r'^rel_lcc/$', RelLccView.as_view(), name='RelLccView'),
    url(r'^globex_export/$', GlobexExportView.as_view(), name='GlobexExportView'),
    url(r'^promelectronica/$', PromelectronicaView.as_view(), name='PromelectronicaView'),
    url(r'^promsoldinvoices/?<sort>$', PromsoldinvoicesView.as_view(), name='PromsoldinvoicesView'),
    url(r'^promsoldinvoices/$', PromsoldinvoicesView.as_view(), name='PromsoldinvoicesView'),
    url(r'^alloperations/$', AllOperationsView.as_view(), name='alloperations'),
    url(r'^alloperations_rel/$', AllOperationsRelView.as_view(), name='alloperations_rel'),
    url(r'^alloperations_export/$', AllOperationsExportView.as_view(), name='alloperations_export'),
    url(r'^alloperations_electro/$', AllOperationsElectroView.as_view(), name='alloperations_electro'),
    url(r'^alloperations_sold/$', AllOperationsPromSoldInvoicesView.as_view(), name='alloperations_sold'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^migrate/$', Converter.as_view(), name='converter'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
