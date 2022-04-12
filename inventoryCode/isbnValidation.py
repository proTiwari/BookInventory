import isbnlib


def checkForIsbn(isbn10, isbn13, yashListForCorrection):

    result = []
    if str(isbn10)[-1] == 'X':
        pass
    else:
        if isfloat(isbn10):
            isbn10 = int(float(isbn10))
        else:
            yashListForCorrection.append("error in isbn10")

    if isfloat(isbn13):
        isbn13 = int(float(isbn13))
    else:
        yashListForCorrection.append("error in isbn13")

    if isbn10 == 'nan':
        yashListForCorrection.append('isbn10 is nan')
    else:
        pass

    if isbn13 == 'nan':
        yashListForCorrection.append('isbn13 is nan')
    else:
        pass

    isbn10 = str(isbn10)
    resultISBN10 = isbnlib.is_isbn10(isbn10)
    if not resultISBN10:
        yashListForCorrection.append("invalid isbn10")
    isbn13 = str(isbn13)
    resultISBN13 = isbnlib.is_isbn13(isbn13)
    if not resultISBN13:
        yashListForCorrection.append("invalid isbn13")
    if resultISBN13 and resultISBN10:
        result.append([True, yashListForCorrection, isbn10, isbn13])
        return result
    else:
        result.append([False, yashListForCorrection, isbn10, isbn13])
        return result


def isfloat(num):
    try:
        int(float(num))
        return True
    except ValueError:
        return False
