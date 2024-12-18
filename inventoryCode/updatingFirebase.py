import firebase_admin
from firebase_admin import credentials, firestore
from numpy.random import random

cred = credentials.Certificate(
    "C:/Users/stabc/OneDrive/Desktop/python/firebase-adminsdk/pucoread-firebase-adminsdk-313ve-78cc304b7a.json")


def updateFirestore(title, author, description, subtitle, originalPrice, isbn10, isbn13, yearOfPublish, frontCoverImageUrl, numberOfPages):
    db = firestore.client()
    originalPrice = int(float(originalPrice))
    numberOfPages = int(float(numberOfPages))

    # code for filtering copies
    query = db.collection("books_database").where(u'isbn10', u'==', isbn10)
    docs10 = []
    for j in query.stream():
        docs10.append(j.id)

    query = db.collection("books_database").where(u'isbn13', u'==', isbn13)
    docs13 = []
    for p in query.stream():
        docs13.append(p.id)

    if not docs10 and not docs13:
        doc_ref = db.collection("books_database").document()
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
    else:
        print(f"book of isbn10:{isbn10} or isbn13:{isbn13} already exists on database")
