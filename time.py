class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"
    
t1 = Time(12,50)
print(t1)
#You can call __str__() directly, but Python automatically calls it when you use print()

        