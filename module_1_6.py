# Работа со словарями
my_dict = {'Змей Гороныч': 271354}
print(my_dict)
print('Вывод данных по ключу:', my_dict['Змей Гороныч'])
# Несушествующий ключ в словаре
my_dict['Леший'] = 262134
print(my_dict)
# Длбавил два несущиствующих ключа
my_dict['Бабушка Гульда'] = 260211
my_dict['Щегол'] = 2711223
print(my_dict)
# Удаление ключа и вывод значения.
my_dict.pop('Щегол')
print(my_dict)
# Работа с множествами
my_set= {12,12 ,'Мороженное',True,True}
print(my_set)
# Добавляем 2 произвольных элемента в множество

set=my_set.add(3)
set1=my_set.add(4)
print(my_set)
# Удалякм элемент из множества
set3=my_set.discard(4)
print(my_set)



