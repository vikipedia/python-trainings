day1
====

- Operating on tabular data using pandas
    - Series, Dataframe
    - Access patterns , selecting
    - Filtering
    - Merging, joining, concatenating
    - groupby
    - reading/writing datasets using pandas


Spreadsheet Of Python
---------------------

Pandas is called as Spreadsheet of python. Indeed it is. You can handle tabular
data very efficiently and with ease using pandas. Here is simple ways by which
we can import tabular data in pandas. Here is how you can load data from csv file::


  import pandas as pd
  wallet = pd.read_csv("wallet.csv")
  wallet.head()
  Unnamed: 0 	date 	category 	description 	debit
  0 	0 	2021-03-07 14:53:28.377359 	Music 	Amazon 	421.207327
  1 	1 	2020-10-08 09:53:28.377359 	Food 	Swiggy 	328.440080
  2 	2 	2021-02-23 09:53:28.377359 	Books 	Amazon 	244.679437
  3 	3 	2020-11-01 14:53:28.377359 	Utility 	Phone 	222.756318
  4 	4 	2021-06-05 13:53:28.377359 	Books 	Flipcart 	494.128492

we can even load data from a csv file from internet.::

  import pandas as pd
  wallet = pd.read_csv("https://raw.githubusercontent.com/vikipedia/python-trainings/master/online_course/source/module2/wallet.csv")
  wallet.head()
  Unnamed: 0 	date 	category 	description 	debit
  0 	0 	2021-03-07 14:53:28.377359 	Music 	Amazon 	421.207327
  1 	1 	2020-10-08 09:53:28.377359 	Food 	Swiggy 	328.440080
  2 	2 	2021-02-23 09:53:28.377359 	Books 	Amazon 	244.679437
  3 	3 	2020-11-01 14:53:28.377359 	Utility 	Phone 	222.756318
  4 	4 	2021-06-05 13:53:28.377359 	Books 	Flipcart 	494.128492

Similarly it is also possible to load data from excel file::

  wallet = pd.read_excel("https://github.com/vikipedia/python-trainings/raw/master/online_course/source/module2/wallet.xlsx")
  wallet.head()
  Unnamed: 0 	date 	category 	description 	debit
  0 	0 	2021-03-07 14:53:28.377359 	Music 	Amazon 	421.207327
  1 	1 	2020-10-08 09:53:28.377359 	Food 	Swiggy 	328.440080
  2 	2 	2021-02-23 09:53:28.377359 	Books 	Amazon 	244.679437
  3 	3 	2020-11-01 14:53:28.377359 	Utility 	Phone 	222.756318
  4 	4 	2021-06-05 13:53:28.377359 	Books 	Flipcart 	494.128492

**Problem 1.1**

Load one excel file from your use case, using pandas as given above. See if you
can load a particular sheet from given excel file.

**Problem 1.2**

Try to load  data from url "https://www.moneycontrol.com/markets/indian-indices/"
using `pandas.read_html` function. What is the type of result returned?

DataFrame and Series
-----------------

Most important data typr from pandas to represent tabulat data is DataFrame.
DataFrame consists of columns.::

  >>> wallet.columns
  Index(['Unnamed: 0', 'date', 'category', 'description', 'debit'], dtype='object')

​Each column can be accessed using::

  >>> wallet.date
  0     2021-03-07 14:53:28.377359
  1     2020-10-08 09:53:28.377359
  2     2021-02-23 09:53:28.377359
  3     2020-11-01 14:53:28.377359
  4     2021-06-05 13:53:28.377359
                   ...
  95    2021-07-19 13:53:28.377359
  96    2021-01-12 19:53:28.377359
  97    2021-03-25 11:53:28.377359
  98    2021-05-13 15:53:28.377359
  99    2020-10-11 16:53:28.377359
  Name: date, Length: 100, dtype: object

  >>> wallet['date']
  0     2021-03-07 14:53:28.377359
  1     2020-10-08 09:53:28.377359
  2     2021-02-23 09:53:28.377359
  3     2020-11-01 14:53:28.377359
  4     2021-06-05 13:53:28.377359
                   ...
  95    2021-07-19 13:53:28.377359
  96    2021-01-12 19:53:28.377359
  97    2021-03-25 11:53:28.377359
  98    2021-05-13 15:53:28.377359
  99    2020-10-11 16:53:28.377359
  Name: date, Length: 100, dtype: object

While each column that we see here is called as Series. This is how Series is
created , it is just like list::

  >>> s1 = pd.Series([421, 328, 123, 234])
  >>> s1
  0    421
  1    328
  2    123
  3    234
  dtype: int64
  >>> s1[0]
  421
  >>> s1[3]
  234
  >>> [i for i in s1]
  [421, 328, 123, 234]

