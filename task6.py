"""Создать класс для работы с файлом в csv формате. Методы класса:
Сортировка по 1 полю
Добавление строки
Обновление строки
Редактирование строки
Поиск элементов по заданному условию"""




import pandas as pandasCSV
import csv
from csv import writer



# Создаем класс для работы с csv
class CvsFile:

    def __init__(self, file):
        self.file = file
    # Сортировка по 1 полю
    def sort_file(self):
        csvData = pandasCSV.read_csv("CsvFile.csv")
        csvData.sort_values(["Wazza"],
                            axis=0,
                            ascending=[False],
                            inplace=True)

    #Добавление строки
    def add_file(self):
        #Сначала открываем файл CSV, обозначаем как 'a', а затем file object
        with open('CsvFile.csv', 'a', newline='') as f_object:
            #Используем writer и даем ему переменную
            writer_object = writer(f_object)
           #Добавляем whiterow
            writer_object.writerow('L')
           #Закрываем затем его
            f_object.close()

    def update_file(self):
        pass

    def correct_file(self):
        # Открываем файл
        with open('CsvFile.csv', 'w') as csv_object:
            #
            writer = csv.writer(csv_object, delimiter=',', quotechar='"')

            # Открываем файл
            with open('tmpEmployeeDatabase.csv', 'r') as csvFile:
                # Читаем содержимое в файле
                reader = csv.reader(csvFile, delimiter=',', quotechar='"')

                # и затем пробегаемся с помощью цикла for
                for row in reader:
                    row[0] = row[0].title()
                    writer.writerow(row)

    def search_file(self):
        pass


a = CvsFile




