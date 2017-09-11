import re
from datetime import date
from dateutil.relativedelta import relativedelta

date_bins = "6d,3m,5y"
start_date = date.today()
bins = [start_date,]

for period_bin in date_bins.split(","):
    print(period_bin)
    if period_bin[-1] == 'd':
        period_bin = int(period_bin[:-1])
        new_date = start_date+relativedelta(days =+ period_bin)
    elif period_bin[-1] == 'm':
        period_bin = int(period_bin[:-1])
        new_date = start_date+relativedelta(months =+ period_bin)
    elif period_bin[-1] == 'y':
        period_bin = int(period_bin[:-1])
        new_date = start_date+relativedelta(years =+ period_bin)
    else:
        period_bin = int(period_bin[:-1])
        new_date = start_date+relativedelta(years =+ period_bin)
    bins.append(new_date)

print("new_date: ", bins)