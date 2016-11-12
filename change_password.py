# -*- encoding: UTF-8 -*-

import re
import getpass


class ValidatorError(Exception):
    pass


class SecondAuthenticationError(Exception):
    pass


class PasswordValidator(object):
    """ A password validator, used to validate a password for
        specific characters, numbers, and special characters """

    def __init__(self, password):
        self.password = password
        self.validators = [self.validate_integers(self.password), self.validate_spec_chars(self.password),
                           self.validate_length(self.password), self.validate_lower_case(self.password),
                           self.validate_upper_case(self.password)]

    def validate_length(self, password):  # Check the length, gotta be over 8
        if len(password) > 8:
            return True
        else:
            raise ValidatorError("Failed to validate length. Allowed length: (> 8)")

    def validate_upper_case(self, password):  # Check for upper case characters
        if re.search("[A-Z]", password) is not None:
            return True
        else:
            raise ValidatorError("Failed to validate upper case characters. (A - Z)")

    def validate_lower_case(self, password):  # Check for lower case characters
        if re.search("[a-z]", password) is not None:
            return True
        else:
            raise ValidatorError("Failed to validate lower case characters. (a - z)")

    def validate_integers(self, password):  # Check for integers
        if re.search("[0-9]", password) is not None:
            return True
        else:
            raise ValidatorError("Failed to validate integers. (0 - 9)")

    def validate_spec_chars(self, password):  # Check for special characters
        if re.search("[!$&*]", password) is not None:
            return True
        else:
            raise ValidatorError("Failed to validate special characters. Allowed: ( !$&* )")

    def validate(self):
        """ Validate everything. """
        try:
            return all(validators for validators in self.validators)
        except ValidatorError as e:
            print e
            return False


def encrypt(password):
    """ Encrypt the password simply example: bÃ­Fuo <- says Test!23456
    :type password: String """
    encrypt_arr = list(password)
    new_encrypt_arr = []

    for i in encrypt_arr:
        num = ord(i) + 3
        new_encrypt_arr.append(chr(num))

    return ''.join(new_encrypt_arr)


def decrypt(encrypted_password):
    """ Decrypt a password when needed
    :type encrypted_password: String (UTF-8) """
    decrypt_arr = list(encrypted_password)
    new_decrypt_arr = []

    for char in decrypt_arr:
        num = ord(char) - 3
        new_decrypt_arr.append(chr(num))

    return ''.join(new_decrypt_arr)


def obtain_password():
    """ Get the password, simple and easy with getpass library """
    return getpass.getpass('Change your password: ')


def second_authentication(password_to_verify):
    """ Verify that the password is what the user wants it to be,
        by asking for it a second time.
        :type password_to_verify: String """
    password = getpass.getpass('Enter password a second time: ')
    if encrypt(password) == encrypt(password_to_verify):
        with open('passwords.txt', 'a+') as f:
            f.write(encrypt(password_to_verify))
        return "Password changed successfully."
    else:
        raise SecondAuthenticationError("Passwords encryption did not match.")


def erase_all(file_list):
    """ Erase all data from the file because you where an idiot and
        forgot your password
        :type file_list: List """
    for files in file_list:
        open(files, 'w').close()


def user_login():
    """ Login and create a username, maybe """
    with open('username.txt', 'a+') as f:
        if f.readline() is "":
            username = raw_input("First login, enter a username to use: ")
            f.seek(0)
            f.write(username)
        else:
            login_id = raw_input("Enter username: ")
            f.seek(0)
            if login_id == f.readline():
                return True
            else:
                print "Invalid username."
                return False


def user_password():
    """ If you mess up all the data will be gone. """
    files = ['username.txt', 'passwords.txt']
    attempts = 3

    while True:
        password_to_compare = getpass.getpass("Enter password: ")

        with open('passwords.txt', 'a+') as password:
            if password.readline() is not "":
                password.seek(0)
                if password_to_compare == decrypt(password.readline()):
                    return True
                else:
                    print "Invalid password.."
                    if attempts == 0:
                        print "Exiting and erasing data.."
                        erase_all(files)
                        print "All data truncated."
                        break
                    else:
                        attempts -= 1
                        print "You have {} attempts left..".format(attempts)


if __name__ == '__main__':
    try:
        if user_login() is True:
            if user_password() is True:
                print "Welcome home.."
        else:
            password_to_verify = obtain_password()
            val = PasswordValidator(password_to_verify)
            if val.validate() is not False:
                print second_authentication(password_to_verify)

    except ValidatorError, SecondAuthenticationError:
        print "Failed to verify, password and username truncated"
        erase_all(['username.txt', 'password.txt'])
