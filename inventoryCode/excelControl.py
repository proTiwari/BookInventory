import pandas as pd
from openpyxl import load_workbook
import numpy as np


def excelControl():
    v = pd.read_excel(io='testing_first_book_into_inventory.xlsx', sheet_name=None)

    Title = v['Title'].iloc[0]
    Author = v['Author'].iloc[0]
    Description = v['Description'].iloc[0]
    MRP = str(v['MRP'].iloc[0])
    ISBN13 = str(v['ISBN13'].iloc[0])
    ISBN10 = str(v['ISBN10'].iloc[0])

    return Title, Author, Description, MRP, ISBN10, ISBN13
