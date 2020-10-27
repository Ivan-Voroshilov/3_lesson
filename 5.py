
def my_func(*args):
    my_sum = 0
    for i in args:
        my_sum += i
        print(i)
    return my_sum


user_input = input('Введите строку чисел разделенных пробелом ... ')
user_list = user_input.split()
print(my_func(user_list))

#  Не могу понять почему не берет числа из списка
