''' Домашняя работа по уроку "Функции в Python.
   Функция с параметром".
Задача "Матрица воплоти":
Напишите функцию get_matrix с тремя параметрами n, m и value,
которая будет создавать матрицу(вложенный список) размерами n строк и m столбцов,
заполненную значениями value и возвращать эту матрицу в качестве результата работы.
Задача1:
Объявите функцию get_matrix и напишите в ней параметры n, m и value.
Задача2:
Создайте пустой список matrix внутри функции get_matrix.
Задача3:
Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
Задача4:
В первом цикле добавляйте пустой список в список matrix.
задача5:
Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
Задача6:
Во втором цикле пополняйте ранее добавленный пустой список значениями value.
Задача7:
После всех циклов верните значение переменной matrix.
Задача8:
Выведите на экран(консоль) результат работы функции get_matrix. '''
'''---------------------Решение----------------------------------------------------------'''
'''Задание1:
Объявите функцию get_matrix и напишите в ней параметры n, m и value.'''
#n - количество строк в списке
#m - количеество строк во вложенном списке (столбцы)
#value - повторяющиеся значения
def get_matrix(n,
               m,
               value):
    """Задание2:
       Создайте пустой список matrix внутри функции get_matrix."""
    matrix = []
    '''Задание3:
       Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.'''
    for i in range(n):
         matrix
    '''Задание4:
       В первом цикле добавляйте пустой список в список matrix.'''
    for i in range(n):
        matrix.append([])
        '''Задание5:
          Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.'''
        '''Задача6:
           Во втором цикле пополняйте ранее добавленный пустой список значениями value.'''
        for j in range(m):
            matrix[i].append(value)
    '''Задача7:
       После всех циклов верните значение переменной matrix.'''
    return matrix
'''Ввод входящих данных в функцию '''
result1=get_matrix(2,2,10)
result2=get_matrix(3,5,42)
result3=get_matrix(4,2,13)
'''Вывод данных на консоль'''
print(f'Результат №1: {result1}')
print(f'Результат №2: {result2}')
print(f'Результат №3: {result3}')