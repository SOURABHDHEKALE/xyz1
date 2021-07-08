# alternative constructor

class date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


@classmethod
    def from_dash(cls, string):
         return cls(*string.split("-"))

date1 = date.from_dash("2021-07-04")

print(date.year)
print(date.month)
