from datetime import datetime


def DateOfPublish(publishingYear, D):
    yy = int(publishingYear)
    resultList = []

    D = D.split('/')
    Dy = int(D[2])
    if yy != ['nan']:
        if Dy < yy:
            resultList.append("error future date")
            resultList.append(False)
        else:
            resultList.append(True)

        if yy < 1000:
            resultList.append("error date invalid")
            resultList.append(False)
        else:
            resultList.append(True)

        return resultList
    else:
        resultList.append("empty date field")
        resultList.append(False)
        return resultList
