"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:

Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.

13. Вывести список отделов с суммарным налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов с указанием месячной налоговой нагрузки – количеством денег, которые в месяц этот отдел платит налогами.
16. Вывести список отделов, отсортированный по месячной налоговой нагрузке.
17. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
18. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

# task 13. Вывести список отделов с суммарным налогом на сотрудников этого отдела.

tax_departments = {}
for department in departments:
    department_salary = []
    for employer in department['employers']:
        department_salary.append(employer['salary_rub'])
    if department["title"] == 'IT department':
        tax_sum = sum(department_salary) * (taxes[0]["value_percents"] + taxes[1]["value_percents"]) / 100
        tax_departments["department"] = department["title"]
        tax_departments["tax"] = tax_sum
    else:
        tax_sum = sum(department_salary) * (taxes[0]["value_percents"] / 100)
        tax_departments["department"] = department["title"]
        tax_departments["tax"] = tax_sum
    print(f'По {tax_departments["department"]} суммарный налог на сотрудников равен {tax_departments["tax"]}')

# task 14. Вывести список всех сотрудников с указанием зарплаты "на руки" и зарплаты с учётом налогов.

tax_departments = {}
for department in departments:
    for employer in department['employers']:
        if department["title"] == 'IT department':
            employer_tax = employer['salary_rub'] * (taxes[0]["value_percents"] + taxes[1]["value_percents"]) / 100
            salary_after_tax = employer['salary_rub'] - employer_tax
            print(f'{employer["first_name"]} {employer["last_name"]}: зарплата после вычета налогов'
                  f' {int(salary_after_tax)}')
            print(f'{employer["first_name"]} {employer["last_name"]}: зарплата до вычета налогов'
                  f' {employer["salary_rub"]}')
        else:
            employer_tax = employer['salary_rub'] * taxes[0]["value_percents"] / 100
            salary_after_tax = employer['salary_rub'] - employer_tax
            print(f'{employer["first_name"]} {employer["last_name"]}: зарплата после вычета налогов'
                  f' {int(salary_after_tax)}')
            print(f'{employer["first_name"]} {employer["last_name"]}: зарплата до вычета налогов'
                  f' {employer["salary_rub"]}')

# task 16. Вывести список отделов, отсортированный по месячной налоговой нагрузке.

# task 17. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.

# task 18. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