But with additional facility of giving labels to index.::

  >>> stocks = pd.Series([421, 328, 123, 234], index=["APPLE","AT&T","IBM","NIKE"])
  >>> stocks
  APPLE    421
  AT&T     328
  IBM      123
  NIKE     234
  dtype: int64

  >>> stocks['APPLE']
  421
  >>> stocks[0]
  421
  >>> [s for s in stocks]
  [421, 328, 123, 234]


DataFrame is collection of series of same indexnames. For example::

  labels = ["APPLE","AT&T","IBM","NIKE"]
  value = pd.Series([234.5, 221.6, 125.7, 100.5], index=labels)
  high = pd.Series([240.32, 222.5, 127.3, 105.0], index=labels)
  low = pd.Series([233.0, 220.0, 123.0, 104.0], index=labels)
  volume = pd.Series([100, 200, 50, 1000], index=labels)
  stocks = pd.DataFrame({"value":value, "high":high, "low":low, "volume":volume})
  stocks
      value 	high 	low 	volume
  APPLE 234.5 	240.32 	233.0 	100
  AT&T 	221.6 	222.50 	220.0 	200
  IBM 	125.7 	127.30 	123.0 	50
  NIKE 	100.5 	105.00 	104.0 	1000

  pd.DataFrame({
      "value" : [234.5, 221.6, 125.7, 100.5],
      "high" : [240.32, 222.5, 127.3, 105.0],
      "low" : [233.0, 220.0, 123.0, 104.0],
      "volume" : [100, 200, 50, 1000]
      },
      index=labels
      )
      value 	high 	low 	volume
  APPLE 	234.5 	240.32 	233.0 	100
  AT&T 	221.6 	222.50 	220.0 	200
  IBM 	125.7 	127.30 	123.0 	50
  NIKE 	100.5 	105.00 	104.0 	1000

Here is how one can access columns from this DataFrame::

  >>> stocks.value
  APPLE    234.5
  AT&T     221.6
  IBM      125.7
  NIKE     100.5
  Name: value, dtype: float64
  >>> stocks.high
  APPLE    240.32
  AT&T     222.50
  IBM      127.30
  NIKE     105.00
  Name: high, dtype: float64
  >>> stocks['value']
  APPLE    234.5
  AT&T     221.6
  IBM      125.7
  NIKE     100.5
  Name: value, dtype: float64

What if column name has space in it?::

  >>> df = pd.DataFrame({
        "value" : [234.5, 221.6, 125.7, 100.5],
        "high value" : [240.32, 222.5, 127.3, 105.0],
        "low value" : [233.0, 220.0, 123.0, 104.0],
        "volume" : [100, 200, 50, 1000]
      })
  >>> df['low value']​
  0    233.0
  1    220.0
  2    123.0
  3    104.0
  Name: low value, dtype: float64

How to access a row or rows? ::

  >>> stocks.loc['APPLE']
  value     234.50
  high      240.32
  low       233.00
  volume    100.00
  Name: APPLE, dtype: float64
  >>> stocks.loc[["APPLE","AT&T"]]
  value 	high 	low 	volume
  APPLE 	234.5 	240.32 	233.0 	100
  AT&T 	221.6 	222.50 	220.0 	200

How to access few rows and few columns?::

  >>> stocks.loc[["APPLE","AT&T"],["value","volume"]]
  value 	volume
  APPLE 	234.5 	100
  AT&T 	221.6 	200

How to access row by index?::

  >>> stocks.iloc[0]
  value     234.50
  high      240.32
  low       233.00
  volume    100.00
  Name: APPLE, dtype: float64

How to access multiple rows with indices?::

  >>> stocks.iloc[[0,3]]
  value 	high 	low 	volume
  APPLE 	234.5 	240.32 	233.0 	100
  NIKE 	100.5 	105.00 	104.0 	1000

How aboubt row and columns together by indices?::

  >>> stocks.iloc[[0,3],[0,1]]
  value 	high
  APPLE 	234.5 	240.32
  NIKE 	100.5 	105.00

can slicing be used?

  >>> stocks.iloc[:2] # first two rows and all columns
  value 	high 	low 	volume
  APPLE 	234.5 	240.32 	233.0 	100
  AT&T 	221.6 	222.50 	220.0 	200

  >>> stocks.iloc[:2, 2:] # take frist two rows and drop first two columns
  low 	volume
  APPLE 	233.0 	100
  AT&T 	220.0 	200






Working with DataFrame
  - access a column by name
  - access a row by indexname
  - access a row by index number
  - head
  - tail
  - columns
  - index
  - selecting
  - Filtering

- More operations
  - merge
  - join
  - concatenating
  - groupby
  - str operations
  - pd.to_numeric
  - pd.to_date

- Writing to csv
