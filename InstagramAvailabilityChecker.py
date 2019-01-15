#oiracis
#its just a concept that can probably be improved. Just worked on it like 15 mins
import requests
input()
def genToken(): #generate new token
    r = requests.post("https://www.instagram.com/accounts/web_create_ajax/attempt/")
    return r.headers["Set-Cookie"].split("csrftoken=")[1].split(";")[0]

with open("list.txt","r+") as x: #open usernames file
    list = x.read().splitlines()
    x.close()
out = open("available.txt","w+")
token = genToken() #initial token

for c,x in enumerate(list, 1):
    if (c == 10):
        token = genToken()
    r = requests.post("https://www.instagram.com/accounts/web_create_ajax/attempt/", headers={"X-CSRFToken":token,"Connection":"close"}, data={"username":x}).json()
    try:
        if (r["errors"]["username"][0]["code"] == "username_is_taken"):
            print("Not available:\t" + x)
    except:
        print("Available:\t" + x)
        out.write(x + "\n")
        out.flush()
