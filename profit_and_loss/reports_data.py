import datetime
import os

import pandas as pd

# from profit_and_loss.models import DepartmentsMonth
from profit_and_loss.models import DepartmentsAllData

MONTHS = {
    'Січень': 'January',
    'Лютий': 'February',
    'Березень': 'March',
    'Квітень': 'April',
    'Травень': 'May',
    'Червень': 'June',
    'Липень': 'July',
    'Серпень': 'August',
    'Вересень': 'September',
    'Жовтень': 'October',
    'Листопад': 'November',
    'Грудень': 'December',
}


def get_departments_to_dict():
    departments = pd.read_excel('./media/files/departments.xlsx', engine='openpyxl',
                                header=6)  # not .xlsx, reading started from line 7, 7th taken as heading
    # engine='openpyxl' - for excel 2003 (xlsx)
    departments_to_dict_nan = pd.DataFrame(departments)
    print('department+s_to_dict_nan', departments_to_dict_nan)
    departments_to_dict_null = departments_to_dict_nan.fillna(0)
    print('ALL departments_to_dict_null', departments_to_dict_null)
    departments_to_dict = departments_to_dict_null.to_dict('records')
    print('DICTIONARIES', departments_to_dict)
    # departments_to_dict_null = pd.DataFrame(departments_to_dict_nan)
    # print('departments_to_dict_null', departments_to_dict_null)
    # departments_to_dict = departments_to_dict_null.fillna(0)
    # print('ALL DICTIONARIES', departments_to_dict)

    return departments_to_dict


def get_all_to_dict():
    departments = pd.read_excel('./media/files/departments.xlsx', engine='openpyxl',
                                header=[6, 7, 8, 9])  # not .xlsx, reading started from line 7, 7th taken as heading
    # engine='openpyxl' - for excel 2003 (xlsx)
    departments_to_dict_nan = pd.DataFrame(departments)
    # print('department+s_to_dict_nan', departments_to_dict_nan)
    departments_to_dict_null = departments_to_dict_nan.fillna(0)
    # print('ALL departments_to_dict_null', departments_to_dict_null)
    departments_to_dict = departments_to_dict_null.to_dict('records')
    # print('DICTIONARIES', departments_to_dict)
    # departments_to_dict_null = pd.DataFrame(departments_to_dict_nan)
    # print('departments_to_dict_null', departments_to_dict_null)
    # departments_to_dict = departments_to_dict_null.fillna(0)
    # print('ALL DICTIONARIES', departments_to_dict)

    return departments_to_dict


DEPARTMENTS = ['X1', 'Основное', 'Сервис', 'Кафе']
PRODUCT = ['КОФЕ', 'СУПУТНІ ТОВАРИ', 'Материалы', 'ДУБЛИ и Старая номенклатура', 'маркетинг', 'МШП',
           'Новые товары в CRM', 'ос_нма', 'Офис ПОСУДА', 'ПРОЧЕЕ ОБОРУДОВАНИЕ', 'РЕМОНТ', 'Служебные', 'УСЛУГИ',
           'я Запчасти', 'я Запчасти (постовые машины)']
CATEGORY_AKM = ['Автоматические и Профмашины', 'АВТОМАТИЧЕСКИЕ КИЕВ', 'КИЕВ']
CATEGORY_RETAIL = ['0', 'Сотрудники', 'РОЗНИЦА']


