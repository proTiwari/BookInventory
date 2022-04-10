import pandas as pd
from openpyxl import load_workbook
import numpy as np


def excelControl():
    v = pd.read_excel(io='C:/Users/stabc/OneDrive/Desktop/python/excel/testing_first_book_into_inventory.xlsx')
    print(v)
    Title = v['Title'].iloc[0]
    Author = v['Author'].iloc[0]
    Description = v['Description'].iloc[0]
    Subtitle = v['Subtitle'].iloc[0]
    MRP = str(v['MRP'].iloc[0])
    ISBN13 = str(v['ISBN13'].iloc[0])
    ISBN10 = str(v['ISBN10'].iloc[0])
    dic = {'Title': Title,
           'Author': Author,
           'Description': Description,
           'Subtitle': Subtitle,
           'MRP': MRP,
           'ISBN10': ISBN10,
           'ISBN13': ISBN13}
    return dic
