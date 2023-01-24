# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
# in
# 10
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]


# from random import randint


# def more_then(num):
#     original_list = [randint(0, 1000) for _ in range(num)]
#     print(original_list)
#     return [num for i, num in enumerate(original_list[1:]) if num > original_list[i]]


# print(more_then(int(input())))



# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.in
# 100
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]
# in
# 424
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147, 160, 168, 180, 189, 200, 210, 220, 231, 240, 252, 260, 273, 280, 294, 300, 315, 320, 336, 340, 357, 360, 378, 380, 399, 400, 420]


# n = int(input("Введите число N: "))

# def find_nums(n):
#     i = 20
#     resalt_list = [i for i in range(i, n+1) if i <= n and i % 20 == 0 or i % 21 == 0]
#     return resalt_list

# res = find_nums(n)
# print(res)


# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь,
#    ключи — первые буквы имён, значения — списки, содержащие имена,
#    начинающиеся с соответствующей буквы.



# def thesaurus(*args):
#     names_dict = {}
#     for i in sorted(args):
#         letter = i[0]
#         if letter not in names_dict:
#             names_dict[letter] = [i]
#         names_dict[letter] += [i]

#     return names_dict


# print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Алина", "Бибочка"))