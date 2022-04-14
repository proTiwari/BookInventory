import firebase_admin
from firebase_admin import credentials, firestore
from numpy.random import random

cred = credentials.Certificate(
    "C:/Users/stabc/OneDrive/Desktop/python/firebase-adminsdk/pucoread-firebase-adminsdk-313ve-78cc304b7a.json")


def updateFirestore(title, author, description, subtitle, originalPrice, isbn10, isbn13, yearOfPublish,
                    backCoverImageUrl, frontCoverImageUrl, numberOfPages, supportingImages):
    db = firestore.client()
    originalPrice = int(float(originalPrice))
    numberOfPages = int(float(numberOfPages))
    doc_ref = db.collection("inventory").document()

    # code for filtering copies
    query = db.collection("inventory").where(u'isbn10', u'==', isbn10)
    docs10 = []
    for j in query.stream():
        docs10.append(j.id)

    query = db.collection("inventory").where(u'isbn13', u'==', isbn13)
    docs13 = []
    for p in query.stream():
        docs13.append(p.id)

    if not docs10 and not docs13:
        bookId = doc_ref.id
        doc_ref.set(
            {"title": title,
             "authors": author,
             "subtitle": subtitle,
             "description": description,
             "mrp": originalPrice,
             "isbn10": isbn10,
             "isbn13": isbn13,
             "bookId": bookId,
             "numberOfPages": numberOfPages,
             # "backCoverImageUrl": backCoverImageUrl[0],
             "frontCoverImageUrl": frontCoverImageUrl[0],
             # "supportingImagesUrl": supportingImages,
             "yearOfPublish": yearOfPublish})
        # users_ref = db.collection("inventory")
        # dos = users_ref.stream()
        # print(f"{doc_ref.id}")
        # for doc in dos:
        #     print(f"{doc.id} => {doc.to_dict()}")
    else:
        print(f"book of isbn10:{isbn10} or isbn13:{isbn13} already exists on database")
