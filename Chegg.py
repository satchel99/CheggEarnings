from bs4 import BeautifulSoup
import Date
class CheggEarnings:
    divClass = "_2xTaIdfehw4CRQbxJPJuqd"
    divClassF2 = "_2e5gl6unh78qrgnE07iC_4"
    earningsSpan = "_6zAgqawnLfo40Z0WHSMP"
    divClassF3 = "_2nSEqu1xa2RyEpFtUeUEKO"
    dateSpan = "QsltVrwi2CdqNHh2i0CCG"
    timeSpan = "_3y718_qjIakYRQvvYbDWYl"
    lessonSpan = "_1unvSMVXylLS3U1rdi1fHU"
    def __init__(self, filename=None, month=None, day=None, time=None, minute=None):
        self.filename = filename
        if((month != None) and (day != None) and (time != None) and (minute != None)):
            self.date = Date.Date(month, day, time, minute)
        else:
            self.date = None
    def parseData(self):
        f = open(self.filename, "r")
        soup = BeautifulSoup(f, 'html.parser')
        mydivs = soup.findAll("div", {"class": CheggEarnings.divClass})
        data = makeDicList(mydivs, CheggEarnings.divClassF2, CheggEarnings.earningsSpan, CheggEarnings.divClassF3, CheggEarnings.dateSpan, CheggEarnings.timeSpan, CheggEarnings.lessonSpan)
        cleanedData = cleanData(data)
        return cleanedData
    def displayReport(self):
        if(self.date == None):
            self.loadDates()
        if(self.filename == None):
            self.loadFile()
        self.report()
    def loadFile(self):
        file = input("Please enter the html file name: ")
        try:
            f = open(file, "r")
            f.close()
            self.filename = file
            print("File successfully loaded")
        except:
            print("File was not found")
    def loadDates(self):
        month = input("Please enter the starting month (i.e January): ")
        day = int(input("Please enter the starting day (i.e 25): "))
        hour = int(input("Please enter the starting hour: "))
        am = input(str(hour) + " AM or " + str(hour) + "PM? (am/pm) ")
        minute = int(input("Please enter the starting minute: "))
        if(am.lower() == "pm"):
            hour+=12
        self.date = Date.Date(month, day, hour, minute)
    def report(self):
        data = self.parseData()
        totalEarnings = 0
        earningsBySubj = {}
        for i in data:
            if(self.date < i["date"]):
                if(i["earnings"] != -1):
                    totalEarnings+=i["earnings"]
                    if(i["lessonType"] in earningsBySubj):
                        earningsBySubj[i["lessonType"]] = earningsBySubj[i["lessonType"]] + i["earnings"]
                    else:
                        earningsBySubj[i["lessonType"]] = i["earnings"]
        print("\n")
        print("Total Earnings since " + str(self.date) + " : $%.2f" % totalEarnings)
        print("\n")
        print("{:<35}{:<14}".format('Subject','Total Earnings'))
        for subj in earningsBySubj:
            earnings = float("{0:.2f}".format(earningsBySubj[subj]))
            print("{:<35} {:<14}".format(subj, earnings))
                
def makeDicList(l, d2, earningsSpan, d3, dateSpan, timeSpan, lessonSpan):
    allLessons = []
    for i in l:
        cell = i.find("div", {"class": d2})
        earnt = cell.find("span", {"class" : earningsSpan}).get_text()
        leftCell = cell.find("div", {"class" : d3})
        dS = leftCell.find("span", {"class" : dateSpan}).get_text()
        tS = leftCell.find("span", {"class" : timeSpan}).get_text()
        lS = leftCell.find("span", {"class" : lessonSpan}).get_text()
        allLessons.append({"lessonType" : lS, "earned" : earnt, "date" : dS, "time" : tS})
    return allLessons

def isolateDate(i):
    dateList = i["date"].split(" ")
    month = dateList[0]
    day = dateList[1]
    timeStr = i["time"].split(" ")[0]
    am = i["time"].split(" ")[1]
    timeList = timeStr.split(":")
    hour = timeList[0]
    minute = timeList[1]
    if(am == "AM"):
        hour = int(hour)
    else:
        hour = int(hour) + 12
    minute = int(minute)
    day = int(day)
    dateObj = Date.Date(month, day, hour, minute)
    return dateObj

def isolateEarnings(i):
    if(i["earned"] == "Void"):
        return -1
    else:
        return float(i["earned"][1:])
def cleanData(data):
    cleaned = []
    for i in data:
        dateObj = isolateDate(i)
        earnings = isolateEarnings(i)
        newobj = {"date" : dateObj, "earnings" : earnings, "lessonType" : i["lessonType"]}
        cleaned.append(newobj)
    return cleaned
        
        

    

