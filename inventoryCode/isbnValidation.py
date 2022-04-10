import isbnlib


def checkForIsbn(isbn10, isbn13, yashListForCorrection):
    isbn10List = []
    isbn13List = []
    result = []

    if isbn10 != '':
        isbn10 = isbn10.split()
        for j in isbn10:
            if j.isdigit():
                isbn10List.append(j)
    else:
        yashListForCorrection.append(f"in isbn10:{isbn10} is null")

    if isbn13 != '':
        isbn13 = isbn13.split()
        for i in isbn13:
            if i.isdigit():
                isbn13List.append(i)
    else:
        yashListForCorrection.append(f"in isbn13:{isbn13} is null")

    if isbn10List != [] and isbn13List != []:
        isbn10 = isbn10List[0]
        isbn13 = isbn13List[0]
    else:
        yashListForCorrection.append("isbn field is empty")
    resultISBN10 = isbnlib.is_isbn10(isbn10)
    if not resultISBN10:
        yashListForCorrection.append("invalid isbn10")
    resultISBN13 = isbnlib.is_isbn13(isbn13)
    if not resultISBN13:
        yashListForCorrection.append("invalid isbn10")
    if resultISBN13 and resultISBN10:
        result.append([True, yashListForCorrection])
        return result
    else:
        result.append([False, yashListForCorrection])
        return result
