import string

class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, username, char, position):
        self._username = username
        self._char = char
        self._position = position

    def __str__(self):
        return "The username '%s' contains an illegal character '%s' at position %d. It should contain only English letters, numbers, and _." % (self._username, self._char, self._position)


class UsernameTooShort(Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        return "The username '%s' is too short. It must contain more than 2 characters." % self._username


class UsernameTooLong(Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        return "The username '%s' is too long. It must contain less than 17 characters." % self._username


class PasswordTooShort(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "The password '%s' is too short. It must contain more than 8 characters." % self._password


class PasswordTooLong(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "The password '%s' is too long. It must contain less than 41 characters." % self._password


class PasswordMissingCharacter(Exception):
    def __init__(self, password):
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
    פונקציה שבודקת שם משתמש וסיסמה ועומדת בתנאים שהוצגו.

    Args:
        username: שם המשתמש (מחרוזת).
        password: הסיסמה (מחרוזת).

    Returns:
        None
    """

    # בדיקת שם משתמש
    if not is_valid_username(username):
        print("Username not valid")
        return False

    # בדיקת סיסמה
    elif not is_valid_password(password):
        print("Password not valid")
        return False

    # שם משתמש וסיסמה תקינים
    else:
        print("OK")
        return True


def is_valid_username(username):
    """
    פונקציה שבודקת שם משתמש תקין.

    Args:
        username: שם המשתמש (מחרוזת).

    Returns:
        True אם שם המשתמש תקין, False אחרת.
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
    function that chceks if the password

    Args:
        password: str

    Returns:
        True אם הסיסמה תקינה, False אחרת.
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
