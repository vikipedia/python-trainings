Project
=======

Daily stock prices are available online from a website. API for geting data in
json format is explained here.

This API returns daily time series (date, daily open, daily high, daily low,
daily close, daily volume) of the global equity specified, covering 20+ years of
historical data.

API Parameters

* Required: function

The time series of your choice. In this case, ``function=TIME_SERIES_DAILY``

* Required: symbol

The name of the equity of your choice. For example: ``symbol=IBM``

* Optional: outputsize

By default, outputsize=compact. Strings compact and full are accepted with the
following specifications: compact returns only the latest 100 data points; full
returns the full-length time series of 20+ years of historical data.
The "compact" option is recommended if you would like to reduce the data size
of each API call.

* Optional: datatype

By default, datatype=json. Strings json and csv are accepted with the following
specifications:``json`` returns the daily time series in JSON format;
``csv`` returns the time series as a CSV (comma separated value) file.

* Required: apikey

Your API key. Claim your free API key using this link
https://www.alphavantage.co/support/#api-key

Examples (click for JSON output)

https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo

https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey=demo

Task
----

Build a commandline python application which downloads daily time series data
for full length, Saves the data locally. then computes monthly average of this
data and save it to excel file. your commandline application should work as
given below::

  python alphavantage_daily_to_monthly.py --symbol IBM --output IBM_monthly.xlsx
