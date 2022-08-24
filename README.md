# Scrapping Yahoo Finance stock prices funcs using threading

I'm learning threading and web scrapping using Python, so I decided to create a simple modeul which wich helps scrapping Yahoo Finance stock prices. It's just a tranining project, but I believe it could be useful for somebody. 

## Requirments
Script requires requests and lxml installed. 

```
pip install requests lxml
```

## How to use

You can send tickers either as a list of strings or as a file with tickers separated in any way.

#### `list2dict`
Takes a list of tickers as strings. Returns a dictionary with tickers as keys and float prices as values.
```python
from stockprices import *
tickers = ['MSFT', 'GOOGL', 'AAPL', 'META']
res_dict = list2dict(tickers) # {'MSFT': 277.39, 'GOOGL': 114.29, 'AAPL': 168.0, 'META': 163.1} 
```

#### `list2file`
Takes a list of tickers as strings. Writes ticker-price pairs to the file, separated by a space.
You can pass a name of an output file as a second argument. If a second argument is omitted, the output file will be named result.txt
```python
from stockprices import *
tickers = ['MSFT', 'GOOGL', 'AAPL', 'META']
list2file(tickers, 'save_file_name.txt') # writes stock prices to the file named save_file_name.txt
```

#### `file2dict`
Takes a path to the file with tikers separated in any way. Returns a dictionary with tickers as keys and float prices as values.
```python
from stockprices import *
path_to_file = '/Users/drewk/PycharmProjects/yahoo-scrapper/tickers.txt'
res_dict = file2dict(path_to_file, 'output_file_name.txt') # {'MSFT': 277.39, 'GOOGL': 114.29, 'AAPL': 168.0, 'META': 163.1} 
```

#### `file2file`
Takes a path to the file with tikers separated in any way. Writes ticker-price pairs to the file, separated by a space.
You can pass a name of an output file as a second argument. If a second argument is omitted, the output file will be named result.txt
```python
from stockprices import *
path_to_file = '/Users/drewk/PycharmProjects/yahoo-scrapper/tickers.txt'
res_dict = file2file(path_to_file, 'output_file_name.txt') # writes stock prices in the file named save_file_name.txt
```
