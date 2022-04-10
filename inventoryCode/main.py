import asyncio
from random import random

from pyasn1.compat.octets import null
from stdnum import ean
from stdnum.exceptions import *
from stdnum.util import clean, isdigits

import janitor
from collections import defaultdict
import isbnlib
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Title
# Subtitle
# description
# Author
# MRP
# ISBN10
# ISBN13
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


