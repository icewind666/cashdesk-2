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
from django.db.models import F, Q


class Converter(View):
    def get(self, request):
        if request.user.is_authenticated():
            all_operations = FinancialOperation.objects.all()
            for op in all_operations:
                try:
                    op.positionNumberPromSold = str(op.positionNumber)
                    print("Converting {} -> {}".format(op.positionNumberPromSold, op.positionNumber))
                    op.save()
                except Exception as e:
                    pass
            return HttpResponse('all done')


class GlobexView(ListView):
    model = FinancialOperation
    queryset = FinancialOperation.objects.filter(company=0).order_by('-positionNumber')


class RelLccView(ListView):
    template_name = "desk/operations_company_rel.html"
    queryset = FinancialOperation.objects.filter(company=1).order_by('-positionNumber')


class GlobexExportView(ListView):
    template_name = "desk/operations_company_export.html"
    queryset = FinancialOperation.objects.filter(company=2).order_by('-positionNumber')


class PromelectronicaView(ListView):
    template_name = "desk/operations_promelectronica.html"
    queryset = FinancialOperation.objects.filter(company=3).order_by('-positionNumber')


class PromsoldinvoicesView(ListView):
    template_name = "desk/operations_prom_sold_invoices.html"
    sort = {}

    def get_context_data(self, **kwargs):
        context = super(PromsoldinvoicesView, self).get_context_data(**kwargs)

        if "order" in self.request.GET and "field" in self.request.GET:
            sort_order = self.request.GET["order"]
            sort_field = self.request.GET["field"]

            self.sort = {"field": sort_field, "order": sort_order}

            context["field"] = self.sort["field"]
            context["order"] = self.sort["order"]

            if "grouping" in self.request.GET:
                context.update({"field": self.sort["field"],
                                "grouping": self.request.GET["grouping"],
                                "order": self.sort["order"]})
            else:
                context.update({"field": self.sort["field"], "order": self.sort["order"]})

        return context

    def get_queryset(self):
        if "field" in self.request.GET and "order" in self.request.GET:
            sort_order = self.request.GET["order"]
            sort_field = self.request.GET["field"]

            self.sort = {"field": sort_field, "order": sort_order}

            result_sort_order_sign = ""

            # usual sort here
            if sort_order == "asc":
                result_sort_order_sign += ""
            else:
                result_sort_order_sign = "-"

            result_sort_expr = "{}{}".format(result_sort_order_sign, sort_field)

            if sort_field != "alreadyPayed":
                queryset = FinancialOperation.objects.filter(company=4
                                                             ).order_by(result_sort_expr)
            else:
                # custom sort for already payed field
                if "grouping" in self.request.GET:
                    ex_field = self.request.GET["grouping"]
                else:
                    ex_field = "positionNumberPromSold"

                ex_field_sort_expr = "{}".format(ex_field)

                if sort_order == "1":
                    # mode 1: unpayed
                    queryset = FinancialOperation.objects.filter(company=4).filter(
                        alreadyPayed=0.0).order_by(ex_field_sort_expr)

                if sort_order == "2":
                    # mode 2: partically payed
                    queryset = FinancialOperation.objects.filter(company=4).filter(
                        alreadyPayed__gt=0.0).exclude(alreadyPayed=F("amount")).order_by(ex_field_sort_expr)

                if sort_order == "3":
                    # mode 3: payed
                    queryset = FinancialOperation.objects.filter(company=4).filter(
                        alreadyPayed=F("amount")).order_by(ex_field_sort_expr)

        else:
            # unsorted. default sort is by positionNumber
            queryset = FinancialOperation.objects.filter(company=4
                                                         ).order_by('-positionNumberPromSold')
        return queryset


class FinancialOperationListView(ListView):
    queryset = FinancialOperation.objects.filter(company=0).order_by('-positionNumber')


class FinancialOperationDetailView(DetailView):
    model = FinancialOperation


# used for ajax getting operations
class AllOperationsView(View):
    def post(self, request):
        context = RequestContext(request)

        if request.user.is_authenticated():
            try:
                operations = FinancialOperation.objects.filter(company=0).order_by('-positionNumber')
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
                operations = FinancialOperation.objects.filter(company=1).order_by('-positionNumber')
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
                operations = FinancialOperation.objects.filter(company=2).order_by('-positionNumber')
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
                operations = FinancialOperation.objects.filter(company=3).order_by('-positionNumber')
                context_dict = {'operations': operations, 'form': DocumentForm()}
                return render_to_response('desk/operations.html', context_dict, context)
            except Exception as e:
                print(e.__doc__)
                print(e.message)
                return HttpResponse('error')
        else:
            return HttpResponse('error')


class AllOperationsPromSoldInvoicesView(View):
    def post(self, request):
        context = RequestContext(request)
        if request.user.is_authenticated():
            try:
                operations = FinancialOperation.objects.filter(company=4).order_by('-positionNumber')
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

                already_payed = "0.0"
                if "alreadyPayed" in request.POST:
                    if request.POST["alreadyPayed"] != "":
                        already_payed = request.POST["alreadyPayed"]

                company = request.POST["company"]
                is_closed = False

                if amount == already_payed:
                    is_closed = True

                op = FinancialOperation()
                op.amount = amount
                if company == "4":
                    op.positionNumberPromSold = position_number
                    op.positionNumber = 0
                else:
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
                if company == "4":
                    return HttpResponseRedirect('/promsoldinvoices/')

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
                if company == "4":
                    op.positionNumberPromSold = position_number
                    op.positionNumber = 0
                else:
                    op.positionNumber = position_number
                op.isClosed = is_closed
                op.whoPayed = who_payed
                op.alreadyPayed = already_payed

                if file_uploaded != '':
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
                if company == "4":
                    return HttpResponseRedirect('/promsoldinvoices/')

            else:
                print(form.errors)
            return HttpResponseRedirect('/')
        except Exception as e:
            print(e.__doc__)
            print(e.message)
