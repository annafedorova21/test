def days_between_dates(date1, date2):
    year1, month1, day1 = map(int, date1.split('-'))
    year2, month2, day2 = map(int, date2.split('-'))

    days1 = day1 + 31 * (month1 - 1) + 365 * (year1 - 1) + (year1 - 1) // 4 - (year1 - 1) // 100 + (year1 - 1) // 400
    days2 = day2 + 31 * (month2 - 1) + 365 * (year2 - 1) + (year2 - 1) // 4 - (year2 - 1) // 100 + (year2 - 1) // 400

    diff_days = days2 - days1

    return abs(diff_days)


def remove_digits(num, k):
    n = len(num)
    mystack = []

    for c in num:
        while (len(mystack) > 0 and k > 0 and ord(mystack[len(mystack) - 1]) > ord(c)):
            mystack.pop()
            k -= 1

        if len(mystack) > 0 or c != '0':
            mystack.append(c)

    while len(mystack) > 0 and k:
        mystack.pop()
        k -= 1
    if len(mystack) == 0:
        return "0"

    num = list(num)
    while (len(mystack) > 0):
        num[n - 1] = mystack[len(mystack) - 1]
        mystack.pop()
        n -= 1
    return "".join(num[n:])
