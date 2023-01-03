"""
Module with tests for password validatior project.
"""

from password_validator import PasswordValidator


def test_characters():

    """
    Validation of acceptable symbols used
    to build passwords.
    """

    acceptable_symbols = PasswordValidator.low_letters + \
                         PasswordValidator.up_letters + \
                         PasswordValidator.special_char + \
                         PasswordValidator.digits
    symbols = [chr(symbol) for symbol in range(32, 127)]

    assert (len(set(acceptable_symbols)) == len(set(symbols)) and
            bool(set(acceptable_symbols) - set(symbols)) is False
    )


def test_check_is_in():

    """
    Validation for one symbols-dependend criterium.
    """

    password_to_validate1 = 'PAsSWORD'
    password_to_validate2 = 'PASSWORD'
    validation_true = PasswordValidator(password_to_validate1)
    validation_false = PasswordValidator(password_to_validate2)

    assert (validation_true.checking_is_in(validation_true.low_letters) is True and
            validation_false.checking_is_in(validation_false.low_letters) is False
    )


def test_api_query():

    """
    Validation of api answear
    """

    password_to_validate_1 = 'hdbSF73hwf9&@91hfskLSLf5ss6dfDF'
    password_to_validate_2 = '1234'
    validation_true = PasswordValidator(password_to_validate_1)
    validation_false = PasswordValidator(password_to_validate_2)

    assert (validation_true.checking_is_leacked_by_api() is True and
            validation_false.checking_is_leacked_by_api() is False
           )


def test_complete_check():

    """
    Validation for all criteriums.
    """

    password_to_validate_1 = 'hdbSF73hwf9&@91hfskLSLf5ss6dfDF'
    password_to_validate_2 = 'A1A1Aaa'
    validation_true = PasswordValidator(password_to_validate_1)
    validation_false = PasswordValidator(password_to_validate_2)

    assert (validation_true.complete_validation() is True and
            validation_false.complete_validation() is False
           )
