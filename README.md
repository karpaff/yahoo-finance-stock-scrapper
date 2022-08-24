# Python script for scrapping Yahoo Finance stock prices using threading

I'm learning threading and web scrapping using Python, so I decided to create a simple modeul which wich helps scrapping Yahoo Finance stock prices. It's just a tranining project, but I believe it could be useful for somebody. 

## Requirments
Script requires requests and lxml installed. 

```
pip install requests lxml
```

## How to use

You can send tickers either as a list of strings or as a file with tickers separated in any way.

### `list2dict`
```python
from stockprices import *
tickers = ['MSFT', 'GOOGL', 'AAPL', 'META']
res_dict = list2dict(tickers) # {'MSFT': 277.39, 'GOOGL': 114.29, 'AAPL': 168.0, 'META': 163.1} 
```

### `list2file`
```python
from stockprices import *
tickers = ['MSFT', 'GOOGL', 'AAPL', 'META']
# second argument can be ommited — output file will be named 'result.txt'
list2file(tickers, 'save_file_name.txt') # saves stock prices in file named save_file_name
```

### `file2dict`
```python
from stockprices import *
path_to_file = '/Users/drewk/PycharmProjects/yahoo-scrapper/tickers.txt'
res_dict = file2dict(path_to_file, 'output_file_name.txt') # {'MSFT': 277.39, 'GOOGL': 114.29, 'AAPL': 168.0, 'META': 163.1} 
```

### `file2file`
```python
from stockprices import *
path_to_file = '/Users/drewk/PycharmProjects/yahoo-scrapper/tickers.txt'
# second argument can be ommited — output file will be named 'result.txt'
res_dict = file2file(path_to_file, 'output_file_name.txt') # saves stock prices in file named save_file_name
```
