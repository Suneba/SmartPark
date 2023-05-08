from django.shortcuts import render
import pyrebase
from django.contrib import auth
import razorpay

config = {
  "apiKey": "AIzaSyCIX86nT42i_1M82ELBNZXsxSH1tr213BU",
  "authDomain": "django-49754.firebaseapp.com",
  "projectId": "django-49754",
"storageBucket":"django-49754.appspot.com",
  "messagingSenderId": "231352706078",
  "appId": "1:231352706078:web:a919c86476d3abbf44ba0f",
  "databaseURL":"https://django-49754-default-rtdb.asia-southeast1.firebasedatabase.app/"

}
firebase = pyrebase.initialize_app(config)
#
authe = firebase.auth()
database = firebase.database()


for i in range(1,13):
    database.child(f"parking_spots/parking_3/spot_num/spot_{i}/booked").set(False)
    print(i)

