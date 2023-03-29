from django.shortcuts import render
import pyrebase
from django.contrib import auth
#
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


def home(request):
  return render(request,"project/index.html")

def signin(request):
  return render(request, "project/LOGIN/index.html")


def register(request):
  return render(request, "project/LOGIN/REGISTER/index.html")



def postsign(request):
  email = str(request.POST.get('email'))
  passw = request.POST.get('pass')

  try:
    user = authe.sign_in_with_email_and_password(email, passw)
  except:
    message = "invalid credentials"
    return render(request,"project/LOGIN/index.html",{"messg":message})
  # print(user['idToken'])
  session_id = str(user['idToken'])
  request.session['uid'] = session_id
  local, at, domain = email.rpartition('@')

  count = 0
  for i in str(database.child(f"parking_spots").get().val()):
    if i == "(":
      count = count + 1

  parking_spot_names =[]
  latitude_list = []
  longitude_list =[]
  number = []

  dict_for_pk_spots ={}
  for i in range(0, count-1):
    name = (database.child(f"parking_spots/parking_{i+1}/details/name").get().val())
    lat = (database.child(f"parking_spots/parking_{i+1}/details/lat").get().val())
    lon = (database.child(f"parking_spots/parking_{i+1}/details/lon").get().val())

    dict_for_pk_spots[i] = [name]
    print(parking_spot_names.append(name))
    print(latitude_list.append(lat))
    print(longitude_list.append(lon))
  print(dict_for_pk_spots)
  return render(request, "project/dashboard/index.html",{"name":local,"email":email,"parking_spot_name":dict_for_pk_spots,"lat":latitude_list,"lon":longitude_list,"number":count-1})


def logout(request):
  auth.logout(request)
  return render(request,"project/index.html")


def postsignup(request):
  name = request.POST.get('name')
  email = request.POST.get('email')
  passw = request.POST.get('pass')

  user = authe.create_user_with_email_and_password(email,passw)

  uid = user['localId']
  data={"name":name, "status":"1"}
  data1={"lat":30.357859, "lon":76.367877}
  database.child("users").child(uid).child("details").set(data)
  print("*********************************************************\n**************************************")
  print(  database.child("parking_spots").child("parking_1").child("details").set(data1))
  return render(request,"project/LOGIN/index.html")

