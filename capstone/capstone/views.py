from django.shortcuts import render
import pyrebase
from django.contrib import auth
import razorpay
from django.http import JsonResponse
import json
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

def logout(request):
  auth.logout(request)
  return render(request,"project/index.html")

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
  session_id = str(user['localId'])
  print("**************************////////////////",session_id)
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
    spot = str(database.child(f"spot_color").get().val())

    credit = (database.child(f"users/{session_id}/details/credit").get().val())


    dict_for_pk_spots[i] = [name]
    print(parking_spot_names.append(name))
    print(latitude_list.append(lat))
    print(longitude_list.append(lon))
  print(dict_for_pk_spots)




  return render(request, "project/dashboard/index.html",{"credit":credit,"session_id":session_id,"name":local,"email":email,"parking_spot_name":dict_for_pk_spots,"lat":latitude_list,"lon":longitude_list,"number":count-1,"spot":spot,})




def postsignup(request):
  name = request.POST.get('name')
  email = request.POST.get('email')
  passw = request.POST.get('pass')

  user = authe.create_user_with_email_and_password(email,passw)

  uid = user['localId']
  data={"name":name, "email":email,}
  database.child("users").child(uid).child("details").set(data)
  return render(request,"project/LOGIN/index.html")


def details(request):
  print(request.session['uid'])
  id  = request.session['uid']
  return render(request, "project/dashboard/details.html",{"id":id})

def dashboard(request):
  print(request.session['uid'])
  id = request.session['uid']
  return render(request, "project/dashboard/index.html", {"id": id})


def book_slot(request):
  lic_num = str(request.POST.get('lic_num'))
  full_name = request.POST.get('full_name')
  spot_num = request.POST.get('spot_num')

  database.child(f"parking_spots/parking_3/spot_num/spot_{spot_num}/booked").set("true")

  return render(request, "project/dashboard/index.html")


def your_django_endpoint(request):
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    if request.method == "POST":
        json_data = json.loads(request.body.decode('utf-8'))

      # Access the 'amount' value from the JSON data
        amount = int(json_data.get('amount'))
        print(amount)

        client = razorpay.Client(auth=("rzp_test_sG6dp9hQK41vti", "wzHZaza8eVIddzVa4micywqO"))

        payment = client.order.create({"amount": f"{amount*100}", 'currency': 'INR', 'payment_capture': 1})
        context = {'payment': payment}
        

        print("**********************paymant****", payment)
        #database.child(f"order_id").set(payment['id'])
        # Generate a unique order ID

        response_data = {"order_id": payment['id']}
        return JsonResponse(response_data)







