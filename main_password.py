'''main conects clases PasworBuild with API'''

from password_build_check import PasswordBuild
from check_password_api import API


def build_api_checking():
    '''functions runs in loop class PasswordBuild and API. \
    Takes password to check from file and returns verifide passwords in file password_git.txt'''
    
    with open('passwords_to_cheack.txt', mode = 'r', encoding = 'utf-8') as file:
        for line in file:
            password_cheack_level_1 = PasswordBuild(line)
            password_cheack_level_1.password_checking()
            
    with open('password_checked.txt', mode = 'r', encoding = 'utf-8') as file2:
        for line2 in file2:
            password_cheack_level_2 = API(line2)
            password_cheack_level_2.leacked_password_checking()
            password_cheack_level_2.git_password_added()

build_api_checking()
