var groupmates = [
    {
        "name": "Данила",
        "surname": "Иванов",
        "group": "БВТ1702",
        "marks": [4, 3, 5]
    },
    {
        "name": "Кирилл",
        "surname": "Купава",
        "group": "БАП1801",
        "marks": [4, 4, 4]
    },
    {
        "name": "Денис",
        "surname": "Чуенко",
        "group": "БСТ1801",
        "marks": [5, 5, 5]
    },
    {
        "name": "Алекснадр",
        "surname": "Поленов",
        "group": "БВТ1801",
        "marks": [5, 5, 5]
    },
    {
        "name": "Николай",
        "surname": "Мельников",
        "group": "БСТ1701",
        "marks": [5, 5, 5]
    }
];

var rpad = function(str, length) {
    str = str.toString();
    while (str.length < length)
        str = str + ' ';
    return str;
};

var printStudents = function(students){
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20)
    );
    for (var i = 0; i<=students.length-1; i++){
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['surname'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['marks'], 20)
        );
    }
    console.log('\n');
}

// Фильтрация массива студентов по названию группы
var filterByGroup = function(students, groupName) {
    // Возвращает студентов, у которых имя группы совпадает с введённым (без учёта регистра)
    return students.filter(function(student) {
        return student.group.toLowerCase() === groupName.toLowerCase();
    });
};

// Фильтрация массива студентов по среднему баллу
var filterByAverageMark = function(students, minAverage) {
    // Возвращает студентов, у которых средний балл превышает минимальное значение
    return students.filter(function(student) {
        var average = student.marks.reduce((a, b) => a + b, 0) / student.marks.length; // Вычисляет средний балл
        return average > minAverage;
    });
};

// Получение ввода от пользователя через диалоговое окно
var getUserInput = function(promptText) {
    // Возвращает введённую пользователем строку
    return prompt(promptText);
};

// Демонстрация фильтрации по группе
var groupFilter = function() {
    var groupFilter = getUserInput("Введите название группы для фильтрации:"); // Получить группу от пользователя
    var filteredByGroup = filterByGroup(groupmates, groupFilter); // Фильтруем студентов по группе
    console.log("Студенты группы '" + groupFilter + "':");
    if (filteredByGroup.length > 0) {
        printStudents(filteredByGroup); // Выводим студентов, если найдены
    } else {
        console.log("Студентов в данной группе не найдено.\n"); // Сообщаем, если никто не найден
    }
};

// Демонстрация фильтрации по среднему баллу
var markFilter = function() {
    var minAverageInput = getUserInput("Введите минимальный средний балл для фильтрации:"); // Запросить балл
    var minAverage = parseFloat(minAverageInput); // Преобразовать ввод к числу
    if (!isNaN(minAverage)) { // Проверка на корректность ввода
        var filteredByMark = filterByAverageMark(groupmates, minAverage); // Фильтруем студентов по среднему баллу
        console.log("Студенты со средним баллом выше " + minAverage + ":");
        if (filteredByMark.length > 0) {
            printStudents(filteredByMark); // Выводим студентов, если найдены
        } else {
            console.log("Студентов с таким средним баллом не найдено.\n"); // Сообщаем, если никто не найден
        }
    } else {
        console.log("Некорректный ввод среднего балла.\n"); // Сообщаем о некорректном вводе
    }
};

