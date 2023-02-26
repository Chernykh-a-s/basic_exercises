"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
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

for department in departments:
    print(department["title"])

for department in departments:
    for employer in department["employers"]:
        print(employer["first_name"])

for department in departments:
    for employer in department["employers"]:
        print(f'{employer["first_name"]} работает в {department["title"]}')

for department in departments:
    for employer in department["employers"]:
        if employer.get('salary_rub') > 100000:
            print(f'Заработная плата {employer["first_name"]} превышает 100К')

for department in departments:
    for employer in department["employers"]:
        if employer.get('salary_rub') < 80000:
            print(f'Заработная плата {employer["first_name"]} ниже 80К')

for department in departments:
    department_salary = 0
    for employer in department["employers"]:
        department_salary += employer.get('salary_rub')
    print(f'Заработная плата {department["title"]} в месяц составляет {department_salary}')