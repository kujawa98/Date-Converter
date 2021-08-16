import re


def is_leap(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        return True
    return False


def create_dmy_regex():
    date_dmy_regex = re.compile(r'''
                            (0[1-9]|[1-2][0-9]|3[0-1]) #day
                            ([/.-])
                            (0[1-9]|1[0-2]) #month
                            ([/.-])
                            ([1-2]\d{3}) #year
                            ''', re.VERBOSE)
    return date_dmy_regex


def create_mdy_regex():
    date_mdy_regex = re.compile(r'''
                            (0[1-9]|1[0-2]) #month
                            ([/.-])
                            (0[1-9]|[1-2][0-9]|3[0-1]) #day
                            ([/.-])
                            ([1-2]\d{3}) #year
                            ''', re.VERBOSE)
    return date_mdy_regex


def create_ymd_regex():
    date_ydm_regex = re.compile(r'''
                            ([1-2]\d{3}) #year
                            ([/.-])
                            (0?[1-9]|1[0-2]) #month
                            ([/.-])
                            (0?[1-9]|[1-2][0-9]|3[0-1]) #day
                            ''', re.VERBOSE)
    return date_ydm_regex


def valid_date(day, month, year):
    if month in [4, 6, 9, 11] and day > 30:
        return False
    elif month not in [2, 4, 6, 9, 11] and day > 31:
        return False
    elif month == 2 and 28 < day <= 29 and not is_leap(year):
        return False
    return True


def take_input():
    while True:
        frmt = input('Choose which format you are interested in (dmy/mdy/ymd): ').lower()
        if frmt != 'dmy' and frmt != 'mdy' and frmt != 'ymd':
            print('Enter correct format!')
        else:
            return frmt


def process(dates, reg, order):
    for date in dates:
        try:
            wn = reg.search(date)
            day = int(wn.group(order[0]))
            month = int(wn.group(order[1]))
            year = int(wn.group(order[2]))
            print_dates(day, month, year)
        except AttributeError:
            pass


def print_dates(day, month, year):
    if valid_date(day, month, year):
        proper_format = '-'.join(map(lambda x: str(x), [day, month, year]))
        print(proper_format)


def main():
    frmt = take_input()
    f = open('dates.txt', 'r')
    dates = f.readlines()
    dates = map(lambda x: x.rstrip(), dates)
    if frmt == 'mdy':
        reg = create_mdy_regex()
        process(dates, reg, (3, 1, 5))
    elif frmt == 'ymd':
        reg = create_ymd_regex()
        process(dates, reg, (5, 3, 1))
    else:
        reg = create_dmy_regex()
        process(dates, reg, (1, 3, 5))
    f.close()


if __name__ == '__main__':
    main()
