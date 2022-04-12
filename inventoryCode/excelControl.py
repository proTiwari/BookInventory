import pandas as pd
from openpyxl import load_workbook
import numpy as np


def excelControl(allErrorList):

    lenth = 0
    wb = load_workbook('C:/Users/stabc/OneDrive/Desktop/python/excel/testing_first_book_into_inventory.xlsx')
    sheet = wb.worksheets[0]
    v = pd.read_excel(io='C:/Users/stabc/OneDrive/Desktop/python/excel/testing_first_book_into_inventory.xlsx')
    row_count = sheet.max_row
    limit = 1000
    j = 0
    resultList = []
    forwardedList = []
    for i in range(j, row_count - 1):

        Title = str(v['Title'].iloc[i])
        Author = str(v['Author'].iloc[i])
        Description = str(v['Description'].iloc[i])
        Subtitle = str(v['Subtitle'].iloc[i])
        MRP = str(v['MRP'].iloc[i])
        ISBN13 = str(v['ISBN13'].iloc[i])
        ISBN10 = str(v['ISBN10'].iloc[i])
        yearOfPublish = str(v['yearOfPublish'].iloc[i])
        backCoverImageUrl = str(v['backCoverImageName'].iloc[i])
        frontCoverImageUrl = str(v['frontCoverImageName'].iloc[i])
        supportingImages = str(v['supportingImages'].iloc[i])
        numberOfPages = str(v['NumberOfPages'].iloc[i])
        dic = {'Title': Title,
               'Author': Author,
               'Description': Description,
               'Subtitle': Subtitle,
               'MRP': MRP,
               'yearOfPublish': yearOfPublish,
               'backCoverImageUrl': backCoverImageUrl,
               'frontCoverImageUrl': frontCoverImageUrl,
               'supportingImages': supportingImages,
               'numberOfPages': numberOfPages,
               'ISBN10': ISBN10,
               'ISBN13': ISBN13}
        resultList.append(dic)
        lenth = len(dic.keys())

    if lenth == 12:
        forwardedList.append(resultList)
        forwardedList.append(row_count)
        return forwardedList
    else:
        return allErrorList.append(f"number of attribute {lenth} != 12")
