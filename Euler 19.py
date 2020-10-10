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

year = 1901
month = 1
day = 1
weekday = 1
number_of_sundays = 0
final_year = 2000
final_month = 12
final_day = 31
feb = leap_check(year)

while year != final_year or month != final_month or day != final_day:
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day > 31:
            day -= 31
            month += 1
            if weekday == 6:
                number_of_sundays += 1
        if month > 12:
            year += 1
            feb = leap_check(year)
            month = 1
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            day -= 30
            month += 1
            if weekday == 6:
                number_of_sundays += 1
    else:
        if day > feb:
            day -= feb
            month += 1
            if weekday == 6:
                number_of_sundays += 1
    day += 1
    weekday += 1
    if weekday > 6:
        weekday = 0

print (number_of_sundays)#anser