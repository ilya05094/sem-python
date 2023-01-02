# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

# from random import sample


# def list_rand_nums(count: int) -> list:
#     if count < 0:
#         print("список из произвольных чисел!")
#         return []

#     list_nums = sample(range(1, count * 2), count)
#     return list_nums


# def sum_odd_pos(list_nums: list):
#     sum_nums = 0
#     for k in range(0, len(list_nums), 2):
#         sum_nums += list_nums[k]
#     return sum_nums


# all_list = list_rand_nums(int(input("Задайте список, состоящий из произвольных чисел: ")))
# print(all_list)
# print(sum_odd_pos(all_list))





# 2. Напишите программу, которая найдёт произведение пар чисел списка.
#    Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# from random import sample


# def list_rand_nums(count):
#     if count < 0:
#         print("список из произвольных чисел!")
#         return []

#     list_nums = sample(range(1, count * 2), count)
#     return list_nums


# def prod_pairs(list_nums: list):
#     res_list = []
#     len_list = len(list_nums)

#     for k in range(len_list // 2):
#         res_list.append(list_nums[k] * list_nums[len_list - k - 1])

#     if len_list % 2:
#         res_list.append(list_nums[len_list // 2])
#     return res_list


# all_list = list_rand_nums(int(input("Задайте список, состоящий из произвольных чисел: ")))
# print(all_list)
# print(prod_pairs(all_list))

# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#    Без использования: встроенной функции преобразования, строк.

# def conv_bin(num: int):
#     list_nums = []

#     while num > 0:
#         list_nums.insert(0, num % 2)
#         num //= 2

#     print(*list_nums, sep="")


# conv_bin(int(input()))