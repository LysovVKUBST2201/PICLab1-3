def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), 
              student["surname"].ljust(10), 
              str(student["exams"]).ljust(30), 
              str(student["marks"]).ljust(20))

groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
    ]

# Ввод порогового значения
min_avg = float(input("Введите минимальный средний балл: "))

# Фильтрация студентов
filtered_students = []
for student in groupmates:
    # Вычисляем средний балл для каждого студента
    marks = student["marks"]
    avg_mark = sum(marks) / len(marks)
    
    # Проверяем условие и добавляем в отфильтрованный список
    if avg_mark >= min_avg:
        filtered_students.append(student)

# Вывод результатов
print("\nСтуденты со средним баллом выше", min_avg)
if filtered_students:
    print_students(filtered_students)
else:
    print("Нет студентов с таким средним баллом")



