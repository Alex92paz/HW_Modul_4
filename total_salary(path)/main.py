import pathlib

def total_salary(filename: str) -> tuple:
    try:
        # Используем pathlib для создания объекта пути
        path = pathlib.Path(filename)

        with path.open("r", encoding="utf-8") as file:
            lines = file.readlines()

        salaries = []  # Список для хранения зарплат

        # Перебираем строки файла
        for line in lines:
            line = line.strip()  # Убираем лишние пробелы и символы новой строки

            if line:  # Если строка не пуста
                parts = line.split(',')  # Разделяем строку по запятой

                if len(parts) > 1:  # Убедимся, что есть и ФИО, и зарплата
                    try:
                        salary = float(parts[1].strip())  # Берём вторую часть как зарплату и убираем лишние пробелы
                        salaries.append(salary)  # Добавляем зарплату в список
                    except ValueError:
                        continue  # Если не удаётся преобразовать зарплату в число, пропускаем эту строку
                    
        average = sum(salaries)/len(salaries)
        total = sum(salaries)
        return (total, average)  # Возвращаем кортеж с зарплатами

    except FileNotFoundError:
        print('Не удалось найти файл')
        return (0, 0)  # Возвращаем кортеж (0, 0) в случае исключения

total, average = total_salary("text/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
