
def my_func(name, surname, birth, city, email, phone):
    """Информация о человеке"""
    return print(name, surname, birth, city, email, phone)


info = input('Введите через пробел ваши: Имя Фамилию Год рождения Город Email Телефон\n')
info_list = info.split()
my_func(name=info_list[0], surname=info_list[1], birth=info_list[2], city=info_list[3],
        email=info_list[4], phone=info_list[5])
