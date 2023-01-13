# 1. Задайте строку из набора чисел. Напишите программу,
#    которая покажет большее и меньшее число.
#    В качестве символа-разделителя используйте пробел.


# def check(str_list: list):
#     new_list = []
#     for i, num in enumerate(str_list):
#         str_list[i] = num.strip('.,;:?!')
#         if str_list[i].replace("-", "").isdigit():
#             new_list.append(str_list[i])
#     return new_list
    

# def find_max_min(nums_str: str):
#     list_nums = nums_str.split()
#     right_list = check(list_nums)

#     if right_list:
#         return min(right_list, key=int), max(right_list, key=int)
#     print("The data is incorrect")
#     return []


# print(*find_max_min(input("Enter the numbers separated by a space: ")))


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
#    с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
#    Уравнения и корни запишите в файл.

# from math import sqrt


# def roots_equ(a, b, c):
#     d = b ** 2 - 4 * a * c
#     with open("roots.txt", "a", encoding="utf-8") as my_f:
#         my_f.write(f"{a}x ** 2 + {b}x + {c}\n")
#         if d > 0 and a:
#             my_f.write(f"The first root: {(-b + sqrt(d)) / (2 * a):.2f}\n")
#             my_f.write(f"The first root: {(-b - sqrt(d)) / (2 * a):.2f}\n")
#         elif d == 0 and a:
#             my_f.write(f"The root: {-b / (2 * a):.2f}\n")
#         else:
#             my_f.write("There are no roots.\n")


# # 1 2 -3, 5 6 -7, 8 9 -10
# for i in range(3):
#     roots_equ(int(input("Enter the coefficient 'a': ")), int(input("Enter the coefficient 'b': ")),
#               int(input("Enter the coefficient 'c': ")))


# 3. На вход программе подается число n.
#    Программа печатает численный треугольник.
#    Используем вложенные циклы.

# n = int(input())

# for i in range(1, n + 1):
#     for k in range(i):
#         print(i, end="")
#     print()
