class Time:
    def __init__(self, hours, minutes) -> None:
        self.hours = hours
        self.minutes = minutes
    def addTime(self, timeX):
        total_hours = self.hours + timeX.hours
        total_minutes = self.minutes + timeX.minutes
        additional_hours = total_minutes//60
        total_hours+=additional_hours
        total_minutes = total_minutes % 60
        return Time(total_hours, total_minutes)
    
    def displayTime(self):
        print(f"The time is {self.hours} hrs and {self.minutes} minutes.")

    def displayMinute(self):
        total_minutes = self.hours*60 + self.minutes
        print(f"The total minutes are {total_minutes}")



print("Enter time 1: ")
hr1 = int(input("Hours: "))
mn1 = int(input("Minutes: "))
t1 = Time(hr1,mn1)

print("Enter time 2: ")
hr2 = int(input("Hours: "))
mn2 = int(input("Minutes: "))
t2 = Time(hr2,mn2)

t1.displayTime()
t2.displayTime()

t3 = t1.addTime(t2)

t3.displayMinute()

t3.displayTime()