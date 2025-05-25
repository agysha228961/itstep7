class Animal:
    def speak(self):
        raise NotImplementedError("Метод speak должен быть переопределён в подклассе")

    def describe(self):
        print(f"This is a {self.__class__.__name__}")

class Dog(Animal):
    def speak(self):
        print("Dog says: Woof")

class Cat(Animal):
    def speak(self):
        print("Cat says: Meow")

class Parrot(Animal):
    def speak(self):
        print("Parrot says: I'm a pirate")


animals = [Dog(), Cat(), Parrot()]
for animal in animals:
    animal.speak()











def who_am_i(obj):
    print("Тип объекта", type(obj))
    print("Атрибуты и методы", dir(obj))
    if type(obj).__module__ == 'builtins':
        print("Это встроенный ")
    else:
        print("пользовательский или внешний ")


who_am_i(123)
who_am_i("hello")
who_am_i([1, 2, 3])










import sys

print("Версия Python:", sys.version)
print("Путь к Python:", sys.executable)
print("Аргументы командной строки:", sys.argv)
print("Имя платформы:", sys.platform)






def calculator():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        op = input("Введите операцию (+, -, *, /): ")

        if op == '+':
            print("Результат:", a + b)
        elif op == '-':
            print("Результат:", a - b)
        elif op == '*':
            print("Результат:", a * b)
        elif op == '/':
            print("Результат:", a / b)
        else:
            print("Ошибка: неизвестная операция.")
    except ValueError:
        print("Ошибка: неверный ввод числа.")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")


calculator()