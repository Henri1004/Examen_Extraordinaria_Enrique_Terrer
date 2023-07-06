import math


def power_of_4(num):
    if str(num).isnumeric() != True:
        return False
    else:
        if num < 0:
            return False
        else:
            while True:
                if num/4 == 1:
                    return True
                elif num/4 < 1:
                    return False
                elif num/4 > 1:
                    num = num/4
                continue

print(power_of_4(1024))
