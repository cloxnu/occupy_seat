from login import *

cookie = ""

# login
print("1")
cookie_str, text = login(uname, password)
cookie = merge_cookie(cookie, cookie_str)
print("Cookie: ", cookie)
print("Res text: ", text)

# text to json object
text_json = json.loads(text)

# login get more cookie
print("2")
cookie_str, text = get_req_to_cookie(text_json["url"], cookie_str)
cookie = merge_cookie(cookie, cookie_str)
print("Cookie: ", cookie)
print("Res text: ", text)

# get oauth cookie
print("3")
cookie_str, text = get_oauth(cookie)
cookie = merge_cookie(cookie, cookie_str)
print("Cookie: ", cookie)
# print("Res text: ", text)

# get seat select token
print("4")
token = get_seat_token(roomId, day, cookie)
print("token", token)

# gotcha
print("5")
text = gotcha(roomId, startTime, endTime, day, seatNum, token, cookie)
print(text)
