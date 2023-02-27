"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела

Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
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

for department in departments:  # task 1
    print(department['title'])

for department in departments:   # task 2
    for employer in department['employers']:
        print(employer['first_name'])

for department in departments:   # task 3
    for employer in department['employers']:
        print(f'{employer["first_name"]} работает в {department["title"]}')

for department in departments:   # task 4
    for employer in department['employers']:
        if employer['salary_rub'] > 100000:
            print(f'Заработная плата {employer["first_name"]} превышает 100К')

for department in departments:   # task 5
    for employer in department['employers']:
        if employer['salary_rub'] < 80000:
            print(f'Заработная плата {employer["position"]} ниже 80К')

for department in departments:   # task 6
    department_salary = 0
    for employer in department['employers']:
        department_salary += employer['salary_rub']
    print(f'Заработная плата {department["title"]} в месяц составляет {department_salary}')

for department in departments:   # task 7
    department_salary = []
    for employer in department['employers']:
        department_salary.append(employer['salary_rub'])
    print(f'Отдел {department["title"]}, минимальная зарплата {sorted(department_salary)[0]}')

for department in departments:  # task 8
    department_salary = []
    avg_salary = 0
    for employer in department['employers']:
        department_salary.append(employer['salary_rub'])
    avg_salary = sum(department_salary) / len(department_salary)
    print(f'Отдел {department["title"]}: минимальная зарплата {sorted(department_salary)[0]}, cредняя зарплата '
          f'{int(avg_salary)}, максимальная зарплата {sorted(department_salary)[-1]}')

avg_salary = 0  # task 9
department_salary = []
for department in departments:
    for employer in department['employers']:
        department_salary.append(employer['salary_rub'])
avg_salary = sum(department_salary) / len(department_salary)
print(f'Средняя зарплата {avg_salary}')

for department in departments:   # task 10
    for employer in department['employers']:
        if employer['salary_rub'] > 90000:
            print(f'{employer["position"]} получает больше 90К')

for department in departments:   # task 11
    avg_girls_salary = 0
    girl_salary = []
    for employer in department['employers']:
        if employer['first_name'] == 'Michelle' or employer['first_name'] == 'Nicole' or employer['first_name'] == \
                'Christina' or employer['first_name'] == 'Caitlin':
            girl_salary.append(employer['salary_rub'])
            avg_girls_salary = sum(girl_salary) / len(girl_salary)
    print(f'Средняя зарплата девушек по {department["title"]} составляет: {int(avg_girls_salary)}')

for department in departments:   # task 12
    for employer in department['employers']:
        if employer['last_name'][-1] in 'aeiouy':
            print(f'Фамилия сотрудника {employer["first_name"]} заканчивается на гласную букву')



