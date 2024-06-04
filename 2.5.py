import string

class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, username, char, position):
        """
        Initialize a new UsernameContainsIllegalCharacter exception.

        :param username: The username that contains an illegal character.
        :param char: The illegal character found in the username.
        :param position: The position of the illegal character in the username.
        :type username: str
        :type char: str
        :type position: int
        """
        self._username = username
        self._char = char
        self._position = position

    def __str__(self):
        return "The username '%s' contains an illegal character '%s' at position %d. It should contain only English letters, numbers, and _." % (self._username, self._char, self._position)


class UsernameTooShort(Exception):
    def __init__(self, username):
        """
        Initialize a new UsernameTooShort exception.

        :param username: The username that is too short.
        :type username: str
        """
        self._username = username

    def __str__(self):
        return "The username '%s' is too short. It must contain more than 2 characters." % self._username


class UsernameTooLong(Exception):
    def __init__(self, username):
        """
        Initialize a new UsernameTooLong exception.

        :param username: The username that is too long.
        :type username: str
        """
        self._username = username

    def __str__(self):
        return "The username '%s' is too long. It must contain less than 17 characters." % self._username


class PasswordTooShort(Exception):
    def __init__(self, password):
        """
        Initialize a new PasswordTooShort exception.

        :param password: The password that is too short.
        :type password: str
        """
        self._password = password

    def __str__(self):
        return "The password '%s' is too short. It must contain more than 8 characters." % self._password


class PasswordTooLong(Exception):
    def __init__(self, password):
        """
        Initialize a new PasswordTooLong exception.

        :param password: The password that is too long.
        :type password: str
        """
        self._password = password

    def __str__(self):
        return "The password '%s' is too long. It must contain less than 41 characters." % self._password


class PasswordMissingCharacter(Exception):
    def __init__(self, password):
        """
        Initialize a new PasswordMissingCharacter exception.

        :param password: The password that is missing a required character.
        :type password: str
        """
        self._password = password

    def __str__(self):
        return "The password '%s' is missing a required character." % self._password


class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"


class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"


class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"


def check_input(username, password):
    """
    Function to check if the username and password meet the specified criteria.

    :param
        username: The username .
        password: The password .

    :type
        username: str
        password: str
    """

    # Check username
    if not is_valid_username(username):
        print("Username not valid")
        return False

    # Check password
    elif not is_valid_password(password):
        print("Password not valid")
        return False

    # Username and password are valid
    else:
        print("OK")
        return True


def is_valid_username(username):
    """
    Check if the username is valid.

    :param username: The username to be checked.
    :type username: str
    :returns: True if the username is valid, False otherwise.
    :rtype: bool
    :raises UsernameTooShort: If the username is too short.
    :raises UsernameTooLong: If the username is too long.
    :raises UsernameContainsIllegalCharacter: If the username contains an illegal character.
    """
    try:
        if len(username) < 3:
            raise UsernameTooShort(username)
        if len(username) > 16:
            raise UsernameTooLong(username)

        allowed_chars = string.ascii_letters + string.digits + "_"
        for position, char in enumerate(username):
            if char not in allowed_chars:
                raise UsernameContainsIllegalCharacter(username, char, position)

    except (UsernameTooShort, UsernameTooLong, UsernameContainsIllegalCharacter) as e:
        print(e)
        return False
    else:
        return True


def is_valid_password(password):
    """
    Check if the password is valid.

    :param password: The password to be checked.
    :type password: str
    :returns: True if the password is valid, False otherwise.
    :rtype: bool
    :raises PasswordTooShort: If the password is too short.
    :raises PasswordTooLong: If the password is too long.
    :raises PasswordMissingUppercase: If the password is missing an uppercase letter.
    :raises PasswordMissingLowercase: If the password is missing a lowercase letter.
    :raises PasswordMissingDigit: If the password is missing a digit.
    :raises PasswordMissingSpecial: If the password is missing a special character.
    """
    try:
        if len(password) < 8:
            raise PasswordTooShort(password)
        if len(password) > 40:
            raise PasswordTooLong(password)

        has_uppercase = False
        has_lowercase = False
        has_digit = False
        has_special = False

        for char in password:
            if char.isupper():
                has_uppercase = True
            elif char.islower():
                has_lowercase = True
            elif char.isdigit():
                has_digit = True
            elif char in string.punctuation:
                has_special = True

        if not has_uppercase:
            raise PasswordMissingUppercase(password)
        if not has_lowercase:
            raise PasswordMissingLowercase(password)
        if not has_digit:
            raise PasswordMissingDigit(password)
        if not has_special:
            raise PasswordMissingSpecial(password)

    except (PasswordTooShort, PasswordTooLong, PasswordMissingCharacter) as e:
        print(e)
        return False
    else:
        return True


if __name__ == '__main__':
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    while not check_input(username, password):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
