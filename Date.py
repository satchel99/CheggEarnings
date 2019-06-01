class Date: 
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "dec", "nov"]
    def __init__(self):
        self.startMonth = ""
        self.startDay = 0
        self.startTime = 8
        self.startMinute = 0
    def __init__(self, month, day, time, minute):
        self.startMonth = ""
        self.startDay = 0
        self.startTime = 8
        self.startMinute = 0
        self.setMonth(month)
        self.setDay(day)
        self.setTime(time)
        self.setMinute(minute)
    def setMonth(self, month):
        if(month.lower()[:3] in Date.months):
            self.startMonth = month.lower()[:3]
        else:
            raise ValueError("Invalid month")
    def setDay(self, day):
        if((isinstance(day, int)) and ((0 < day) and (day <= 31))):
            self.startDay = day
        else:
            raise ValueError("Invalid day")
    def setTime(self, time):
        if((isinstance(time, int)) and ((0 <= time) and (time <= 24))):
            self.startTime = time
        else:
            raise ValueError("Invalid time")
    def setMinute(self, minute):
        if((isinstance(minute, int)) and ((0 <= minute) and (minute <= 59))):
            self.startMinute = minute
        else:
            raise ValueError("Invalid minute")
    def __lt__ (self, other):
        if Date.months.index(self.startMonth) < Date.months.index(other.startMonth):
            return True
        elif Date.months.index(self.startMonth) > Date.months.index(other.startMonth):
            return False
        else:
            if(self.startDay < other.startDay):
                return True
            elif(self.startDay > other.startDay):
                return False
            else:
                if(self.startTime < other.startTime):
                    return True
                elif(self.startTime > other.startTime):
                    return False
                else:
                    if(self.startMinute < other.startMinute):
                        return True
                    else:
                        return False
    def __str__(self):
        minStr = ""
        if(self.startMinute < 10):
            minStr = "0" + str(self.startMinute)
        else:
            minStr = str(self.startMinute)
        timeStr = ""
        if(self.startTime < 12):
            timeStr = str(self.startTime) + ":" + minStr + " AM"
        else:
            timeStr = str(self.startTime - 12) + ":" + minStr + " PM"
        return ("Start time: " + str(self.startMonth) + " " + str(self.startDay) + " " + timeStr)
