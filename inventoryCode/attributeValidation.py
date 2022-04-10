def isAllAttributeValid(title, author, description, subtitle, mrp, isbn10, isbn13, cleanIsbn10, cleanIsbn13):
    isAllAttributeValidErrorList = []
    if isbn10 == cleanIsbn10:
        if isbn13 == cleanIsbn13:
            if mrp.isdigit():
                pass
            else:
                isAllAttributeValidErrorList.append("error in MRP")
            if subtitle != "":
                pass
            else:
                isAllAttributeValidErrorList.append("error in Subtitle")
            if description != "":
                pass
            else:
                isAllAttributeValidErrorList.append("error in description")
            if author != "":
                pass
            else:
                isAllAttributeValidErrorList.append("error in author")
            if title != "":
                pass
            else:
                isAllAttributeValidErrorList.append("error in title")
        else:
            isAllAttributeValidErrorList.append("error in isbn13")
    else:
        isAllAttributeValidErrorList.append("error in isbn10")

    return isAllAttributeValidErrorList





