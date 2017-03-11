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
class AddSpentView(EditorGroupRequiredMixin, View):
    
    def post(self, request):
        try:
            amount = request.POST["amount"]
            comment = request.POST["comment"];
            op = FinancialOperation()
            op.amount = amount
            op.comment = comment
            op.isSpent = True
            op.datetime = datetime.datetime.now()
            op.save()
            return HttpResponse('ok');
        except Exception as e:
            print(e.__doc__)
            print(e.message)

'''
Adding income operation
'''
class AddIncomeView(EditorGroupRequiredMixin, View):
    def post(self, request):
        try:
            amount = request.POST["amount"]
            comment = request.POST["comment"];
            op = FinancialOperation()
            op.amount = amount
            op.comment = comment
            op.isSpent = False
            op.datetime = datetime.datetime.now()
            op.save()
            return HttpResponse('ok');
        except Exception as e:
            print(e.__doc__)
            print(e.message)

'''
Removing all data and start with previous remainder
'''
class ArchiveView(AdminGroupRequiredMixin, View):
    def post(self, request):
        try:
            print('archiving data...')
            
            # save the remainder
            rem = FinancialOperation.get_remainder()
            print(rem)
            FinancialOperation.objects.all().delete()
            
            # now adding remainder as income if it is >0
            print('records removed. adding remainder')
            finOperation = FinancialOperation()
            finOperation.isSpent = True if rem < 0 else False
            finOperation.amount = math.fabs(rem)
            finOperation.datetime = datetime.datetime.now()
            finOperation.comment = "остаток предыдущего месяца"
            #print(finOperation)
            finOperation.save()
            print('remainder added')
            
            
            
            return HttpResponse('ok');
        except Exception as e:
            print(e.__doc__)
            print(e.message)
            return HttpResponse('ok')