#
# def save_data_by_department(): #my previous function
#     # print('departments_to_dict', departments_to_dict)
#     updated_departments_to_dict = []
#     current_name = ''
#     departments_to_dict = get_departments_to_dict()
#     print('departments_to_dict 1', departments_to_dict)
#     for d in departments_to_dict:
#         print('DICTIONARIES', d)
#         for key, value in d.items():
#             # print(key, value)
#             if value in DEPARTMENTS:
#                 # print(value)
#                 current_name = value
#             # print(current_name)
#         updated_departments_to_dict.append(d)
#         print('updated_departments_to_dict 1', updated_departments_to_dict)
#         # updated_departments_to_dict[-1]['buyer_category'] = current_buyer
#         updated_departments_to_dict[-1]['name'] = current_name
#     print('updated_departments_to_dict 2', updated_departments_to_dict)
#     print('departments_to_dict 2', departments_to_dict)
#     del departments_to_dict[0]
#     del departments_to_dict[0]
#
#     for updated_d in departments_to_dict:
#         print('updated_d', updated_d)
#         for key, value in updated_d.items():
#             # print('d.items:', key, value, updated_d['name'], updated_d['buyer_category'])
#             if key != 'Підрозділ' and key != 'name':
#                 # print('KEY !=', key, value, updated_d['name'], updated_d['buyer_category'])
#                 key_date = key.split()
#                 months_of_report = key_date[0]
#                 date_of_string = MONTHS[months_of_report] + ' ' + key_date[1]
#                 key_db = datetime.datetime.strptime(date_of_string, '%B %Y')
#                 print('key_db', key_db, value, updated_d['name'], updated_d['Підрозділ'])
#
#                 if DepartmentsMonth.objects.filter(name=updated_d['name'], buyer_category=updated_d['Підрозділ'],
#                                                    date=key_db).exists():
#
#                     obj = DepartmentsMonth.objects.get(name=updated_d['name'], buyer_category=updated_d['Підрозділ'],
#                                                        date=key_db)
#                     obj.value = value
#                     obj.save()
#
#                 else:
#                     obj = DepartmentsMonth.objects.create(name=updated_d.get('name'))
#                     obj.name = updated_d['name']
#                     obj.buyer_category = updated_d['Підрозділ']
#                     obj.date = key_db
#                     obj.value = value
#                     obj.save()


# save_data_by_department()


def form_date(req):
    from_date = req.POST.get('from')
    to_date = req.POST.get('to')
    print('from_date', from_date)
    if req.POST.get('from') and req.POST.get('to'):
        from_date_new = datetime.datetime.strptime(from_date, '%B %Y')
        print("from_date_new", from_date_new)
        to_date_new = datetime.datetime.strptime(to_date, '%B %Y')
    elif req.POST.get('from'):
        from_date_new = datetime.datetime.strptime(from_date, '%B %Y')
        to_date_get = datetime.datetime.now()
        to_date = to_date_get.strftime('%B %Y')
        to_date_new = to_date_get.strftime('%Y-%m-%d')

    else:
        from_date = 'January 2000'
        to_date = 'January 2000'
        from_date_new = datetime.datetime.strptime(from_date, '%B %Y')
        to_date_new = datetime.datetime.strptime(to_date, '%B %Y')

    order = DepartmentsAllData.objects.filter(date__gte=from_date_new, date__lte=to_date_new)
    dates = order.dates('date', 'month')

    return {'dates': dates, 'from_date': from_date, 'to_date': to_date}


