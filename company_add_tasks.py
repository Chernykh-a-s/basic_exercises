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
import operator

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
def generating_departments_salaries(departments):
    departments_salary = {}
    for department in departments:
        department_salaries = []
        for employer in department["employers"]:
            department_salaries.append(employer["salary_rub"])
        departments_salary[department["title"]] = sum(department_salaries)
    return departments_salary


def get_departments_tax_rate(taxes, departments):
    taxes_for_department = {}
    for tax in taxes:
        if tax["department"] is not None:
            taxes_for_department[tax["department"]] = tax["value_percents"] / 100
        else:
            tax_for_all_departments = tax["value_percents"] / 100

    department_taxes = {}
    departments_title = [department["title"] for department in departments]
    tax_titles = [tax for tax in taxes_for_department]

    for department in departments_title:
        tax = []
        if department in tax_titles:
            tax.append(taxes_for_department.get(department))
            tax.append(tax_for_all_departments)
            department_taxes[department] = sum(tax)
        else:
            tax.append(tax_for_all_departments)
            department_taxes[department] = sum(tax)
    return department_taxes


def calculate_department_tax_burden(departments_salary, department_taxes):
    departments_tax_burden = {}
    for department in departments_salary:
        tax_burden = departments_salary.get(department) * department_taxes.get(department)
        departments_tax_burden[department] = tax_burden

    for department, tax_burden in departments_tax_burden.items():
        print(f'По {department} суммарный налог на сотрудников равен {tax_burden}')


# task 14. Вывести список всех сотрудников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
def calculate_employers_salaries(departments):
    tax_of_departments = get_departments_tax_rate(taxes, departments)
    for department in departments:
        for employer in department['employers']:
            employer_tax = employer['salary_rub'] * (tax_of_departments[department["title"]]) / 100
            salary_after_tax = employer['salary_rub'] - employer_tax
            print(f'{employer["first_name"]} {employer["last_name"]}: зарплата после вычета налогов'
                  f' {int(salary_after_tax)}')
            print(f'{employer["first_name"]} {employer["last_name"]}: зарплата до вычета налогов'
                  f' {employer["salary_rub"]}')


# task 16. Вывести список отделов, отсортированный по месячной налоговой нагрузке.
def output_departments_name_by_total_taxes(departments_salary, department_taxes):
    departments_total_taxes = {}
    for department in departments_salary:
        tax_burden = departments_salary.get(department) * department_taxes.get(department)
        departments_total_taxes[department] = tax_burden

    sorted_departments_total_taxes = dict(sorted(departments_total_taxes.items(), key=lambda item: item[1],
                                                 reverse=True))
    departments_names_by_total_taxes = [department_name for department_name in sorted_departments_total_taxes]
    for department_name in departments_names_by_total_taxes:
        print(department_name)


# task 17. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
def output_employers_over_option_tax(departments, option_sum_of_tax):
    tax_of_departments = get_departments_tax_rate(taxes, departments)
    for department in departments:
        for employer in department['employers']:
            employer_year_tax = employer['salary_rub'] * 12 * tax_of_departments[department["title"]]
            if employer_year_tax > option_sum_of_tax:
                print(f'За {employer["first_name"]} {employer["last_name"]} компания платит больше '
                        f'{option_sum_of_tax//1000} тысяч налогов в год')


# task 18. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
def get_employer_with_max_tax(departments):
    tax_of_departments = get_departments_tax_rate(taxes, departments)
    employers_taxes_list = []
    for department in departments:
        for employer in department['employers']:
            employers_taxes = {}
            employer_year_tax = employer['salary_rub'] * 12 * tax_of_departments[department["title"]]
            employers_taxes["first_name"] = employer["first_name"]
            employers_taxes["last_name"] = employer["last_name"]
            employers_taxes["year_tax"] = employer_year_tax
            employers_taxes_list.append(employers_taxes)

    sorted_list_of_employers_tax = sorted(employers_taxes_list, key=lambda x: x["year_tax"], reverse=True)

    return sorted_list_of_employers_tax[0]["first_name"], sorted_list_of_employers_tax[0]["last_name"]


if __name__ == "__main__":
    salaries_of_departments = generating_departments_salaries(departments)
    tax_of_departments = get_departments_tax_rate(taxes, departments)
    print(calculate_department_tax_burden(salaries_of_departments, tax_of_departments))  # 13
    print(calculate_employers_salaries(departments))  # 14
    print(output_departments_name_by_total_taxes(salaries_of_departments, tax_of_departments))  # 16
    print(output_employers_over_option_tax(departments, 100000))  # 17
    print(* get_employer_with_max_tax(departments))  # 18
