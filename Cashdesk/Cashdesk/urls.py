from django.conf.urls import include, url
from django.contrib import admin
from desk.views import FinancialOperationListView, \
    AllOperationsView, addrecord
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', FinancialOperationListView.as_view(), name='list'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', name='log_in'),
    url(r'^addrecord/$', addrecord, name='addrecord'),
    url(r'^alloperations/$', AllOperationsView.as_view(), name='alloperations'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
