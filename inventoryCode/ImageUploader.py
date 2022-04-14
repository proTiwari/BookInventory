import glob
from random import random

import firebase_admin
from firebase_admin import credentials, initialize_app, storage

cred = credentials.Certificate(
    "C:/Users/stabc/OneDrive/Desktop/python/firebase-adminsdk/pucoread-9169d85a2597.json")
firebaseApp = firebase_admin.initialize_app(cred, {'storageBucket': 'pucoread.appspot.com'})


def ImageUploader(frontCoverImageUrl, backCoverImageUrl, supportingImages):
    # fileName3 = "front.jpg"
    # bucket = firebase_admin.storage.bucket()
    # blob3 = bucket.blob(f'inventoryImages/{fileName3}')
    # blob3.upload_from_filename(fileName3)

    errorList = []
    supportingUrlList = []
    frontUrlList = []
    backUrlList = []
    id = random()
    resultList = []
    bucket = firebase_admin.storage.bucket()

    frontCoverImageList = glob.glob(f"{frontCoverImageUrl}")

    if not frontCoverImageList:
        return errorList.append(f'No match for {frontCoverImageUrl} found')

    # f"C:/Users/stabc/OneDrive/Desktop/python/Images/{frontCoverImageUrl}"
    backCoverImageList = glob.glob(f"{backCoverImageUrl}")

    if not backCoverImageList:
        return errorList.append(f'No match for {backCoverImageUrl} found')

    supportingImages = supportingImages.split(',')

    lent = len(supportingImages)

    for i in range(lent):
        supportingImageList = glob.glob(supportingImages[i])
        if not supportingImages[i]:
            return errorList.append(f'No match for {supportingImages[i]} found')
        fileName3 = supportingImageList[0]
        blob3 = bucket.blob(f'inventoryImages/{id}/supportingImage/{fileName3}')
        blob3.upload_from_filename(fileName3)
        down = blob3.public_url
        supportingUrlList.append(down)

    fileName1 = frontCoverImageList[0]
    fileName2 = backCoverImageList[0]
    blob1 = bucket.blob(f'inventoryImages/{id}/frontCoverImage/{fileName1}')
    blob1.upload_from_filename(fileName1)
    down1 = blob1.public_url
    frontUrlList.append(down1)

    blob2 = bucket.blob(f'inventoryImages/{id}/backCoverImage/{fileName2}')
    blob2.upload_from_filename(fileName2)
    down2 = blob2.public_url
    backUrlList.append(down2)

    resultList.append(supportingUrlList)
    resultList.append(frontUrlList)
    resultList.append(backUrlList)

    return resultList


