import re

date_dmy_regex = re.compile(r'''
                        (0?[1-9]|[1-2][0-9]|3[0-1]) #day
                        ([/.-])
                        (0?[1-9]|1[0-2]) #month
                        ([/.-])
                        ([1-2]\d{3}) #year
                        ''', re.VERBOSE)

rg = date_dmy_regex.search('02/02/1998')
print(rg.group())
