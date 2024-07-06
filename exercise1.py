import sys
from datetime import datetime


def get_days_from_today(date):
    try:
        datetime_object = datetime.strptime(date, "%Y.%m.%d")
        return (datetime.today() - datetime_object).days
    except ValueError:
        sys.stderr.write("Invalid date format. Please use YYYY.MM.DD\n")
        sys.exit(1)


print(get_days_from_today('202p.02.23'))
