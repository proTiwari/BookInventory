
def isAllAttributeValid(title, author, description, subtitle, mrp, isbn10, isbn13, cleanIsbn10, cleanIsbn13,
                        frontCoverImageUrl, backCoverImageUrl, numberOfPages, supportingImages, yearOfPublish):
    isAllAttributeValidErrorList = []

    if isbn10 == cleanIsbn10:
        if isbn13 == cleanIsbn13:

            if yearOfPublish != "nan":
                pass
            else:
                isAllAttributeValidErrorList.append("error in yearOfPublish")

            if frontCoverImageUrl:
                pass
            else:
                isAllAttributeValidErrorList.append("empty list frontCoverImageUrl")

            if backCoverImageUrl:
                pass
            else:
                isAllAttributeValidErrorList.append("empty list backCoverImageUrl")

            if supportingImages:
                pass
            else:
                isAllAttributeValidErrorList.append("empty list supportingImages")

            if isfloat(numberOfPages):
                pass
            else:
                isAllAttributeValidErrorList.append("error in number of pages")

            if isfloat(mrp):
                pass
            else:
                isAllAttributeValidErrorList.append("error in MRP")
            if subtitle != "nan":
                pass
            else:
                isAllAttributeValidErrorList.append("error in Subtitle")
            if description != "nan":
                pass
            else:
                isAllAttributeValidErrorList.append("error in description")
            if author:
                pass
            else:
                isAllAttributeValidErrorList.append("error in author")
            if title != "nan":
                pass
            else:
                isAllAttributeValidErrorList.append("error in title")
        else:
            isAllAttributeValidErrorList.append("error in isbn13")
    else:
        isAllAttributeValidErrorList.append("error in isbn10")

    return isAllAttributeValidErrorList


def isValidYearOfPublish():
    pass


def isfloat(num):
    try:
        int(float(num))
        return True
    except ValueError:
        return False
