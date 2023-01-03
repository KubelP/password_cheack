"""
Password validation main file.
To validate password pass it as string
to PASSWORD_TO_VALIDATE variable.
"""

from password_validator import PasswordValidator

if __name__ == '__main__':
    PASSWORD_TO_VALIDATE = 'put your password for validation here'
    password = PasswordValidator(PASSWORD_TO_VALIDATE)
    RESULT = password.complete_validation()

    if RESULT is True:
        print('Password pass all validation critriums - password safe.')
    else:
        print('Password not safe!')
