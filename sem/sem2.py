# 1. Напишите программу, которая принимает на вход число N и выдает последовательность из N членов.

# n = int(input())

# for i in range (n):
#     print((-3)**i, end= ' ')

# Вариант 2

# n = int(input())
# seq_n = 1

# for i in range (n):
#     print(seq_n, end= ' ')
#     seq_n*=-3

# 2. Создать список, длины n, значение формируется по формуле 3k+1, где k принимает значение от 1 до n включительно.

# import os
# clear = lambda:os.system('cls')
# clear()

# num_list = []
# n = int(input('введите число'))
# for ik in range (1, n+1):
#     num_list.append(3*k+1)
# print(num_list)    

# 3. Напишите программу, в которой пользователь будет задавать две строки, программа - определять количество вхождений одной строки в другую.

# n = input()
# m = input()

# print(n.count(m))

