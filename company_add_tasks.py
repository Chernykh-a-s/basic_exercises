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

def departments_salary(departments):
    departments_salary = {}
    for department in departments:
        salary_lst = []
        for employer in department["employers"]:
            salary_lst.append(employer["salary_rub"])
        departments_salary[department["title"]] = sum(salary_lst)
    return departments_salary


def departments_tax_rate(taxes, departments):
    taxes_for_department = {}

    for tax in taxes:
        taxes_for_department[tax["department"]] = tax["value_percents"] / 100

    taxes_for_department["All"] = taxes_for_department.pop(None)

    department_taxes = {}
    departments_lst = [department["title"] for department in departments]

    for department in departments_lst:
        dep_tax = []
        if True:
            dep_tax.append(taxes_for_department.get(department))
            dep_tax.append(taxes_for_department.get("All"))
            if None in dep_tax:
                dep_tax.remove(None)
            department_taxes[department] = sum(dep_tax)
        else:
            dep_tax.append(tax_dict.get("All"))
            department_taxes[department] = sum(dep_tax)
    return department_taxes


def department_tax_burden(departments_salary, department_taxes):
    for department in departments_salary:
        tax_burden = departments_salary.get(department) * department_taxes.get(department)
        print(f'По {department} суммарный налог на сотрудников равен {tax_burden}')


if __name__ == "__main__":
    dep_sal = departments_salary(departments)
    dep_tax = departments_tax_rate(taxes, departments)
    print(department_tax_burden(dep_sal, dep_tax))

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
