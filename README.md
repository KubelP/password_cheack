# password_cheack
Take passwords from file password_to_cheack.txt and checks is build is proper by class PasswordBuild.
If fullifiled requirements (at least lenght 8 symbols, at least 1 lower letter, 1 upper, 1 digit and 1 special) returns checked passwords to password_cheacked.txt.
Then checks is password leaked by class API. Takes password checked by class PasswordBuild, change to HASH, send to API server and cheaks is password is in returnes valuse. If false saves passwords in password_git.txt
