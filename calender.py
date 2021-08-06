from year import Year
from date import Date


class Calendar:
    def __init__(self, startYear, endYear):
        self.startYear = startYear
        self.endYear = endYear

        self.yearObjects = {}

        for year in range(startYear, endYear + 1):
            # print('Year is:', year)
            self.yearObjects[str(year)] = Year(year)

    def getDate(self, date):
        date_split_year = date[0] + date[1] + date[2] + date[3]
        date_split_month = date[4] + date[5]
        date_split_day = date[6] + date[7]

        year = self.yearObjects[date_split_year]
        month = year.getMonth(int(date_split_month))
        day = month.getDate(int(date_split_day))
        print(day)
        weekday = month.fud + day % 7

        return Date(int(date_split_year), int(date_split_month), int(date_split_day), weekday)



        # correct = Date(int(date_split_year), int(date_split_month), int(date_split_day), 0)
        # print(correct.yearMonthDay())

        # if Year(date_split_year) in self.yearObjects.values():
        # if date_split_year in self.yearObjects.keys():
        #     yearObject = self.yearObjects.get(date_split_year)
        #     for month in yearObject.months:
        #         if month(date_split_day, date_split_month, date_split_day, 1) ==
        #
            # monthbject = yearObject.months
            # print(yearObject)
            # # return)
            # return date_split_year.YearMonthDay(date_split_year, date_split_month, date_split_day)
        # else:
        #     print('Date not in calendar.')

    def getYear(self, year):
        date_split_year = year[0] + year[1] + year[2] + year[3]

        if date_split_year in self.yearObjects.keys():
            return self.yearObjects.get(date_split_year)
        else:
            print('Year not in calendar.')

    def findDays(self, date, integer):
        pass

    def calculateMovingHolydays(self):
        pass


calendar = Calendar(2000, 2020)
calendar.getDate('20150517')


# for keys, values in calendar.yearObjects.items():
#     print(keys, values.annual)
#

# print(calendar.getDate("20150517"))
#
# for values in calendar.yearObjects.values():
#     print(values)
#
# if '2015' in calendar.yearObjects.values():
#     print('Gotcha!')
# else:
#     print('Damn.')

# print(calendar.yearObjects.Year.months())
