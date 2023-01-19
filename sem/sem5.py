# 1. Создайте список из N натуральных чисел(0 до N),
#    упорядоченных по возрастанию. Среди чисел не хватает
#    одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
#    Найдите это число.


# from random import choice


# def sequ(num: int):
#     if num < 1:
#         return []

#     num_list = list(range(num + 1))
#     num_list.remove(choice(num_list))
#     return num_list


# def lostie(num_list: list):
#     for i in range(1, len(num_list)):
#         if num_list[i - 1] != num_list[i] - 1:
#             return num_list[i] - 1
#     return -1


# list_nums = sequ(int(input()))
# print(list_nums)
# print(lostie(list_nums))


# 2. Создайте список, в который попадают числа,
#    описывающие возрастающую последовательность.
#    Порядок элементов менять нельзя.

# from random import choices


# def sequ(num: int) -> list:
#     if num < 1:
#         return []
#     return choices(range(num * 2), k=num)


# def all_sets(num_list: list):
#     new_list = []
#     for k in range(len(num_list)):
#         n = num_list[k]
#         temporary = [n]
#         for i in range(k + 1, len(num_list)):
#             if num_list[i] > n:
#                 n = num_list[i]
#                 temporary.append(n)
#         if len(temporary) > 1:
#             new_list.append(temporary)

#     return new_list


# list_nums = sequ(int(input()))
# print(list_nums)
# print(all_sets(list_nums))