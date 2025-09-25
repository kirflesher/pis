groupmates = [
    {
        "name": "Данила",
        "surname": "Иванов",
        "exams": ["СИИ", "АИС", "Web-программирование"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Кирилл",
        "surname": "Купава",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Денис",
        "surname": "Чуенко",
        "exams": ["Философия", "АИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Алекснадр",
        "surname": "Поленов",
        "exams": ["Философия", "ППСУБДиЗ", "СИИ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Николай",
        "surname": "Мельников",
        "exams": ["История", "РОС", "КТП"],
        "marks": [5, 5, 5]
    }
]

def filter_students_by_average(students, min_average):
    """
    Фильтрует студентов по среднему баллу.
    
    Args:
        students: список словарей с информацией о студентах
        min_average: минимальный средний балл для фильтрации
    
    Returns:
        список студентов с средним баллом выше заданного
    """
    filtered_students = []
    
    for student in students:
        # Вычисляем средний балл студента
        marks = student["marks"]
        if marks:  # проверяем, что список оценок не пустой
            average_mark = sum(marks) / len(marks)
        else:
            average_mark = 0
        
        # Если средний балл выше минимального, добавляем студента в результат
        if average_mark > min_average:
            filtered_students.append(student)
    
    return filtered_students

def print_students(students):
    """Функция вывода списка студентов"""
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20), u"Ср. балл".ljust(10))
    for student in students:
        marks = student["marks"]
        average_mark = sum(marks) / len(marks) if marks else 0
        print(student["name"].ljust(15), 
              student["surname"].ljust(10), 
              str(student["exams"]).ljust(30), 
              str(student["marks"]).ljust(20),
              f"{average_mark:.2f}".ljust(10))

if __name__ == "__main__":
    print("Все студенты:")
    print_students(groupmates)
        # Затем запросим фильтрацию
    try:
        min_average = float(input("Введите минимальный средний балл для фильтрации: "))
        
        # Фильтрация студентов
        filtered_students = filter_students_by_average(groupmates, min_average)
        
        # Вывод результатов
        if filtered_students:
            print(f"\nСтуденты со средним баллом выше {min_average}:")
            print_students(filtered_students)
        else:
            print(f"\nНет студентов со средним баллом выше {min_average}")
            
    except ValueError:
        print("Ошибка! Введите числовое значение для среднего балла.")
