from constants import weekdays, months, daysInAMonth


class Date:
    def __init__(self, year, month, day, weekday):
        if month > 12 or day > 31 or weekday > 6:
            raise Exception('Date format is not correct.')
        self.year = year
        self.month = month
        self.day = day
        self.weekday = weekday

    def yearMonthDay(self):
        if self.month < 10:
            self.month = '0' + str(self.month)
        return str(self.year) + str(self.month) + str(self.day)

    def __str__(self):
        return weekdays[self.weekday] + ' ' + str(self.day) + '. ' + months[self.month] + ' ' + str(self.year)

    def __eq__(self, other):
        return other.yearMonthDay() == self.yearMonthDay()


# Just for testing...
# date = Date(2021, 10, 22, 4)
# date2 = Date(2021, 10, 21, 5)
# print(date == date2)
#
# print(date.yearMonthDay())
# print(date)
