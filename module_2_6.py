#Дополнительное практическое задание по модулю*
def get_password(number):
    codes = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    if codes.count(number) :
        print(f'Элемент {number} присутствует в списке!')
    else:
        print(f'Элемент {number} отсутствует в списке!\n     Обработка прервана!')
        return
    #Создаю временный список для результатов перебора в циклах
    result_tmp=[]
    #Создаю пустую таблицу номеров numbers для ввода ряда чисел от 1 до number
    numbers=[]
    n = 0
    while n != number-1:
        n = n + 1
        numbers.append(n)
    for num1 in numbers:
        for num2 in numbers:
            if num1!=num2:
               sum_num = num1 + num2
               itognum =[num1, num2]
               itognum.sort()
               if number % sum_num == 0:
                   result_tmp += (itognum,)
    new_result = []
    for num in result_tmp:
        if num not in new_result:
            new_result.append(num)
        result = []
    for num in new_result:
        result += num
    return  result
repport=(get_password(9))
print(("=")*20,"Ответ",("=")*20)
print(*repport)