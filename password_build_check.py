'''Part I of password cheacking - cheacking proper build of password'''
class InvalidPasswordLen(Exception):
    '''Password has to contain at last 8 signs'''

class PasswordBuild:
    '''Take passwords from file password_to_cheack.txt to check is build is proper.\
    If fullifiled requirements returns checked passwords to password_cheacked.txt '''

    def __init__(self, password) -> None:
        self.password = password
        self.lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',\
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', \
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.special_signs = [ '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+',\
            ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^']
        self.digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


    def password_checking(self):
        '''function takes as argument password and checks if meet four conditions
        returnes checked password to check_password.txt file'''

        if len(self.password) < 8:
            raise InvalidPasswordLen

        for letter in self.password:
            if letter in self.lower_letters:
                lower = True
                break
            else:
                lower = False
        for letter in self.password:
            if letter in self.upper_letters:
                upper = True
                break
            else:
                upper = False
        for signe in self.password:
            if signe in self.special_signs:
                signs = True
                break
            else:
                signs = False
        for digit in self.password:
            if digit in self.digits:
                digitss = True
                break
            else:
                digitss = False

        if lower is True and upper is True and signs is True and digitss is True:
            print('Password ok')
            with open('password_checked.txt', mode = 'a', encoding = 'utf-8') as file:
                file.write(self.password)
        elif any([lower, upper, signs, digitss]):
            print('Password has to contain at least one lower case, one upper case,\
one diggit and one symbol')
