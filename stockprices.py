import threading
import requests
from lxml import html


class Stock(threading.Thread):
    def __init__(self, ticker: str) -> None:
        super().__init__()

        self.ticker = ticker
        self.url = f'https://finance.yahoo.com/quote/{ticker}'
        self.price = None

    def run(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            tree = html.fromstring(response.text)
            # get the price in text
            price_text = tree.xpath(
                '//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]/text()')
            if price_text:
                try:
                    self.price = float(price_text[0].replace(',', ''))
                except ValueError:
                    self.price = None


def list2dict(tickers: list) -> dict:
    threads = []

    for ticker in tickers:
        t = Stock(ticker)
        t.start()
        threads.append(t)

    result_dict = {}

    for t in threads:
        t.join()
        result_dict[t.ticker] = t.price

    return result_dict


def list2file(tickers: list, save_as='result.txt') -> None:
    threads = []

    for ticker in tickers:
        t = Stock(ticker)
        t.start()
        threads.append(t)

    result_dict = {}

    for t in threads:
        t.join()
        result_dict[t.ticker] = t.price

    write_in_file(save_as, result_dict)


def file2dict(input_file_path: str) -> dict:
    threads = []

    tickers = parse_file(input_file_path)

    for ticker in tickers:
        t = Stock(ticker)
        t.start()
        threads.append(t)

    result_dict = {}

    for t in threads:
        t.join()
        result_dict[t.ticker] = t.price

    return result_dict


def file2file(input_file_path: str, save_as='result.txt') -> None:
    threads = []

    tickers = parse_file(input_file_path)

    for ticker in tickers:
        t = Stock(ticker)
        t.start()
        threads.append(t)

    result_dict = {}

    for t in threads:
        t.join()
        result_dict[t.ticker] = t.price

    write_in_file(save_as, result_dict)


def write_in_file(file_name: str, result_dict: dict) -> None:
    with open(file_name, 'w') as file:
        for ticker in result_dict.keys():
            file.write(f'{ticker} {str(result_dict[ticker])}\n')


def parse_file(file_path: str) -> list:
    separator = find_separator(file_path)
    with open(file_path, 'r') as file:
        if separator == ' ':
            tickers = file.read().split(separator)
        else:
            tickers = file.read().replace(' ', '').split(separator)
    return tickers


def find_separator(file_path):
    separator = ' '
    with open(file_path, 'r') as file:
        for symb in file.read():
            if not ('A' < symb < 'Z' or 'a' < symb < 'z'):
                separator = symb
                break
    return separator

