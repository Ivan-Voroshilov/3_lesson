
def my_func(arg_1, arg_2):
    """Деление чисел"""
    if arg_1 == 0:
        return 'Ошибка: деление на ноль'
    elif arg_2 == 0:
        return 'Ошибка: деление на ноль'
    else:
        return arg_1 / arg_2


arg_out_1 = int(input('Введите первое число ... '))
arg_out_2 = int(input('Введите второе число ... '))
print(my_func.__doc__)
print(my_func(arg_out_1, arg_out_2))
