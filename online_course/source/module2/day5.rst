Working With CSV and Excel Files
================================

Reading
-------

Read data using reader::

  import csv
  def read_csv(filename):
    data = []
    with open(filename) as f:
        freader = csv.reader(f)
        headers = next(freader)
        for row in freader:
            data.append(row)
    return data

  read_csv("indexdata.csv")
  [['XFNBI', '154.27522023650917', '2.871245637237712', '3926'],
   ['ORGHT', '117.97670217978481', '4.539536223184663', '586'],
   ['VEBHV', '113.3520799776703', '0.6635982458596046', '3688'],
   ['BYRIK', '104.2138293580797', '2.626015334200588', '1767'],
   ['VCRRD', '155.43160467760868', '0.4681719455962513', '641'],
   ['PEQVY', '181.21666821143089', '0.42729711749318167', '2738'],
   ['LQTQZ', '168.33573338890363', '3.521911607612079', '2670'],
   ['HPDAK', '155.96008397206708', '1.7239221076463696', '4259'],
   ['XLHUI', '174.46964754068694', '3.745170925696039', '2770'],
   ['JEAZX', '148.7162928469953', '2.6624961725339205', '1614'],
   ['QOZAM', '192.1176069819026', '4.139241768741275', '726'],
   ['XJAHU', '150.20434996488757', '3.1065263183864253', '2688'],
   ['VLXDC', '178.73486584779386', '3.8678532141202036', '4103'],
   ['PJQEK', '199.0461185921472', '3.2096859326164178', '1592'],
   ['DWJDV', '148.7534049268761', '3.331681968931371', '2177'],
   ['ORJMD', '174.11752806601532', '3.180221402115432', '909'],
   ['DLJGR', '117.33043838185898', '0.34686211777134657', '4092'],
   ['YCHHM', '144.8746810221045', '3.3530551951924155', '1571'],
   ['WFNNB', '147.65332106681385', '3.7760281088943017', '3195'],
   ['YNRZG', '128.86957732022677', '4.5699186134962435', '2713']]


With this, data is loaded but all fields are strings. To fix it we can little
fix up in our code::

  def read_csv(filename, fields):
    data = []
    with open(filename) as f:
        freader = csv.reader(f)
        headers = next(freader)
        for row in freader:
            row = tuple(convert(v) for convert, v in zip(fields, row))
            data.append(row)
    return data

  fields = [str, float, float, int]
  read_csv("indexdata.csv")
  [('XFNBI', 154.27522023650917, 2.871245637237712, 3926),
   ('ORGHT', 117.97670217978481, 4.539536223184663, 586),
   ('VEBHV', 113.3520799776703, 0.6635982458596046, 3688),
   ('BYRIK', 104.2138293580797, 2.626015334200588, 1767),
   ('VCRRD', 155.43160467760868, 0.4681719455962513, 641),
   ('PEQVY', 181.21666821143089, 0.42729711749318167, 2738),
   ('LQTQZ', 168.33573338890363, 3.521911607612079, 2670),
   ('HPDAK', 155.96008397206708, 1.7239221076463696, 4259),
   ('XLHUI', 174.46964754068694, 3.745170925696039, 2770),
   ('JEAZX', 148.7162928469953, 2.6624961725339205, 1614),
   ('QOZAM', 192.1176069819026, 4.139241768741275, 726),
   ('XJAHU', 150.20434996488757, 3.1065263183864253, 2688),
   ('VLXDC', 178.73486584779386, 3.8678532141202036, 4103),
   ('PJQEK', 199.0461185921472, 3.2096859326164178, 1592),
   ('DWJDV', 148.7534049268761, 3.331681968931371, 2177),
   ('ORJMD', 174.11752806601532, 3.180221402115432, 909),
   ('DLJGR', 117.33043838185898, 0.34686211777134657, 4092),
   ('YCHHM', 144.8746810221045, 3.3530551951924155, 1571),
   ('WFNNB', 147.65332106681385, 3.7760281088943017, 3195),
   ('YNRZG', 128.86957732022677, 4.5699186134962435, 2713)]

