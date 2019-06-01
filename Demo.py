import Chegg as cg

print("\nDemo using paramterized constructor\n")
report = cg.CheggEarnings("chegg.html", "May", 15, 12, 30)
report.displayReport()


print("\nDemo using default constructor\n")
report2 = cg.CheggEarnings()
report2.displayReport()