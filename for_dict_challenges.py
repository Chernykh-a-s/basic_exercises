# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
name_of_students = [students[name]['first_name'] for name in range(len(students))]
uniq_name = []

for name in name_of_students:
    if name not in uniq_name:
        uniq_name.append(name)

for name in range(len(uniq_name)):
    print(f'{uniq_name[name]}: {name_of_students.count(students[name]["first_name"])}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

def max_name(students):
    name_of_students = [students[name]['first_name'] for name in range(len(students))]

    names_counter = dict()
    for name in name_of_students:
        if name in names_counter:
            names_counter[name] += 1
        else:
            names_counter[name] = 1

    max_names = []
    max_count = 0

    for name, count_of_name in names_counter.items():
        if count_of_name > max_count:
            max_count = count_of_name
            max_names = [name]
        elif count_of_name == max_count:
            max_names.append(name)
    return f'Самое частое имя среди учеников: {"".join(max_names)}'


print(max_name(students))
# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
print(max_name(school_students[0]))
print(max_name(school_students[1]))
print(max_name(school_students[2]))

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

male_gender = 0
female_gender = 0

for class_i in range(len(school)):
    lst_of_class = [class_x for class_x in school[class_i]['students']]
    for i in range(len(lst_of_class)):
        if is_male.get(lst_of_class[i]['first_name']) == 1:
            male_gender += 1
        else:
            female_gender += 1
    print(f'Класс {school[class_i]["class"]}: девочки {female_gender}, мальчики {male_gender}')
    male_gender = 0
    female_gender = 0


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???

