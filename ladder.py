from datetime import date
from dateutil.relativedelta import relativedelta
import numpy as np
import pandas as pd

def generate_df(df, start_date, date_bins, date_bins_labels):
    """
    Build a ladder based on the provided timeseries bins.
    
    Keyword arguments:
    df                  -- dataframe to process
    start_date          -- starting date
    date_bins           -- date bins that take the start_date as delta reference
    date_bins_labels    -- labels for the date bins
    """

    bins = [start_date,]
    datetup = lambda x:np.datetime64(x)
    df = pd.DataFrame(data, columns = ['date', 'score', 'colors'])
    df['date'] = pd.to_datetime(df['date'])
    df.set_index(['date'], inplace=True)

    for period_bin in date_bins:
        new_date = start_date+relativedelta(months =+ period_bin)
        bins.append(new_date)

    df['categories'] = pd.cut(df.index, list(map(datetup, bins)), labels=date_bins_labels)

    return df

def timeseries_binning(df):
    dx = df.groupby(['categories']).sum().transpose()
    return dx

def group_df(df, group_by):
    """
    df          -- dataframe to process
    group_by    -- how the aggregate df will be grouped
    """
    dy = df.groupby([group_by, 'categories']).sum().transpose()
    dz = dy.stack(0).reset_index(level=0, drop=True).fillna(0).astype(int)
    return dz

data = {
    'date': ['2017-09-01', '2017-09-01', '2017-10-08', '2018-01-02', '2018-02-02', '2018-05-02', '2019-01-03', '2018-05-03', '2018-05-04', '2019-05-04'],
    'score': [34, 25, 26, 15, 15, 14, 26, 25, 62, 41],
    'colors': ['r', 'b', 'g', 'r', 'b', 'g', 'r', 'b', 'g', 'g']
}

date_now = date.today()
bins = [6,12,999]
labels = ['Alpha', 'Beta', 'Omega']

lad1 = generate_df(data, date_now, bins, labels)
print(lad1)

lad2 = timeseries_binning(lad1)
print(lad2)

lad3 = group_df(lad1, 'colors')
print(lad3)