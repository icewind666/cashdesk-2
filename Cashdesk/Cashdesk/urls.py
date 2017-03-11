from django.conf.urls import include, url
from django.contrib import admin
from desk.views import FinancialOperationListView, AddSpentView,\
    AllOperationsView, AddIncomeView, ArchiveView

urlpatterns = [
    # Examples:
    # url(r'^$', 'Cashdesk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', FinancialOperationListView.as_view(), name='list'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', name='log_in'),
    url(r'^addspent/$', AddSpentView.as_view(), name='addspent'),
    url(r'^archive/$', ArchiveView.as_view(), name='archive'),
    url(r'^addincome/$', AddIncomeView.as_view(), name='addincome'),
    url(r'^alloperations/$', AllOperationsView.as_view(), name='alloperations'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    
]
