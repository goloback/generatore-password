from random import randint, choice

class Generate_password():
    def __init__(self):
        self.password = ''
        self.pass_len = 16
        self.numbers = '1234567890'
        self.letters = 'qwertyuiopasdfghjklzxcvbnm'
        self.LETTERS = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        self.sympol = '!@#$%^&*_-()=+~:;<,>./?|\\][{}:"\''
        self.numbers_amount = 20
        self.letters_amount = 45
        self.LETTERS_amount = 20
        self.sympol_amount = 15

    def amount_generator(self):
        self.password = ''
        self.pass_len = self.numbers_amount + self.letters_amount + self.LETTERS_amount + self.sympol_amount
        len_numbers = self.numbers_amount
        len_letters = self.letters_amount
        len_LETTERS = self.LETTERS_amount
        len_sympol = self.sympol_amount
        buf_str = ''
        for i in range(len_numbers):
            buf_str +='1'
        for i in range(len_letters):
            buf_str +='2'
        for i in range(len_LETTERS):
            buf_str +='3'
        for i in range(len_sympol):
            buf_str +='4'
        used_index = list()
        buf_str_random = ''
        while len(buf_str_random) != self.pass_len:
            index = randint(0, self.pass_len-1)
            if index in used_index:
                continue
            else:
                used_index.append(index)
                buf_str_random += buf_str[index]
        for i in buf_str_random:
            if i == '1':
                self.password+=self.numbers[randint(0, len(self.numbers)-1)]
            elif i == '2':
                self.password+=self.letters[randint(0, len(self.letters)-1)]
            elif i == '3':
                self.password+=self.LETTERS[randint(0, len(self.LETTERS)-1)]
            elif i == '4':
                self.password+=self.sympol[randint(0, len(self.sympol)-1)]
        print(self.password)
    def set_len_password(self):
        self.pass_len = int(input('write password length\n'))

    def generator_only_one_type_password(self, type):
        self.password = ''
        list_for_password = None
        if type == 'numbers':
            list_for_password = self.numbers
        elif type == 'letters':
            list_for_password = self.letters
        elif type == 'LETTERS':
            list_for_password = self.LETTERS
        elif type == "sympols":
            list_for_password = self.sympol
        for i in range(self.pass_len):
            random_value = list_for_password[randint(0, len(list_for_password)-1)]
            self.password += random_value
        print(self.password)

    def generator_two_types_password(self, type1, type2):
        self.password = ''
        list_for_password=[]
        if type1 == 'numbers' or type2 == 'numbers':
            list_for_password.append(self.numbers)
        if type1 == 'letters' or type2 == 'letters':
            list_for_password.append(self.letters)
        if type1 == 'LETTERS' or type2 == 'LETTERS':
            list_for_password.append(self.LETTERS)
        if type1 == 'sympols' or type2 == 'sympols':
            list_for_password.append(self.sympol)
        for i in range(self.pass_len):
            random_list = choice(list_for_password)
            random_value = random_list[randint(0, len(random_list)-1)]
            self.password += random_value
        print(self.password)
    def generator_three_types_password(self, type1, type2, type3):
        self.password = ''
        list_for_password=[]
        if type1 == 'numbers' or type2 == 'numbers' or type3 == 'numbers':
            list_for_password.append(self.numbers)
        if type1 == 'letters' or type2 == 'letters' or type3 == 'letters':
            list_for_password.append(self.letters)
        if type1 == 'LETTERS' or type2 == 'LETTERS' or type3 == 'LETTERS':
            list_for_password.append(self.LETTERS)
        if type1 == 'sympols' or type2 == 'sympols' or type3 == 'sympols':
            list_for_password.append(self.sympol)
        for i in range(self.pass_len):
            random_list = choice(list_for_password)
            random_value = random_list[randint(0, len(random_list)-1)]
            self.password += random_value
        print(self.password)


    def generator_four_types_password(self):
        self.password = ''
        for i in range(self.pass_len):
            number_str = randint(1, 4)
            if number_str == 1:
                self.password += self.numbers[randint(0, len(self.numbers)-1)]
            elif number_str == 2:
                self.password += self.letters[randint(0, len(self.letters)-1)]
            elif number_str == 3:
                self.password += self.LETTERS[randint(0, len(self.LETTERS)-1)]
            elif number_str == 4:
                self.password += self.sympol[randint(0, len(self.sympol)-1)]
        print(self.password)


