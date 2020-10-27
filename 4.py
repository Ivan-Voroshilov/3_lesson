
def my_func(x, y):
    return x ** y  # Либо добавить abs(y) чтобы искать положительную степень


def my_func2(x, y):
    if y == 0:
        return 1
    elif y > 0:
        return x * my_func2(x, y - 1)
    elif y < 0:
        return x * my_func2(x, y + 1)


user_input = input('Введите два числа через пробел ... ')
user_num = user_input.split()
print(my_func(int(user_num[0]), int(user_num[1])))
print(my_func2(int(user_num[0]), int(user_num[1])))
