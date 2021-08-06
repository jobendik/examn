from constants import daysInAMonth
from date import Date


class Month:
    def __init__(self, year, month, fud):
        if month > 12 or fud > 6:
            raise Exception('Month format is not correct.')
        self.year = year
        self.month = month - 1
        # if month == 12:
        #     month += 1
        self.fud = fud

        self.listOfDates = []

    def makeMonthCalendar(self):
        first_weekday = self.fud
        # print(self.month)
        if self.year % 4 == 0 and self.month == 1:
            # print('Leap Year!')
            daysInAMonth[1] = 29

        for days in range(1, daysInAMonth[self.month] + 1):
            self.listOfDates.append(Date(self.year, self.month, days, first_weekday))
            first_weekday += 1
            if first_weekday > 6:
                first_weekday = 0
        daysInAMonth[1] = 28

        return first_weekday

    def retreaveDates(self):
        return self.listOfDates

    def getDate(self, d):
        return self.listOfDates[d - 1]

    def print(self):
        for date in self.listOfDates:
            print(date)


# month = Month(2020, 3, 5)
# month.makeMonthCalendar()
# month.print()
#
#
# month = Month(2020, 2, 5)
# month.makeMonthCalendar()
# month.print()

# print(month.makeMonthCalendar())
# print(month.getDate(17))
# mai_21 = Month(2021, 5, 5)  # (årstall, mnd_nr, ukedag for den 1. i måneden)
# mai_21.print()
# print(mai_21)
