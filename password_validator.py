"""
Password validator used for validation of password by cheacking
is it contains at least:
- one lower case letter
- one uppercase letter
- one special character
- one digit
- contains of eight symbols.
Additionally it is checking by using api pwnedpasswords.com
if password leaked to the Internet.
"""

from hashlib import sha1
from requests import get


class PasswordValidator:

    """
    Class take as arguemet string password_to_validate.
    Methodes:
    - checking_is_in
    - checking_is_leacked_by_api
    - complete_validation
    """

    low_letters = [chr(letter) for letter in range(97, 123)] #low case letters
    up_letters = [letter.upper() for letter in low_letters] # upper case letters
    special_char = [chr(special) for special in range(32, 48)] +\
                   [chr(special) for special in range(58, 65)] +\
                   [chr(special) for special in range(91, 97)] +\
                   [chr(special) for special in range(123, 127)] # special characters
    digits = [str(digit) for digit in range(0, 10)] # digits

    def __init__(self, password_to_validate: str):
        self.password_to_validate = password_to_validate
        self.api_url = 'https://api.pwnedpasswords.com/range/'


    def checking_is_in(self, symbols: list) -> bool:

        """
        Checking if symbol is in validated password.
        Returns True if it is and False if not.
        """

        for character in self.password_to_validate:
            if character in symbols:
                return True
        return False

    def checking_is_leacked_by_api(self) -> bool:

        """
        Checking if password is leaked to internet by
        send five first characters of hashed password_to_validate,
        compares with returned from api  hashes and if matched
        any returns False.
        """

        hashed_password = sha1(self.password_to_validate.encode('utf-8')).hexdigest()
        hashed_password_part = hashed_password[:5].upper()
        api_query = self.api_url + hashed_password_part

        with get(api_query, timeout = 3) as leaked_validation:
            return_hashes = leaked_validation.text.splitlines()

        for return_hash in return_hashes:
            return_hashes_split, _ = return_hash.split(':')

            if hashed_password.upper()[5:] == return_hashes_split:
                return False
        return True


    def complete_validation(self) -> bool:

        """
        Validates with all criteria.
        Password has to contain at least:
        - one lower case letter
        - one uppercase letter
        - one special character
        - one digit
        - contains of eight symbols
        and it is not in records in pwnedpasswords.com.
        If all are fulfilled returns True, else returns
        False with not fulfilled critetirum.
        """

        low_letters_criterium = True
        up_letters_criterium = True
        special_char_criterium = True
        digits_criterium = True
        pass_length_criterium = True
        leacked_criterium = True

        if not self.checking_is_in(self.low_letters):
            low_letters_criterium = False
            print('No low case letter in password.')

        if not self.checking_is_in(self.up_letters):
            up_letters_criterium = False
            print('No up case letter in password.')

        if not self.checking_is_in(self.special_char):
            special_char_criterium = False
            print('No special chracter in password.')

        if not self.checking_is_in(self.digits):
            digits_criterium = False
            print('No digit in password.')

        if not len(self.password_to_validate) >= 8:
            pass_length_criterium = False
            print('Password to short.')

        if not self.checking_is_leacked_by_api():
            leacked_criterium = False
            print('Danger! Password leaked to the Internet!')

        criteriums = [low_letters_criterium, up_letters_criterium,
                      special_char_criterium, digits_criterium,
                      pass_length_criterium, leacked_criterium]

        if all(criteriums):
            return True
        return False
