# coding: utf-8

import datetime, logging
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView, View
from desk.models import FinancialOperation
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from desk.forms import DocumentForm, EditDocumentForm


class GlobexView(ListView):
    model = FinancialOperation
    queryset = FinancialOperation.objects.filter(company=0).order_by('positionNumber')


class RelLccView(ListView):
    template_name = "desk/operations_company_rel.html"
    queryset = FinancialOperation.objects.filter(company=1).order_by('positionNumber')


class GlobexExportView(ListView):
    template_name = "desk/operations_company_export.html"
    queryset = FinancialOperation.objects.filter(company=2).order_by('positionNumber')


class PromelectronicaView(ListView):
    template_name = "desk/operations_promelectronica.html"
    queryset = FinancialOperation.objects.filter(company=3).order_by('positionNumber')


class FinancialOperationListView(ListView):
    #model = FinancialOperation
    queryset = FinancialOperation.objects.filter(company=0).order_by('positionNumber')


class FinancialOperationDetailView(DetailView):
    model = FinancialOperation


# used for ajax getting operations
class AllOperationsView(View):
    def post(self, request):
        # logger = logging.getLogger(__name__)
        # logger.info("ajax request start")
        context = RequestContext(request)
        if request.user.is_authenticated():
            try:
                operations = FinancialOperation.objects.filter(company=0).order_by('positionNumber')
                context_dict = {'operations': operations, 'form': DocumentForm()}
                return render_to_response('desk/operations.html', context_dict, context)
            except Exception as e:
                print(e.__doc__)
                print(e.message)
                return HttpResponse('error')
        else:
            return HttpResponse('error')


class AllOperationsRelView(View):
    def post(self, request):
        context = RequestContext(request)
        if request.user.is_authenticated():
            try:
                operations = FinancialOperation.objects.filter(company=1).order_by('positionNumber')
                context_dict = {'operations': operations, 'form': DocumentForm()}
                return render_to_response('desk/operations.html', context_dict, context)
            except Exception as e:
                print(e.__doc__)
                print(e.message)
                return HttpResponse('error')
        else:
            return HttpResponse('error')


class AllOperationsExportView(View):
    def post(self, request):
        context = RequestContext(request)
        if request.user.is_authenticated():
            try:
                operations = FinancialOperation.objects.filter(company=2).order_by('positionNumber')
                context_dict = {'operations': operations, 'form': DocumentForm()}
                return render_to_response('desk/operations.html', context_dict, context)
            except Exception as e:
                print(e.__doc__)
                print(e.message)
                return HttpResponse('error')
        else:
            return HttpResponse('error')


class AllOperationsElectroView(View):
    def post(self, request):
        context = RequestContext(request)
        if request.user.is_authenticated():
            try:
                operations = FinancialOperation.objects.filter(company=3).order_by('positionNumber')
                context_dict = {'operations': operations, 'form': DocumentForm()}
                return render_to_response('desk/operations.html', context_dict, context)
            except Exception as e:
                print(e.__doc__)
                print(e.message)
                return HttpResponse('error')
        else:
            return HttpResponse('error')


class EditorGroupRequiredMixin(object):
    """
     Checking if user has editors group
    """
    @method_decorator(user_passes_test(lambda u: u.groups.filter(name="editors").exists()))
    def dispatch(self, *args, **kwargs):
        return super(EditorGroupRequiredMixin, self).dispatch(*args, **kwargs)            


class AdminGroupRequiredMixin(object):
    """
     Checking if user is admin(superuser)
    """
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(AdminGroupRequiredMixin, self).dispatch(*args, **kwargs)            


def addrecord(request):
    """
    Adding spent operation
    """
    if request.method == 'POST':
        try:
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():

                file_uploaded = request.FILES['fileLink']
                amount = request.POST["amount"]
                position_number = request.POST["positionNumber"]
                who_payed = request.POST["whoPayed"]
                already_payed = request.POST["alreadyPayed"]
                company = request.POST["company"]
                is_closed = False
                
                if amount == already_payed:
                    is_closed = True
                    
                op = FinancialOperation()
                op.amount = amount
                op.positionNumber = position_number
                op.isClosed = is_closed
                op.whoPayed = who_payed
                op.alreadyPayed = already_payed
                op.datetime = datetime.datetime.now()
                op.fileLink = file_uploaded
                op.company = company
                op.save()

                if company == "0":
                    return HttpResponseRedirect('/')
                if company == "1":
                    return HttpResponseRedirect('/rel_lcc/')
                if company == "2":
                    return HttpResponseRedirect('/globex_export/')
                if company == "3":
                    return HttpResponseRedirect('/promelectronica/')

            else:
                print('addform is not valid')
            return HttpResponseRedirect('/')

        except Exception as e:
            print(e.__doc__)
            print(e.message)


def edit_operation(request):
    """
    Edit spent operation
    """
    if request.method == 'POST':
        try:
            form = EditDocumentForm(request.POST, request.FILES)

            if form.is_valid():
                file_uploaded = ''
                if 'op_file' in request.FILES:
                    file_uploaded = request.FILES['op_file']

                amount = request.POST["op_amount"].replace(',', '.')
                position_number = request.POST["op_number"]
                who_payed = request.POST["op_payer"]
                already_payed = request.POST["op_alreadypayed"].replace(',', '.')
                op_id = request.POST["op_id"]

                if 'op_close' in request.POST:
                    is_closed = request.POST["op_close"]
                    if is_closed == "on":
                        is_closed = True
                    else:
                        is_closed = False
                else:
                    is_closed = False

                company = request.POST["op_company"]
                op = FinancialOperation.objects.get(id=op_id)
                op.amount = amount
                op.positionNumber = position_number
                op.isClosed = is_closed
                op.whoPayed = who_payed
                op.alreadyPayed = already_payed
                op.fileLink = file_uploaded
                op.company = company
                op.save()

                if company == "0":
                    return HttpResponseRedirect('/')
                if company == "1":
                    return HttpResponseRedirect('/rel_lcc/')
                if company == "2":
                    return HttpResponseRedirect('/globex_export/')
                if company == "3":
                    return HttpResponseRedirect('/promelectronica/')
            else:
                print(form.errors)
            return HttpResponseRedirect('/')
        except Exception as e:
            print(e.__doc__)
            print(e.message)

