import string
import secrets

pwd_len = int(input('Please enter the password length do you want: '))

ALL_CHARACTERS = string.ascii_letters + string.digits + string.punctuation


def generator_random_password(pwd_len):
    """The function receives an int that functions as the maximum range to
    iterate to create the password.

    Args:
        pwd_len (int): Integer that determines the password length.

    Returns:
        str: returns a text string with different characters and digits that
            make up the password.
    """
    for i in range(pwd_len):
        print(secrets.choice(ALL_CHARACTERS), end='')


generator_random_password(pwd_len)
