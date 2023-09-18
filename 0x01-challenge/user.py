#!/usr/bin/python3

class User():
    """ User class """

    def __init__(self):
        """ Initialize User object """
        self.__email = None

    @property
    def email(self):
        """ Get the email """
        return self.__email

    @email.setter
    def email(self, value):
        """ Set the email """
        if not isinstance(value, str):
            raise TypeError("email must be a string")
        self.__email = value

if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)
