from datetime import date, timedelta

def add_years_to_date(original_date, years_to_add):
    try:
        return original_date.replace(year=original_date.year + years_to_add)
    except ValueError:
        days_in_february = 29 if is_leap_year(original_date.year + years_to_add) else 28
        last_day_of_february = date(original_date.year + years_to_add, 2, days_in_february)
        return last_day_of_february
        

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
