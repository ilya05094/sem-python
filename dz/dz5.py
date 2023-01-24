# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
# in
# Number of words: 6
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва
# in
# Number of words: -1
# out
# The data is incorrect
# from random import sample


# def list_rand_words(count: int, alp: str = 'абв'):
#     words_list = []
#     for i in range(count):
#         letters = sample(alp, 3)
#         words_list.append("".join(letters))
#     return " ".join(words_list)





# def simple_sentence(words: str) -> str:
#     return " ".join(i for i in words.split() if i != "абв")


# all_list = list_rand_words(int(input("Number of words: ")))
# print(all_list)
# print(simple_sentence(all_list))


# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах

# with open('text_file.txt', 'w', encoding='UTF-8') as file:
#     file.write(input('Please, input text for encoding: '))
# with open('text_file.txt', 'r') as file:
#     my_txt = file.readline()
#     txt_compr = my_txt.split()
# print(my_txt)

# def rle_encode(decoded_string):
#     encoded_string = ''
#     count = 1
#     char = decoded_string[0]
#     for i in range(1, len(decoded_string)):
#         if decoded_string[i] == char:
#             count += 1
#         else:
#             encoded_string = encoded_string + str(count) + char
#             char = decoded_string[i]
#             count = 1
#             encoded_string = encoded_string + str(count) + char
#     return encoded_string

# with open('text_file.txt', 'r') as file:
#     decoded_string = file.read()



# print('Encoded text: \t' + rle_encode(decoded_string))