from month import Month
from constants import daysInAMonth


class Year:
    def __init__(self, anuall):
        self.annual = anuall
        self.months = []
        self._ud_01jan = self.find01jan(anuall)
        self.weekday = self._ud_01jan

        for months in range(1, 13):
            month = Month(self.annual, months, self.weekday)
            self.months.append(month)
            # print(months, self.weekday)

            self.weekday = month.makeMonthCalendar()

    def getMonthList(self):
        return self.months

    def getMonth(self, month):
        return self.months[month - 1]

    def writeMnd(self, month):
        self.months[month - 1].print()

    def print(self):
        for month in self.months:
            month.print()

    def find01jan(self, anual):
        return 2


# year = Year(2020)

# year.print()

# for i in year.months:
#     print(i)
# print(year.months)
# year.months[5].print()
