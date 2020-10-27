
def my_func(arg1, arg2, arg3):
    """Принимает три, возвращает сумму наибольших двух"""
    my_list = [arg1, arg2, arg3]
    lowest = min(my_list)
    my_list.remove(lowest)
    print(int(my_list[0]) + int(my_list[1]))


user_input = (input('Введите три числа через пробел ... '))
user_list = user_input.split()
my_func(user_list[0], user_list[1], user_list[2])
