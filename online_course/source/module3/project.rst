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
given below. Give requirements.txt with it , so that the user can install 
dependencies and run the script::

    python alphavantage_daily_to_monthly.py --help
    Usage: alphavantage_daily_to_monthly.py [OPTIONS]

    This script downloads data from alphavantage. It downloads daily series
    for given symbol. computes monthly avearges, open, close, high, low. and
    saves data in required format.

    various options are

    --csv       if this flag is given it saves data in csv format
    with this option --csvfile must be given

    --database  if this flag is given it saves data in sqlite database.
    with this option --dbfile must be given

    --xlsx   if this flag is given it saves dat in xlsx format.           with
    this option --xlsxfile must be given

    Options:
    --symbol TEXT                   [default: IBM]
    --csv / --no-csv                [default: True]
    --csvfile TEXT                  [default: ]
    --database / --no-database      [default: False]
    --dbfile TEXT                   [default: ]
    --xlsx / --no-xlsx              [default: False]
    --xlsxfile TEXT                 [default: ]
    --install-completion [bash|zsh|fish|powershell|pwsh]
                                    Install completion for the specified shell.
    --show-completion [bash|zsh|fish|powershell|pwsh]
                                    Show completion for the specified shell, to
                                    copy it or customize the installation.

    --help                          Show this message and exit.
