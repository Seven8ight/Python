import math

class DateCalculator:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def calculate(self):

        if self.month == 1 or self.month == 2:
            self.year -= 1
            if self.month == 1:
                self.month = 13
            else:
                self.month = 14
        
        q = self.day
        K = self.year % 100
        J = self.year // 100

        return (q + ((13 * (self.month + 1)) / 5) + K + (K / 4) + (J / 4) + 5 * J) % 7
    
dateCalc:DateCalculator = DateCalculator(2025,1,18)

print(math.floor(dateCalc.calculate()))
