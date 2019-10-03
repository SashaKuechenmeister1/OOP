import random
from random import shuffle

def shuffle_word(word):
    middle_part = word[1:len(word) - 1]
    first_let = str(word[0])
    last_let = str(word[-1])
    middle_part = list(middle_part)
    shuffle(middle_part)
    return first_let + ''.join(middle_part) + last_let

#user input
txt_str = input("Enter text you wish to scramble and hit enter:")
my_list = str.split(txt_str)

for i in range(len(my_list)):
    if 3 < len(my_list[i]):
        print(shuffle_word(my_list[i]))
    else:
        print(my_list[i])