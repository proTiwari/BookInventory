from inventoryCode.excelControl import excelControl
from inventoryCode.isbnValidation import checkForIsbn
from inventoryCode.attributeValidation import isAllAttributeValid
from inventoryCode.updatingFirebase import updateFirestore


yashListForCorrection = []
values = excelControl()

isIsbnValid = checkForIsbn(values["ISBN10"], values["ISBN13"], yashListForCorrection)

isAllAttributeValid = isAllAttributeValid(values["Title"], values["Author"], values["Description"], values["Subtitle"],
                                          values["MRP"], values["ISBN10"], values["ISBN13"], isIsbnValid[0][2], isIsbnValid[0][3])

if isIsbnValid[0][0] and not yashListForCorrection:
    ISBN10 = values["ISBN10"]
    ISBN13 = values["ISBN13"]

    if not isAllAttributeValid:
        updateFirestore(values["Title"], values["Author"], values["Description"], values["Subtitle"], values["MRP"], isIsbnValid[0][2], isIsbnValid[0][3])
    else:
        error = yashListForCorrection.append(isAllAttributeValid)
        print(error)

# total number of attributes should be included for validation
