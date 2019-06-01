CheggEarnings

This is a tool that CheggTutors can use to easily calculate their total earnings from a specific period in time to the present, and get a tabulate report that breaks down total earnings by subject for this period.

Tutorial:

0) Save the html for the Earnings Archive you can finding on your chegg tutors "Past Lessons" tab.  You must click loadmore until you have all the data you want to use displayed.  (In v.2 this data will be scraped for you)

1) import the Chegg module.

import Chegg as cg


2) instantiate a Chegg Earnings object.

report = report.CheggEarnings("chegg.html","May", 15, 11, 30)

the constructor takes 4 paramaters, the first is the path to your saved html, the second is the starting month, the 3rd is the starting day (1-31), the 4th is the hour in military time (0-24), and the 5th is the minute (0-59)

**Note you can also call the default constructor, and the program will prompt you for this data when you call dispalyReport().  When it prompts you for the hour that should be given in standard time (0-12), as it will next ask you if it is am or pm.

report = report.CheggEarnings()

3) call report.displayReport()

-----------------------------------
below is sample input from the Demo and the displayed table

import Chegg as cg
report = cg.CheggEarnings()
report.displayReport()
Please enter the starting month (i.e January): May
Please enter the starting day (i.e 25): 12
Please enter the starting hour: 8
8 AM or 8PM? (am/pm) am
Please enter the starting minute: 0
Please enter the html file name: chegg.html
File successfully loaded


Total Earnings since Start time: may 12 8:00 AM : $353.34
Subject                            Total Earnings
Python Programming lessonwritten    100.0         
Computer Science lesson             171.67        
Java Programming lessonwritten      80.0          
PHP Programming lesson              1.67          
 