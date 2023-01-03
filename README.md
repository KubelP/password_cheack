# Password validation

This project is prepare for Pycamp bootcamp. 

This script validates your password by checking if contains at least:
- one lower case letter
- one uppercase letter
- one special character
- one digit
- contains of eight symbols.

Additionally is checking by using api pwnedpasswords.com if password leaked to the Internet.

## Requirements

For use of this script requirement is python3 interpreter or higher.

## Installation

Clone this repositiry on your machine:

```bash
git clone https://github.com/KubelP/password_cheack.git
```

## Script run

For validation pass your password as string to `PASSWORD_TO_VALIDATE` varible in `main.py` file

    PASSWORD_TO_VALIDATE = 'yourpassword'

and run script:

```bash
python3 main.py
```

Information with validation result of your password will be shown in console. 
