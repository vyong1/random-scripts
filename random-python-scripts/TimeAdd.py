class Time:
    def __init__(self, hours, mins):
        self.hours = hours
        self.mins = mins
    
    def add(self, otherTime):
        self.hours += otherTime.hours
        self.hours += (self.mins + otherTime.mins) // 60
        self.mins = (self.mins + otherTime.mins)%60
        return self
    
    def __str__(self):
        if(self.mins < 10):
            return (str(self.hours) + ":0" + str(self.mins))
        else:
            return (str(self.hours) + ":" + str(self.mins))

t1 = Time(1, 45)
t2 = Time(8, 5)

print(t1.add(t2))