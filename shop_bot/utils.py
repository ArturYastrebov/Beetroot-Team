def check_for_number(num, list_input_id, name="Guest"):
    while 1:
        if num.isdecimal() and num in list_input_id:
            print(f'\n\033[40m   Good choice {name}  \033[0m ')
            return num
        num = input(f'\033[31mAnswer is not correct =(\033[0m\n{name}, Choice the number again from {list_input_id}:')


def check_for_one_word(word, name = 'Guest') -> str:
    while 1:
        if word.isalpha():
            print(f'\n Nice to meat you {name}\n\033[40m   Your welcome in \'Buffer\' shop   \033[0m ')
            return word
        word = input(f'{name}, Wrong type of value.Please try again and use only one word:')





