from datetime import date

# Get birth date
year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))

birth_date = date(year, month, day)
today = date.today()

# Calculate age
age = today.year - birth_date.year

# Check if birthday has happened this year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print(f"\nYou are {age} years old.")