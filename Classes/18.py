# Write a Python class named Time with two attributes: hours and minutes. Include a method to add two time objects.
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def add_time(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours + total_minutes // 60
        total_minutes %= 60
        return Time(total_hours, total_minutes)

t1 = Time(2, 45)
t2 = Time(1, 30)
t3 = t1.add_time(t2)
print(f"{t3.hours} hours, {t3.minutes} minutes")
