import re
import time
buffer_len = 1
work_buffer = ""
h = 0
flag1 = False
flag2 = False
flag3 = False
try:
    while 1:
        k = input('Введите число k:')  # Ввод значения переменной с клавиатуры
        if (k >= '0') and (k <= '9'):
            digit = int(k)
            break
        else:  # Если число выходит за промежутки
            print('Программа не может переводить числа в такую систему счисления, '
                  'либо такой системы счисления не существует.')
    start = time.time()
    with open("laba 2.txt", 'r+', encoding='utf-8') as file:
        print("\n Результат работы программы")
        buffer = file.read(buffer_len)
        if not buffer:
            print("\n Рабочий файл пустой")
            flag3 = True
        while buffer:
            work_buffer += buffer
            if re.findall(r'[.!?]', buffer):
                if len(work_buffer) == 1:
                    work_buffer = ""
                    flag2 = True
                flag1 = True
                g = re.split(r'\W', work_buffer)
                g = g[:len(g) - 1]
                for i in range(len(g)):
                    if g[i].isdigit():
                        h += 1
                        if len(g[i]) != digit and not flag2:
                            print(work_buffer)
                if h == 0 and not flag2:
                    print(work_buffer)
                else:
                    h = 0
                flag2 = False
                work_buffer = ""
                g = ""
            buffer = file.read(buffer_len)
        if not flag1 and not flag3:
            print("\nВ файле отсутствуют знаки препинания.")
        finish = time.time()
        result = finish - start
        print("Program time: " + str(result) + " seconds.")
except FileNotFoundError:
    print("\nФайл проекта не обнаружен в директории.")кта не обнаружен в директории.")