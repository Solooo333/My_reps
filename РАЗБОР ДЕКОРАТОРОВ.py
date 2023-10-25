# ------------------------------------- Передача функции в качестве аргумента ------------------------------------------
def say_hello(name):  # функция 1
    return f"Привет, {name}!"  # возврат строки с переменной аргументом


def be_awesome(name):  # функция 2
    return f"Класс, {name}, быть вместе так круто!"  # возврат строки с переменной аргументом


def greet_vanya(greeter_func):  # функция 3
    return greeter_func("Ваня")  # возврат аргумента функции!


print(greet_vanya)  # <function greet_vanya at 0x000001A4471E9EE0> если просто вызвать функцию 3 без передачи аргумента
print(greet_vanya(be_awesome))  # передача функции 2 в качестве аргумента к функции 3


# --------------------------------------------- Внутренние функции -----------------------------------------------------
def parent():  # родительская функция
    print("Привет из функции parent().")

    def first_child():  # внутренняя функция 1
        print("Привет из функции first_child().")

    def second_child():  # внутренняя функция 2
        print("Привет из функции second_child().")

    second_child()  # порядок определения не имеет значения (печать только при вызове функции внутри)
    first_child()  #


parent()  # вызов родительской функции


# --------------------------------------------- Возврат функций из функций ---------------------------------------------

def parent(num):  # родительская функция
    def first_child():  # внутренняя функция 1
        return "Привет, меня зовут Ксавье."

    def second_child():  # внутренняя функция 2
        return "Зови меня X Æ A-12."

    if num == 1:  # условие для возврата
        return first_child  # возврат функции 1
    else:
        return second_child  # возврат функции 2


first = parent(1)  # присвоение переменной, по условию, функции 1
second = parent(2)  # присвоение переменной, по условию, функции 1

print(first)  # ссылка на функцию 1
print(second)  # ссылка на функцию 1

print(first())  # вызов внутренней функции 1
print(second())  # вызов внутренней функции 2


# в итоге мы получили доступ во внутренние функции материнской def parent(num)

# --------------------------------------------- Простые декораторы -----------------------------------------------------

def decorator(func):
    def wrapper():
        result = func()
        ans = ""
        # ans += "-" * (len(result) + 2)
        ans += f"|{result}|"
        # ans += "-" * (len(result) + 2)
        return ans

    return wrapper


@decorator
def get_hello():
    return "Hello!"


print(get_hello())


def my_decorator(func):  # родительская функция
    def wrapper():  # внутренняя функция
        print("До вызова функции.")
        func()  # ссылка на функцию 2
        print("После вызова функции.")

    return wrapper  # возврат функции wrapper в родительскую функцию


def say_whee():  # функция 2
    print("Ура!")


say = my_decorator(say_whee)  # присвоение в переменную родительской функции (декорирование)
print(say)  # ссылка на внутреннюю функцию wrapper()
say()  # вывод декоратора

from datetime import datetime


def not_during_the_night(func):  # родительская функция
    def wrapper():  # внутренняя функция
        if 8 <= datetime.now().hour < 22:  # условие
            func()  # ссылка на функцию 2
        else:
            print("Не кричи! Уже поздно")

    return wrapper  # возврат функции wrapper в родительскую функцию


def say_whee():  # функция 2
    print("Ура!")


say = not_during_the_night(say_whee)  # присвоение в переменную родительской функции (декорирование)

say()  # вывод декоратора


# --------------------------------------------- Немного синтаксического сахара! ----------------------------------------

def my_decorator(func):
    def wrapper():
        print("До вызова функции.")
        func()
        print("После вызова функции.")

    return wrapper


@my_decorator  # синтаксический сахар в декорировании (вместо: say_whee = my_decorator(say_whee))
def say_whee():
    print("Ура!")


say_whee()


# ----------------------------------------- Повторное использование декораторов ----------------------------------------

# создаем новый файл.py (с именем: decorators.py) и пишем в нем код:
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()

    return wrapper_do_twice


# далее в другом файле.py:
from decorators import do_twice  # из файла decorators.py импортируем декоратор с помощью @do_twice


@do_twice  # декорируем функцию
def say_whee():
    print("Ура!")


say_whee()  # вызываем задекорированную функцию


# ----------------------------------------- Декорирование функций, принимающих аргументы -------------------------------

# создаем новый файл.py (с именем: decorators.py) и пишем в нем код:
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):  # для декорации функции со своим аргументом, указать в декораторе аргументы
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_twice


# далее в другом файле.py:
from decorators import do_twice  # из файла decorators.py импортируем декоратор с помощью @do_twice


@do_twice  # декорируем функцию со своим аргументом
def greet(name):
    print(f"Привет, {name}")


greet("Мир")


def dec(h):
    def wrapper(m):
        if isinstance(m, int):
            return h(m)
        else:
            return list(map(h, list_))

    return wrapper


@dec
def dfg(a):
    return a ** 2


list_ = [1, 2, 3, 4, 5]

print(dfg(list_))
print(dfg(12))
