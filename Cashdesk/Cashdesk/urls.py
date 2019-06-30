from django.conf.urls import include, url
from django.contrib import admin
from desk.views import FinancialOperationListView, \
    AllOperationsView, AllOperationsRelView, addrecord, edit_operation, GlobexView, \
    RelLccView, GlobexExportView, PromelectronicaView, AllOperationsExportView,\
    AllOperationsElectroView, PromsoldinvoicesView,AllOperationsPromSoldInvoicesView,Converter,\
    remove_globex_export_op,remove_globex_op, remove_rel_op, remove_promsold_op, remove_promelectronica_op
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', FinancialOperationListView.as_view(), name='list'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', name='log_in'),
    url(r'^addrecord/$', addrecord, name='addrecord'),
    url(r'^edit_operation/$', edit_operation, name='edit_operation'),
    url(r'^globex/$', GlobexView.as_view(), name='GlobexView'),
    url(r'^globex/remove/$', remove_globex_op, name='remove_globex_op'),

    url(r'^rel_lcc/$', RelLccView.as_view(), name='RelLccView'),
    url(r'^rel_lcc/?<sort>$', RelLccView.as_view(), name='RelLccView'),
    url(r'^rel_lcc/remove/$', remove_rel_op, name='remove_rel_op'),

    url(r'^globex_export/$', GlobexExportView.as_view(), name='GlobexExportView'),
    url(r'^globex_export/?<sort>$', PromsoldinvoicesView.as_view(), name='GlobexExportView'),
    url(r'^globex_export/remove/$', remove_globex_export_op, name='remove_globex_export_op'),

    url(r'^promelectronica/$', PromelectronicaView.as_view(), name='PromelectronicaView'),
    url(r'^promelectronica/?<sort>$', PromelectronicaView.as_view(), name='PromelectronicaView'),
    url(r'^promelectronica/remove/$', remove_promelectronica_op, name='remove_promelectronica_op'),

    url(r'^promsoldinvoices/?<sort>$', PromsoldinvoicesView.as_view(), name='PromsoldinvoicesView'),
    url(r'^promsoldinvoices/$', PromsoldinvoicesView.as_view(), name='PromsoldinvoicesView'),
    url(r'^promsoldinvoices/remove/$', remove_promsold_op, name='remove_promsold_op'),

    url(r'^alloperations/$', AllOperationsView.as_view(), name='alloperations'),
    url(r'^alloperations_rel/$', AllOperationsRelView.as_view(), name='alloperations_rel'),
    url(r'^alloperations_export/$', AllOperationsExportView.as_view(), name='alloperations_export'),
    url(r'^alloperations_electro/$', AllOperationsElectroView.as_view(), name='alloperations_electro'),
    url(r'^alloperations_sold/$', AllOperationsPromSoldInvoicesView.as_view(), name='alloperations_sold'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    #url(r'^migrate/$', Converter.as_view(), name='converter'),
    #/globex_export/op_remove/{{op.id}}
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
