# pandas-ladder

This project demonstrates how to use Pandas to first create a timeseries binning dataframe which is first grouped and aggregated accordingly by a number of columns. 

The dataset is then pivoted through the stack() method. 

## Sample data
The sample data for this project is a dictionary made up of three lists:
```
data = {
    'date': ['2017-09-01', '2017-09-01', '2017-10-08', '2018-01-02', '2018-02-02', '2018-05-02', '2019-01-03', '2018-05-03', '2018-05-04', '2019-05-04'],
    'score': [34, 25, 26, 15, 15, 14, 26, 25, 62, 41],
    'colors': ['r', 'b', 'g', 'r', 'b', 'g', 'r', 'b', 'g', 'g']
}
```

## How it works
### Cutting the dataframe to build the bins (buckets) by timeseries
After converting the time periods into numpy datetime64 format, the Pandas cut() method is used to build the bins:
```
df['categories'] = pd.cut(df.index, list(map(datetup, bins)), labels=date_bins_labels)
```

At this stage the data looks like this:
```
            score colors categories
date
2017-09-01     34      r      Alpha
2017-09-01     25      b      Alpha
2017-10-08     26      g      Alpha
2018-01-02     15      r      Alpha
2018-02-02     15      b      Alpha
2018-05-02     14      g       Beta
2019-01-03     26      r      Omega
2018-05-03     25      b       Beta
2018-05-04     62      g       Beta
2019-05-04     41      g      Omega
```


### Grouping, aggregating and transposing
Pandas allows us to group by multiple columns. This feature allows us to produce the dataframe as per below:
```
colors         b                 g                 r
categories Alpha  Beta Omega Alpha  Beta Omega Alpha Beta Omega
score       40.0  25.0   NaN  26.0  76.0  41.0  49.0  NaN  26.0
```

### Converting the dataset into a pivot table
Our goal for this project was to build a pivot table that produces colors an categories on the x- and y- axis respectively while getting the aggregate score in the cell (and filling 0 where there is no value). 

This is done by using the stack() for reshape, then remove first level with score if necessary by reset_index() and last replace NaNs to 0 and cast to int:
```
categories  Alpha  Beta  Omega
colors
b              40    25      0
g              26    76     41
r              49     0     26
```
