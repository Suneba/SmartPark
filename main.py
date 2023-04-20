import pyrebase

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
parking_spot_names =[]
latitude_list = []
longitude_list =[]
dict_for_pk_spots = {}

# for i in range(1, 4):
#     name = (database.child(f"parking_spots/parking_{i}/details/name").get().val())ng_{i}/
#     lat = (database.child(f"parking_spots/parking_{i}/details/lat").get().val())
#     lon = (database.child(f"parking_spots/parking_{i}/details/lon").get().val())
#
#     dict_for_pk_spots[i] = [name]
#     print(parking_spot_names.append(name))
#     print(latitude_list.append(lat))
#     print(longitude_list.append(lon))
# print(dict_for_pk_spots)


# database.child(f"parking_spots/parking_3").child(f"spot_num/spot_1/curr_num_plate").set("123")
# database.child(f"parking_spots/parking_3").child(f"spot_num/spot_1/curr_num_plate/in_time").set("123")
# database.child(f"parking_spots/parking_3").child(f"spot_num/spot_1/curr_num_plate/out_time").set("123")
database.child(f"parking_spots/parking_3").child(f"spot_num/spot_1/old_num_plate/num_plate__date_time/num_plate").set("DL123F3")
database.child(f"parking_spots/parking_3").child(f"spot_num/spot_1/old_num_plate/num_plate__date_time/in_time").set("time")
database.child(f"parking_spots/parking_3").child(f"spot_num/spot_1/old_num_plate/num_plate__date_time/out_time").set("time")
database.child(f"parking_spots/parking_3").child(f"spot_num/spot_1/old_num_plate/num_plate__date_time/duration").set("time")


