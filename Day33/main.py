# import requests
# from datetime import datetime 

# MY_LAT = 39.738449
# MY_LNG = -104.984848



# def is_above():
#     if  latitude-float(5) < MY_LAT < latitude+float(5):
#         print("above")
#     else:
#         print(("not above"))

# iss_response = requests.get(url= "http://api.open-notify.org/iss-now.json")

# longitude = float(iss_response.json()["iss_position"]["longitude"])
# latitude = float(iss_response.json()["iss_position"]["latitude"])

# iss_position = (longitude, latitude)

# params = {
#     "lat":MY_LAT,
#     "lng":MY_LNG,
#     "formatted": 0,
# }

# response = requests.get(url= "https://api.sunrise-sunset.org/json", params=params)
# response.raise_for_status()

# sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]
# sunset = response.json()["results"]["sunset"].split("T")[1].split(":")[0]

# print(f"{sunrise}, {sunset}")

# time_now = datetime.now().hour

# print(time_now)

# is_above()
