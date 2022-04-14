from datetime import datetime


def DateOfPublish(publishingYear, D):
    lst = publishingYear.split('\\')
    resultList = []

    D = D.split('/')
    Dd = int(D[0])
    Dm = int(D[1])
    Dy = int(D[2])
    if lst != ['nan']:
        dd = lst[0]
        mm = lst[1]
        yy = lst[2]
        dd = int(dd)
        mm = int(mm)
        yy = int(yy)
        if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
            max1 = 31
        elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
            max1 = 30
        elif yy % 4 == 0 and yy % 100 != 0 or yy % 400 == 0:
            max1 = 29
        else:
            max1 = 28

        if mm < 1 or mm > 12:
            resultList.append("month is invalid.")

        elif dd < 1 or dd > max1:
            resultList.append("date is invalid.")
        else:
            D = datetime(yy, mm, dd)
            res = D.strftime("%B")
            resultList.append(f'{dd} {res} {yy}')
            resultList.append('True')
        if Dy < yy:
            resultList.append("error future date")
        if Dy == yy:
            if Dm < mm:
                resultList.append("error future month")
            if Dm == mm:
                if Dd == dd:
                    pass
                if Dd < dd:
                    resultList.append("error future date")
        return resultList
    else:
        resultList.append("empty date field")
        return resultList
