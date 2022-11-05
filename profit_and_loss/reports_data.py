import datetime

import pandas as pd

from profit_and_loss.models import DepartmentsMonth

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


# def path_and_rename(path):
#     def wrapper(instance, filename):
#         ext = filename.split(".")[-1]
#         # get filename
#         filename = "{}.{}".format(uuid4().hex, ext)
#         # return the whole path to the file
#         return os.path.join(path, filename)
#     return wrapper
#
# file = models.FileField(upload_to=path_and_rename("path/to/upload/"), 'departments.xlsx')

def get_departments_to_dict():
    departments = pd.read_excel('./media/files/departments.xlsx', engine='openpyxl',
                                header=6) # not .xlsx, reading started from line 7, 7th taken as heading
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

DEPARTMENTS = ['X1', 'Основное', 'Сервис', 'Кафе Коцюбинское']




def save_data_by_department():
    # print('departments_to_dict', departments_to_dict)
    updated_departments_to_dict = []
    current_name = ''
    departments_to_dict = get_departments_to_dict()
    for d in departments_to_dict:
        # print('DICTIONARIES', d['Підрозділ'])
        for key, value in d.items():
            # print(key, value)
            if value in DEPARTMENTS:
                # print(value)
                current_name = value
            # print(current_name)
        updated_departments_to_dict.append(d)
        # updated_departments_to_dict[-1]['buyer_category'] = current_buyer
        updated_departments_to_dict[-1]['name'] = current_name
    # print('updated_departments_to_dict', updated_departments_to_dict)
    del departments_to_dict[0]
    del departments_to_dict[0]
    for updated_d in departments_to_dict:
        # print('updated_d', updated_d)
        for key, value in updated_d.items():
            # print('d.items:', key, value, updated_d['name'], updated_d['buyer_category'])
            if key != 'Підрозділ' and key != 'name':
                # print('KEY !=', key, value, updated_d['name'], updated_d['buyer_category'])
                key_date = key.split()
                months_of_report = key_date[0]
                date_of_string = MONTHS[months_of_report] + ' ' + key_date[1]
                key_db = datetime.datetime.strptime(date_of_string, '%B %Y')
                # print('key_db', key_db, value, updated_d['name'], updated_d['Підрозділ'])

                if DepartmentsMonth.objects.filter(name=updated_d['name'], buyer_category=updated_d['Підрозділ'],
                                                   date=key_db).exists():

                    obj = DepartmentsMonth.objects.get(name=updated_d['name'], buyer_category=updated_d['Підрозділ'],
                                                       date=key_db)
                    obj.value = value
                    obj.save()

                else:
                    obj = DepartmentsMonth.objects.create(name=updated_d.get('name'))
                    obj.name = updated_d['name']
                    obj.buyer_category = updated_d['Підрозділ']
                    obj.date = key_db
                    obj.value = value
                    obj.save()


# save_data_by_department()





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
    while line_of_tables_departments < len(departments_to_dict):
        print(line_of_tables_departments, departments_to_dict[line_of_tables_departments])

        line_of_tables_departments += 1


    # print('departments_to_dict', departments_to_dict)
    print('Підрозділ LISTS', departments['Підрозділ'].tolist())  # data from a column and convert it to a list of values

    departments_to_dict_service = next(x for x in departments_to_dict if x["Підрозділ"] == "Сервис")
    departments_to_dict_employee = list(filter(lambda item: item['Підрозділ'] == 'Сотрудники', departments_to_dict))
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

    print('Excel Sheet to Dict:', departments_to_dict[4])  # read the 4th line

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


