from datetime import datetime

final_year = int(input("Enter the final year: "))
current_year = datetime.now().year

leap_years = [year for year in range(current_year, final_year + 1)
              if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))]

print("Leap years:", leap_years)