import re


def is_leap(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        return True
    return False


date_dmy_regex = re.compile(r'''
                        (0?[1-9]|[1-2][0-9]|3[0-1]) #day
                        ([/.-])
                        (0?[1-9]|1[0-2]) #month
                        ([/.-])
                        ([1-2]\d{3}) #year
                        ''', re.VERBOSE)

date_mdy_regex = re.compile(r'''
                        (0?[1-9]|1[0-2]) #month
                        ([/.-])
                        (0?[1-9]|[1-2][0-9]|3[0-1]) #day
                        ([/.-])
                        ([1-2]\d{3}) #year
                        ''', re.VERBOSE)

date_ydm_regex = re.compile(r'''
                        ([1-2]\d{3}) #year
                        ([/.-])
                        (0?[1-9]|[1-2][0-9]|3[0-1]) #day
                        ([/.-])
                        (0?[1-9]|1[0-2]) #month
                        ''', re.VERBOSE)

while True:
    frmt = input('Choose which format you are interested in (dmy/mdy): ').lower()
    if frmt != 'dmy' and frmt != 'mdy':
        print('Enter correct format!')
    else:
        break
month, day, year = 0, 0, 0
if frmt == 'mdy':
    rg = date_mdy_regex.search('04.20.1998')
    month = int(rg.group(1))
    day = int(rg.group(3))
else:
    rg = date_dmy_regex.search('20.04.1998')
    day = int(rg.group(1))
    month = int(rg.group(3))
year = int(rg.group(5))

if month in [4, 6, 9, 11] and day > 30:
    print('invalid')
elif month == 2 and day > 29:
    print('invalid')
elif month == 2 and day > 28 and not is_leap(year):
    print('invalid')
else:
    proper_format = '-'.join(map(lambda x: str(x), [day, month, year]))
    print(proper_format)