There is another reader `DictReader` which takes headers and from that takes
field names. This allows to make access to row items as dictionary.::

  fields = [("price", float),
            ("change", float),
            ("volume", int)]
  with open("indexdata.csv") as f:
      for row in csv.DictReader(f):
          row.update((key, convert(row[key])) for key, convert in fields)
          print(row)

This can be used easily to access only particular column from file.::

  def getcolumn(filename , name , type_):
      with open(filename) as f:
          return [type_(row[name]) for row in csv.DictReader(f)]

  getcolumn("indexdata.csv", "price", float)
  [154.27522023650917,
   117.97670217978481,
   113.3520799776703,
   104.2138293580797,
   155.43160467760868,
   181.21666821143089,
   168.33573338890363,
   155.96008397206708,
   174.46964754068694,
   148.7162928469953,
   192.1176069819026,
   150.20434996488757,
   178.73486584779386,
   199.0461185921472,
   148.7534049268761,
   174.11752806601532,
   117.33043838185898,
   144.8746810221045,
   147.65332106681385,
   128.86957732022677]
  ​

It is also possible to read tsv file with option , delimiter='\t' to the reader.

Writing
-------
To write file use csv.writer and then write row by row.::

  def write_csv(data, columns, filename):
      with open(filename, "w") as f:
          csvf = csv.writer(f)
          csvf.writerow(columns)
          for row in data:
              csvf.writerow(row)


Writing Excel Files with xlsxwriter
-----------------------------------
xlsxwriter is a third party library well equiped to write excel files. Not only
basic tabular data writing but most of excel functionality can be used through
python scrips, which include all formatting tricks and charts too. Here is very
example of how to write tabular data in excel file using xlsxwriter::

  def write_row(sheet, rowentry, rownumber=0, colnumber=0):
      for c, item in enumerate(rowentry, start=colnumber):
          sheet.write(rownumber, c, item)

  columns = ['symbol', 'price', 'change', 'volume']
  workbook = xlsxwriter.Workbook("indexdata.xlsx")
  worksheet = workbook.add_worksheet("prices")

  write_row(worksheet, columns, rownumber=0)

  for r, entries in enumerate(indexdata, start=1):
      write_row(worksheet, entries, r)

  workbook.close()


We can also try some formatting using this library::


  def write_row(sheet, rowentry, rownumber=0, colnumber=0, format=None):
      for c, item in enumerate(rowentry, start=colnumber):
          if format:
              sheet.write(rownumber, c, item, format)
          else:
              sheet.write(rownumber, c, item)

  def write_col(sheet, column, rownumber=0, colnumber=0, format=None):
      for r, item in enumerate(column, start=rownumber):
          if format:
              sheet.write(r, colnumber, item, format)
          else:
              sheet.write(r, colnumber, item)


  columns = ['symbol', 'price', 'change', 'volume']
  workbook = xlsxwriter.Workbook("indexdata_format.xlsx")
  worksheet = workbook.add_worksheet("prices")

  bold = workbook.add_format({'bold': True})
  money = workbook.add_format({'num_format': '$#,##0'})

  write_row(worksheet, columns, format=bold)
  symbol = [row[0] for row in indexdata]
  price = [row[1] for row in indexdata]

  write_col(worksheet, symbol, rownumber=1, colnumber=0)
  write_col(worksheet, price, rownumber=1, colnumber=1, format=money)

  for c, colname in enumerate(columns[2:], start=2)
      col =  [row[c] for row in indexdata]
      write_col(worksheet,col, rownumber=1, colnumber=c)

  lastrow = len(indexdata)
  worksheet.write(lastrow+1, len(columns)-1, "=SUM(D2:D{})".format(lastrow))

  workbook.close()


- Excel tables - add_table,
- Collapsed outline and grouping - set_row
- Panes - freeze panes