def save_all_data():
    updated_departments_to_dict = []
    new_departments_to_dict = []
    current_name = ''
    departments_to_dict = get_all_to_dict()
    for d in departments_to_dict:
        print('d', type(d))
        for key, value in d.items():
            # print('key, value', key, value)
            if value in DEPARTMENTS:
                current_name = value
        updated_departments_to_dict.append(d)
        updated_departments_to_dict[-1]['name'] = current_name
    #
    # print('departments_to_dict', departments_to_dict)
    # print('updated_departments_to_dict', updated_departments_to_dict)

    line_of_tables_departments = 0
    for to_dict in updated_departments_to_dict:
        del to_dict[('Unnamed: 0_level_0', 'Unnamed: 0_level_1', 'Unnamed: 0_level_2', 'Unnamed: 0_level_3')]
        to_dict['buyer_category'] = to_dict.pop(
            ('Підрозділ', 'Покупець (категорії)', 'Unnamed: 1_level_2', 'Unnamed: 1_level_3'))
        new_departments_to_dict.append(to_dict)

    for new_dict in new_departments_to_dict:
        for key, value in list(new_dict.items()):
            if key[3] != 'З ПДВ' and key[3] != 'Од. звітів' and key != 'buyer_category' and key != 'name':
                del new_dict[key]

    for finish_dict in new_departments_to_dict:
        line_of_tables_departments += 1
        print(line_of_tables_departments)
        for key, value in finish_dict.items():
            if key != 'name' and key != 'buyer_category':
                # print('key, value', key[0], value)
                key_date = key[0].split()
                months_of_report = key_date[0]
                date_of_string = MONTHS[months_of_report] + ' ' + key_date[1]
                key_db = datetime.datetime.strptime(date_of_string, '%B %Y')
                product = key[1]

                if DepartmentsAllData.objects.filter(name=finish_dict['name'],
                                                     buyer_category=finish_dict['buyer_category'], product=product,
                                                     date=key_db).exists():
                    obj = DepartmentsAllData.objects.get(name=finish_dict['name'],
                                                         buyer_category=finish_dict['buyer_category'], product=product,
                                                         date=key_db)

                    if key[2] == 'Вартість продажу (грн)':
                        obj.sale_value = value
                        obj.save()

                    elif key[2] == 'Собівартість  (грн)':
                        obj.cost_price = value
                        obj.save()

                    elif key[2] == 'Кількість':
                        obj.cost_price = value
                        obj.save()

                else:
                    obj = DepartmentsAllData.objects.create(product=product)
                    obj.product = product
                    obj.name = finish_dict['name']
                    obj.buyer_category = finish_dict['buyer_category']
                    obj.date = key_db

                    if key[2] == 'Вартість продажу (грн)':
                        obj.sale_value = value
                        obj.save()

                    elif key[2] == 'Собівартість  (грн)':
                        obj.cost_price = value
                        obj.save()

                    elif key[2] == 'Кількість':
                        obj.quantity = value
                        obj.save()


def additional_code():
    upload_date = 'Січень 2022 р.'.split()
    months_of_report = upload_date[0]
    date_of_string = MONTHS[months_of_report] + ' ' + upload_date[1]
    date_of_project = datetime.datetime.strptime(date_of_string, '%B %Y')

    print(date_of_project)
    print(date_of_project.strftime('%B %Y'))

    #  sifted through the table:
    print('ALL DICTIONARIES')
    line_of_tables_departments = 0
    while line_of_tables_departments < len(get_departments_to_dict):
        print(line_of_tables_departments, get_departments_to_dict[line_of_tables_departments])

        line_of_tables_departments += 1

    # print('departments_to_dict', departments_to_dict)
    print('Підрозділ LISTS',
          get_departments_to_dict['Підрозділ'].tolist())  # data from a column and convert it to a list of values

    departments_to_dict_service = next(x for x in get_departments_to_dict if x["Підрозділ"] == "Сервис")
    departments_to_dict_employee = list(filter(lambda item: item['Підрозділ'] == 'Сотрудники', get_departments_to_dict))
    # print(departments)
    print(departments_to_dict_service)
    print(departments_to_dict_employee)

    print("Сервис январь", departments_to_dict_service['Січень 2022 р.'])
    print("Сервис февраль", departments_to_dict_service['Лютий 2022 р.'])
    print("Сервис март", departments_to_dict_service['Березень 2022 р.'])

    d1 = departments_to_dict_employee[0]
    d2 = departments_to_dict_employee[1]
    d1_none = d1['Березень 2022 р.']
    d2_none = d2['Січень 2022 р.']
    print('d1_none', (d1_none))
    print('d2_none', (d2_none))
    print('d2_none + d1_none', (d2_none + d1_none))
    print(type(d1_none))

    print('Excel Sheet to Dict:', get_departments_to_dict[4])  # read the 4th line

# @login_required
# def date_period():
#     url = 'http://127.0.0.1:8233/profit_and_loss/sales_by_department/'
#     data = {
#         'from_date': 'January 2001',
#         'to_date': 'January 2022'
#     }
# reg = requests.get(url, params=data)
# r = requests.post(url, data=data)
# reg.encoding


# print('GET', reg.url)


# print('POST', r)
