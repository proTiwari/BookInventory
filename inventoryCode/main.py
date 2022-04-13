import isbnlib
from datetime import date

from inventoryCode.excelControl import excelControl
from inventoryCode.isbnValidation import checkForIsbn
from inventoryCode.attributeValidation import isAllAttributeValid
from inventoryCode.updatingFirebase import updateFirestore
from inventoryCode.attributeValidation import isfloat
from inventoryCode.yearOfPublish import DateOfPublish

allErrorsList = []


def main():
    x = False
    isIsbnValid = False
    values = excelControl(allErrorsList)
    count = 0
    countError = 0
    countAttError = 0
    for dic in values[0]:
        count += 1
        yashListForCorrection = []
        isAttributeValid = []
        title = dic["Title"]
        authors = dic["Author"]
        description = dic["Description"]
        subtitle = dic["Subtitle"]
        originalPrice = dic["MRP"]
        isbn10 = dic["ISBN10"]
        isbn13 = dic["ISBN13"]
        frontCoverImageUrl = dic["frontCoverImageUrl"]
        backCoverImageUrl = dic["backCoverImageUrl"]
        numberOfPages = dic["numberOfPages"]
        supportingImages = dic["supportingImages"]
        publishingDate = dic["yearOfPublish"]
        Date = date.today()
        d1 = Date.strftime("%d/%m/%Y")
        publishingList = DateOfPublish(publishingDate, d1)
        if publishingList[-1] == 'True':
            publishingDate = publishingList[-2]
        else:
            yashListForCorrection.append(publishingList)

        if len(isbn10) == 9:
            isbn10 = '0' + isbn10

        if isbn10[-1] == 'X':
            x = isbnlib.is_isbn10(isbn10)
            if not x:
                yashListForCorrection.append('invalid isbn10(this isbn10 ends with X)')

        if isfloat(isbn10) or x:
            if isfloat(isbn13):
                if x:
                    isIsbnValid = checkForIsbn(isbn10, int(float(isbn13)), yashListForCorrection)
                else:
                    isIsbnValid = checkForIsbn(int(float(isbn10)), int(float(isbn13)), yashListForCorrection)

            else:
                yashListForCorrection.append('isbn13 is not in required format')
        else:
            yashListForCorrection.append('isbn10 is not in required format')

        isallAttributeValid = isAllAttributeValid

        if yashListForCorrection:
            countError = count

        if isIsbnValid[0][0] and not yashListForCorrection:
            if x:
                isAttributeValid = isallAttributeValid(title, authors, description, subtitle, originalPrice,
                                                       isbn10,
                                                       int(float(isbn13)),
                                                       isIsbnValid[0][2], int(float(isIsbnValid[0][3])),
                                                       frontCoverImageUrl,
                                                       backCoverImageUrl, numberOfPages, supportingImages,
                                                       publishingDate)
            else:
                isAttributeValid = isallAttributeValid(title, authors, description, subtitle, originalPrice,
                                                       int(float(isbn10)),
                                                       int(float(isbn13)),
                                                       int(float(isIsbnValid[0][2])), int(float(isIsbnValid[0][3])),
                                                       frontCoverImageUrl,
                                                       backCoverImageUrl, numberOfPages, supportingImages,
                                                       publishingDate)

            if isAttributeValid:
                countAttError = count

        else:
            pass

        if not isAttributeValid and not yashListForCorrection:
            updateFirestore(title, authors, description, subtitle,
                            originalPrice,
                            isIsbnValid[0][2], isIsbnValid[0][3], publishingDate, backCoverImageUrl,
                            frontCoverImageUrl, numberOfPages, supportingImages)
        else:

            if isAttributeValid:
                allErrorsList.append(isAttributeValid)
                allErrorsList.append(f"row:{countAttError + 1}")
                # print(f'error countAttError = {countAttError}')
                # print(isAttributeValid)

            if yashListForCorrection:
                allErrorsList.append(yashListForCorrection)
                allErrorsList.append(f"row:{countError + 1}")
                # print(f'error countError = {countError}')
                # print(yashListForCorrection)
    print(allErrorsList)


main()
# including images
# getting most formatted data form excel file//done
# searching isbn on firestore if it exist already or not//done
# coma separated multiple supportingImages and author0.
# counting the numbers of filled rows than match it with count in loop. when differ send data not reachable error//done
# yearofpublish
#
