import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render

from profit_and_loss.forms import ResultForm
from profit_and_loss.models import DepartmentsMonth


def index(request):
    return render(
        request,
        'index.html',
    )


@login_required
def all_statements(request):
    return render(request, 'all_statements.html', {'all_statements': all_statements})


@login_required
def p_and_l(request):
    return render(request, 'profit_and_loss/p_and_l.html', {'p_and_l': p_and_l})


@login_required
def sales_by_customer(request):
    return render(request, 'profit_and_loss/sales_by_customer.html', {'sales_by_customer': sales_by_customer})


# @login_required
# def sales_by_department(request):
#     date = '2022-01-01'
#     departments = DepartmentsMonth.objects.filter(date=date)
#     # departments_a = DepartmentsMonth.objects.filter(date='2022-01-01').exclude(buyer_category='Сотрудники')
#     employees = DepartmentsMonth.objects.filter(date=date, buyer_category='Сотрудники')
#     # employees = DepartmentsMonth.objects.filter(buyer_category='Сотрудники')
#     print('department', departments.values())
#     print('employees', employees.values())
#
#     filter_department = []
#     for department in departments:
#         if department.name == department.buyer_category:
#             for employee in employees:
#                 if employee.name == department.name:
#                     department_value = department.value - employee.value
#                     department.value = department_value
#
#                     print('department_value', department_value)
#             filter_department.append(department)
#
#     print('filter_department', filter_department)
#
#     sum_employees = employees.aggregate(Sum('value'))['value__sum']
#
#     return render(request, 'profit_and_loss/sales_by_department.html', {'departments': filter_department, 'sum_employees': sum_employees, 'date': 'date'})


@login_required
def upload_result(request):
    if request.method == 'POST':
        form = ResultForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = ResultForm
    return render(request, 'profit_and_loss/upload_result.html', {'form': form})


# @login_required
# def upload_sales(request):
#     if request.method == 'POST':
#         form = AllSalesForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/")
#     else:
#         form = ResultForm
#     return render(request, 'profit_and_loss/upload_sales.html', {'form': form})

# @csrf_exempt
@login_required
def sales_by_department(request):
    from_date = request.POST.get('from')
    to_date = request.POST.get('to')
    print('from_date', from_date)
    if request.POST.get('from') and request.POST.get('to'):
        from_date_new = datetime.datetime.strptime(from_date, '%B %Y')
        print("from_date_new", from_date_new)
        to_date_new = datetime.datetime.strptime(to_date, '%B %Y')
    elif request.POST.get('from'):
        from_date_new = datetime.datetime.strptime(from_date, '%B %Y')
        to_date_get = datetime.datetime.now()
        to_date = to_date_get.strftime('%B %Y')
        to_date_new = to_date_get.strftime('%Y-%m-%d')

    else:
        from_date = 'January 2000'
        to_date = 'January 2000'
        from_date_new = datetime.datetime.strptime(from_date, '%B %Y')
        to_date_new = datetime.datetime.strptime(to_date, '%B %Y')
    order = DepartmentsMonth.objects.filter(date__gte=from_date_new, date__lte=to_date_new)
    filter_department = []
    filter_total_sum_dict = {}
    sale_first_list = []
    sale_second_list = []
    filter_sum_employees_dict = {}
    dates = order.dates('date', 'month')
    sale_list = []

    for date in dates:
        departments = DepartmentsMonth.objects.filter(date=date)
        # departments_a = DepartmentsMonth.objects.filter(date='2022-01-01').exclude(buyer_category='Сотрудники')
        employees = DepartmentsMonth.objects.filter(date=date, buyer_category='Сотрудники')
        sum_employees = employees.aggregate(Sum('value'))['value__sum']

        filter_sum_employees_dict[date] = int(sum_employees * 100) / 100

        sum = DepartmentsMonth.objects.filter(date=date)
        total_sum = sum.aggregate(Sum('value'))['value__sum']
        filter_total_sum_dict[date] = int(total_sum / 2 * 100) / 100

        for department in departments:
            if department.name == department.buyer_category:
                for employee in employees:
                    if employee.name == department.name:
                        department_value = department.value - employee.value
                        department.value = department_value

                        if department.name == 'X1':
                            print(department.name, department.value)
                            sale_first_list.append(department)

                        if department.name == 'Основное':
                            print(department.name, department.value)
                            sale_second_list.append(department)

                filter_department.append(department)

    for sale_first in sale_first_list:
        for sale_second in sale_second_list:
            for date in dates:
                if date == sale_first.date and date == sale_second.date:
                    # for employee in employees:
                    # if sale_second.name == sale_second.buyer_category:
                    sale = sale_first.value + sale_second.value
                    print('sale', sale)
                    sale_first.value = int(sale * 100) / 100

        sale_list.append(sale_first)

    department_names = DepartmentsMonth.objects.values('name').distinct()
    today = datetime.datetime.today()
    our_year = today.strftime('%Y')
    print('datetime_now', type(our_year))
    print('filter_total_sum_dict', filter_total_sum_dict)
    print('sale_list', sale_list)

    return render(request, 'profit_and_loss/sales_by_department.html',
                  {'filter_department': filter_department, 'dates': dates, 'department_names': department_names,
                   'filter_sum_employees_dict': filter_sum_employees_dict, 'from_date': from_date, 'to_date': to_date,
                   "our_year": our_year, 'sale_first_list': sale_first_list, 'sale_second_list': sale_second_list,
                   'filter_total_sum_dict': filter_total_sum_dict, 'sale_list': sale_list})
