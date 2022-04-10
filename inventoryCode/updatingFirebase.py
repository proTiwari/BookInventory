import firebase_admin
from firebase_admin import credentials, firestore
from numpy.random import random

from inventoryCode.excelControl import Title, Author, Description, MRP
from inventoryCode.main import yashListForCorrection


def updateFirestore(isbn10, isbn13):
    cred = credentials.Certificate("pucoread-firebase-adminsdk-313ve-78cc304b7a.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    doc_ref = db.collection("inventory").document(str(random()))
    doc_ref.set(
        {"Title": Title, "Author": Author, "Description": Description, "MRP": MRP, "ISBN10": isbn10,
         "ISBN13": isbn13})
    users_ref = db.collection("inventory")
    docs = users_ref.stream()
    print(f"{yashListForCorrection} {doc_ref.id}")

    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")