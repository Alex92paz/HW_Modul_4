import pathlib
# import os
# print(f"Текущая рабочая директория: {os.getcwd()}")

def get_cats_info(filename: str) -> list:
    try:
        # Используем pathlib для создания объекта пути
        path = pathlib.Path(filename)

        with path.open("r", encoding="utf-8") as file:
            lines = file.readlines()

        cats_list = []  # Список для хранения данных о котах

        # Перебираем строки файла
        for line in lines:
            line = line.strip()  # Убираем лишние пробелы и символы новой строки

            if line:  # Если строка не пуста
                parts = line.split(',')  # Разделяем строку по запятой

                if len(parts) == 3:  # Убедимся, что есть идентификатор кота, его имя и возраст
                    try:
                        id = parts[0].strip()  # Берём первую часть как идентификатор кота и убираем лишние пробелы
                        name = parts[1].strip()  # Берём вторую часть как имя кота и убираем лишние пробелы
                        age = parts[2].strip()  # Берём третью часть как возраст кота и убираем лишние пробелы

                        # Добавляем данные кота в список в формате словаря
                        cats_list.append({"id": id, "name": name, "age": age})
                    except ValueError:
                        continue  # Если не удаётся преобразовать возраст в число, пропускаем эту строку

        return cats_list  # Возвращаем список с данными о котах

    except FileNotFoundError:
        print('Не удалось найти файл')
        return [0]

# Вызов функции и вывод результата
result = get_cats_info("data/cats_info.txt")
print(result)