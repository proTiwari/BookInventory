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

yashListForCorrection = []
values = excelControl()
print(values)

isIsbnValid = checkForIsbn(values.ISBN10, values.ISBN13, yashListForCorrection)
print(isIsbnValid)
