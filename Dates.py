def leap_check(year):
    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True

    if leap:
        return 29
    else:
        return 28

year = 2020
month = 10
day = 9
k = 200069
day += k
feb = leap_check(year)#dfcc

while day > 28:
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day > 31:
            day -= 31
            month += 1
        else:
            break
        if month > 12:
            year += 1
            feb = leap_check(year)
            month = 1
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            day -= 30
            month += 1
        else:
            break
    else:
        if day > feb:
            day -= feb
            month += 1

print (year, month, day)
