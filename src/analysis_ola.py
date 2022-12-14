import pickle
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from utils import parse_mail
from bs4 import BeautifulSoup
import datetime
import re
import os


def getData(dumpfile):
    with open(dumpfile, 'rb') as handle:
        data_dump = pickle.load(handle)

    parsed_data = parse_mail(data_dump)

    x = []
    y = []
    for parsed_row in parsed_data:
        date_this = parsed_row['date']
        snippet = parsed_row['snippet']
        subject_this = parsed_row['subject']
        if 'ride to' in subject_this:
            amount_parsed = float(snippet.split('₹')[1].split(' ')[0])
            date_parsed = datetime.datetime.strptime(
                date_this, '%a, %d %b %Y %H:%M:%S %z')
            x.append(date_parsed)
            y.append(amount_parsed)
    return x[::-1], y[::-1]
