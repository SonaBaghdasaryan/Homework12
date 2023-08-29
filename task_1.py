# Решить задания, которые не успели решить на семинаре.
# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
import csv
from random import randint

myList = [{'lesson' : 'Русский язык'},
          {'lesson' : 'Английский язык'},
          {'lesson' : 'Математика'},
          {'lesson' : 'Физика'}]

with open("lessons.csv", 'w', newline='', encoding='utf-8') as file:
    csv_write = csv.DictWriter(file, fieldnames=[*myList[0]])
    csv_write.writeheader()
    csv_write.writerows(myList)
import csv

class descrStr:

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
#        print(f"__set__{self.name} = {value}")
        if not(value.isalpha() and value[0].isupper()):
            raise TypeError("Имя должно содержать только буквы, первая заглавная")
        else:
            setattr(instance, self.name, value)

class Student:
    name = descrStr()
    surname = descrStr()
    patronymic = descrStr()

    def __init__(self, name:str, surname: str, patronymic :str, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self._myList = self.grades()
        self.performance = self.setGrades()

    def grades(self):
        with open("lessons.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            myList = []
            for row in reader:
                myList.append(row["lesson"])
        return myList

    def setGrades(self):
        gradeDict = {}
        for i in self._myList:
            x = randint(2, 5)
            y = randint(2, 5)
            z = randint(2, 5)
            iTest = randint(20, 100)
            gradeDict[i] = f"{x}, {y}, {z}    средний балл - {round((x+y+z)/3, 2)},    Итоговое тестирование - {iTest}"
        return gradeDict

    def printSt(self):
        print("©"*100)
        print(f'{self.surname} {self.name[0]}. {self.patronymic[0]} ')
        print(" "+';\n '.join([f'{key.capitalize()}: {value}' for key, value in self.performance.items()]))


ob = Student("Иван", "Иванов", "Иванович")
ob2 = Student("Андрей", "Петров", "Сергеевич")
ob3 = Student("Сергей", "Шишков", "Алексеевич")

ob.printSt()
ob2.printSt()
ob3.printSt()