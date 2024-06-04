class IDIterator:
    """
       Iterate over valid ID numbers.

       :param id: The starting ID number.
       :type id: int
       :returns: An iterator over valid ID numbers.
       :rtype: iterator
       :raises StopIteration: If the ID number exceeds the maximum value.
       """
    def __init__(self, id):
        self._id = id

    def get_name(self):
        return self._id

    def __iter__(self):
        return self

    def __next__(self):
        if self._id > 999999999:
            raise StopIteration

        while not check_id_valid(self._id):
            self._id += 1
            if self._id > 999999999:
                raise StopIteration

        result = self._id
        self._id += 1
        return result


def multi(num, index):
    """
        Multiply the number by 2 if the index is odd.

        :param num: The number to be multiplied.
        :type num: int
        :param index: The index of the number.
        :type index: int
        :returns: The multiplied number.
        :rtype: int
        """
    if index % 2 == 0:
        return num
    else:
        return num * 2


def check_id_valid(id_number):
    """
       Check if the ID number is valid.

       :param id_number: The ID number to be checked.
       :type id_number: int
       :returns: True if the ID number is valid, False otherwise.
       :rtype: bool
       """
    id_str = str(id_number).zfill(9)

    id_digits = [int(digit) for digit in id_str]
    multiplied = list(map(multi, id_digits, range(len(id_digits))))
    total = sum(sum(divmod(num, 10)) for num in multiplied)
    return total % 10 == 0


def id_generator(start_id):
    """
        Generate valid ID numbers starting from the given start_id.

        :param start_id: The starting ID number.
        :type start_id: int
        :returns: The next valid ID number.
        :rtype: int
        """
    id_number = start_id
    while id_number <= 999999999:
        if check_id_valid(id_number):
            yield id_number
        id_number += 1


if __name__ == '__main__':
    print(check_id_valid(123456780))
    user_id = int(input("Enter ID: "))
    result = input("Generator or Iterator? (gen/it)? ")
    if result == "it":
        new_iter = IDIterator(user_id)
        for i in range(10):
            print(next(new_iter))
    elif result == "gen":
        id_gen = id_generator(user_id)
        for _ in range(10):
            print(next(id_gen))
