import re


def is_valid_time(time):
    time_pattern = re.compile(r'([0-9]{1,2}):([0-9]{1,2})')
    result = time_pattern.fullmatch(time)
    if result:
        return True
    return False


print(is_valid_time('459:15'))
