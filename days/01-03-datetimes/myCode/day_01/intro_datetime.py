# Day 01
# Basics of date and datetimes
# 03.11.2023 Benjamin Zbinden

from datetime import datetime
from datetime import date

def pae(code):
    print(code)
    try:
        result = eval(code, globals())
        print(result)
    except Exception as e:
        print(f"Error: {e}")

print("datetime.today()")
print(datetime.today())
print("-------------------")
print("datetime(2018, 2, 24, 22, 17, 10, 244957)")
print(datetime(2018, 2, 24, 22, 17, 10, 244957))
print("-------------------")
print("date.today()")
print(date.today())
print("-------------------")
print("date(2023, 11, 1)")
print(date(2023,11, 1))
print("-------------------")
print("todaydate = date.today()")
todaydate = date.today()
print("todaydate.day")
print(todaydate.day)
print("todaydate.month")
print(todaydate.month)
print("todaydate.year")
print(todaydate.year)
print("-------------------")



print("\n"*2)
print("Math with Dates.")
print()

print("christmas = date(2023, 12, 24)")
christmas = date(2023, 12, 24)
print("christmas - todaydate")
print(christmas - todaydate)
print("(christmas - todaydate).days")
print((christmas - todaydate).days)

print()

print(""" 
if christmas is not todaydate:
    print(f"Sorry there are still {(christmas - todaydate).days} until Christmas!")
else:
    print("Yay it's Christmas!")
""")
if christmas is not todaydate:
    print(f"Sorry there are still {(christmas - todaydate).days} until Christmas!")
else:
    print("Yay it's Christmas!")
    
    
from datetime import timedelta
print("\n"*2)
print("Timedelta.")
print()

print("t = timedelta(days=4, hours=10)")
t = timedelta(days=4, hours=10)
print("type(t)")
print(type(t))

"pae = print and execute code"
pae("t.days")
pae("t.seconds")
print("t.seconds only shows the seconds from the 10 hours not the full 4days and 10hours !!!!!")
pae("t.hours")
print("When you want hours you need to calculate it.")
pae("t.seconds / 3600")

print("\n"*2)
print("Date add Timedelta.")
print()

print("eta = timedelta(days=1)")
eta = timedelta(days=1)
print("today = datetime.today()")
today = datetime.today()
pae("today")
pae("eta")
pae("today + eta")























