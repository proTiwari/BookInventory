import firebase_admin
from firebase_admin import credentials, firestore
from numpy.random import random


from inventoryCode.main import yashListForCorrection

if not yashListForCorrection:
    def updateFirestore(title, author, description, subtitle, mrp, isbn10, isbn13):
        cred = credentials.Certificate("pucoread-firebase-adminsdk-313ve-78cc304b7a.json")
        firebase_admin.initialize_app(cred)
        db = firestore.client()

        doc_ref = db.collection("inventory").document(str(random()))
        doc_ref.set(
            {"Title": title, "Author": author, "Subtitle": subtitle, "Description": description, "MRP": mrp, "ISBN10": isbn10,
             "ISBN13": isbn13})
        users_ref = db.collection("inventory")
        docs = users_ref.stream()
        print(f"{yashListForCorrection} {doc_ref.id}")

        for doc in docs:
            print(f"{doc.id} => {doc.to_dict()}")
else:
    print(f"upload failed due to filled yashListForCorrection {yashListForCorrection}")