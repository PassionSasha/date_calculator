import datetime
from calendar import monthrange


# func for calculating datetime
def add_days(date, num_of_days):
    day, month, year = tuple(map(lambda x: int(x), date.split('.')))
    for i in range(num_of_days):
        # algorithm for leap year

        if day < monthrange(year, month)[1]:
            day, month, year = day + 1, month, year
        else:
            if month == 12:
                day, month, year = 1, 1, year + 1
            else:
                day, month, year = 1, month + 1, year

    print(f'Output date - {day}.{month}.{year}')


def add_days_datetime(date, num_of_days):
    current_date = datetime.datetime.strptime(date, "%d.%m.%Y")
    new_date = current_date + datetime.timedelta(days=num_of_days)
    print(f'Output date with datetime lib - {new_date}')


add_days('24.08.2000', 3)
add_days('05.03.1974', 100)
add_days('14.07.1976', 6000)
add_days('15.04.1999', 6765)
add_days('1.2.2000', 500)

add_days_datetime('24.08.2000', 3)
add_days_datetime('05.03.1974', 100)
add_days_datetime('14.07.1976', 6000)
add_days_datetime('15.04.1999', 6765)
add_days_datetime('1.2.2000', 500)

