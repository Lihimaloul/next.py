def gen_secs():
    """
    Generate seconds from 0 to 59.
    """
    for sec in range(60):
        yield sec


def gen_minutes():
    """
    Generate minutes from 0 to 59.
    """
    for min in range(60):
        yield min


def gen_hours():
    """
       Generate hours from 0 to 23.
       """
    for hours in range(24):
        yield hours


def gen_time():
    """
       Generate time in HH:MM:SS format.
       """
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, sec)


def gen_years(start=2019):
    """
       Generate years starting from the given start year.

       :param start: The starting year.
       :type start: int
       :returns: The next year.
       :rtype: int
       """
    year = start
    while True:
        yield year
        year += 1


def gen_months():
    """
      Generate months from 1 to 12.
      """
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    """
       Generate days in the given month.

       :param month: The month.
       :type month: int
       :param leap_year: Flag indicating whether it's a leap year.
       :type leap_year: bool
       :returns: The next day in the month.
       :rtype: int
       """
    days_in_month = {
        1: 31,
        2: 29 if leap_year else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    for day in range(1, days_in_month[month] + 1):
        yield day


def is_leap_year(year):
    """
       Check if the given year is a leap year.

       :param year: The year to check.
       :type year: int
       :returns: True if the year is a leap year, False otherwise.
       :rtype: bool
       """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def gen_date():
    """
        Generate dates in the format 'DD/MM/YYYY HH:MM:SS'.
        """
    for year in gen_years():
        for month in gen_months():
            leap_year = is_leap_year(year)
            for day in gen_days(month, leap_year):
                for hour in gen_hours():
                    for minute in gen_minutes():
                        for sec in gen_secs():
                            yield f"{day:02d}/{month:02d}/{year:04d} {hour:02d}:{minute:02d}:{sec:02d}"


if __name__ == '__main__':
    gen = gen_date()
    for _ in range(100):  # הפקת והדפסת 100 החתימות הראשונות של התאריכים
        print(next(gen))
    # דוגמה לשימוש
    gen = gen_date()
    for i in range(1, 1000001):
        next_value = next(gen)
        if i % 1000000 == 0:
            print(next_value)