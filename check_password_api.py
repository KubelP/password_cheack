'''Part II of password cheacking - cheacking is password leaked using API '''

from hashlib import sha1
from requests import get


class API:
    '''class API checks is password leaked. Takes password checked by class\
    PasswordBuild, change to HASH, send to API server and cheaks is password\
    is in returnes valuse. If false save password in password_git.txt '''

    def __init__(self, password_to_hash) -> None:
        self.password_to_hash = password_to_hash
        self.url = 'https://api.pwnedpasswords.com/range/'
        self.return_hashes = ''
        self.hashed_password = sha1(self.password_to_hash.encode('utf-8'))
        self.hashed = self.hashed_password.hexdigest()
        self.hashed_password_part = self.hashed[:5]
        self.url_with_hash = self.url + self.hashed_password_part

    def leacked_password_checking(self):
        '''take password, chaange to hash, sends to API, chesks is password in\
         returnes values form API and returns file password_git.txt'''

        with get(self.url_with_hash) as cheched_with_api:
            self.return_hashes = cheched_with_api.text

        for return_hash in self.return_hashes:
            if self.hashed_password_part.upper() not in return_hash:
                with open('password_git.txt', mode = 'a', encoding = 'utf-8') as password_git:
                    password_git.write(self.password_to_hash)
                break
