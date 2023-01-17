# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000
# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
# out
# 8.988

# from decimal import Decimal


# def accuracy(num, acc):
#     number = Decimal(f"{num}")
#     return number.quantize(Decimal(f"{acc}"))


# print(accuracy(float(input("Введите число: ")), float(input("Введите точность округления в виде 0.0001: "))))




# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# in
# 54
# out
# [2, 3, 3, 3]
# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]
# in
# 650
# out
# [2, 5, 5, 13]

# def find_prime_nums(num):
#     pr_fact = []
#     di = 2
#     while num > 1:
#         if num % di == 0:
#             pr_fact.append(di)
#             num //= di
#         else:
#             di += 1
#     return pr_fact
    
# print(find_prime_nums(int(input())))

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in
# -1
# out
# Negative value of the number of numbers!
# []
# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]


# from random import randrange


# def list_rand_nums(count: int):
#     if count < 0:
#         print("Negative value of the number of numbers!")
#         return []

#     list_nums = []
#     for i in range(count):
#         list_nums.append(randrange(count))

#     return list_nums


# def uniq_el(list_nums: list):
#     result = []
#     my_dict = {}.fromkeys(list_nums, 0)

#     for i in list_nums:
#         my_dict[i] += 1

#     for k in my_dict:
#         if my_dict[k] == 1:
#             result.append(k)

#     return result


# all_list = list_rand_nums(int(input("Number of numbers: ")))
# print(all_list)
# print(uniq_el(all_list))
