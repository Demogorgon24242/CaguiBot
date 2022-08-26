# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore


# try:
#     cred = credentials.Certificate("trial_python_firebase_key.json")
#     firebase_admin.initialize_app(cred)

#     print("No problems")

#     db= firestore.client()
#     print("No problems")
#     db.collection("career_options").add({"sample_career1":"reference2"})

# except:
#     print("Something went wrong")


# api__key = "AIzaSyCQtbVmEfzYZqhPHaRxumwUi7PoPE2VblY"
    # youtube = build('youtube','v3',developerKey=api__key)
    # req= youtube.search().list(q=sea,part='snippet',type='video')
    # res = req.execute()
    # for item in res['items']:
    #     print(item['snippet']['title'])


