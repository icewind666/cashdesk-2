#coding: utf-8

import json, datetime, math
from django.shortcuts import render, render_to_response, redirect
from django.views.generic import ListView,DetailView, View
from desk.models import FinancialOperation
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django import template
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from __builtin__ import False
from desk.forms import DocumentForm


class FinancialOperationListView(ListView):
    model = FinancialOperation

    def get_queryset(self):
        queryset = FinancialOperation.objects.order_by('-datetime')
        return queryset
    
    

class FinancialOperationDetailView(DetailView):
    model = FinancialOperation

# used for ajax getting operations
class AllOperationsView(View):
    def post(self, request):
        context = RequestContext(request)
        if request.user.is_authenticated():
            try:
                operations = FinancialOperation.objects.order_by('-datetime')
                context_dict = {}    
                context_dict['operations'] = operations
                context_dict['form'] = DocumentForm()
                return render_to_response('desk/operations.html', context_dict, context)
            except Exception as e:
                print(e.__doc__)
                print(e.message)
                return HttpResponse('error')
        else:
            return HttpResponse('error')

'''
 Checking if user has editors group
'''
class EditorGroupRequiredMixin(object):
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name="editors").exists()))
    def dispatch(self, *args, **kwargs):
        return super(EditorGroupRequiredMixin, self).dispatch(*args, **kwargs)            

'''
 Checking if user is admin(superuser)
'''
class AdminGroupRequiredMixin(object):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(AdminGroupRequiredMixin, self).dispatch(*args, **kwargs)            

'''
Adding spent operation
'''     
def addrecord(request):
    if request.method == 'POST':
        try:
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                print 'we are here'
                filOther = form.cleaned_data['fileLink']
                fileUploaded = request.FILES['fileLink']
                print request.FILES['fileLink']
                amount = request.POST["amount"]
                print amount
                positionNumber = request.POST["positionNumber"];
                print positionNumber
                whoPayed = request.POST["whoPayed"];
                print whoPayed
                alreadyPayed = request.POST["alreadyPayed"];
                print alreadyPayed
                isClosed = False
                
                if amount == alreadyPayed:
                    isClosed = True
                    
                op = FinancialOperation()
                op.amount = amount
                op.positionNumber = positionNumber
                op.isClosed = isClosed
                op.whoPayed = whoPayed
                op.alreadyPayed = alreadyPayed
                op.datetime = datetime.datetime.now()
                op.fileLink = fileUploaded
                
                #print op.toJSON()
                
                op.save()
                
            return HttpResponseRedirect('/');
        except Exception as e:
            print(e.__doc__)
            print(e.message)

