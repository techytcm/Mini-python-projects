from datetime import date

year = int(input("Enter event year: "))
month = int(input("Enter event month: "))
day = int(input("Enter event day: "))

event_date = date(year, month, day)
today = date.today()

difference = event_date - today

if difference.days > 0:
    print(f"\nThe event is {difference.days} days away! ")
elif difference.days == 0:
    print("\nThe event is today!")
else:
    print(f"\nThe event was {-difference.days} days ago.")