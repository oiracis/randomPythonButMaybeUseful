#oiracis
import requests, time
s = requests.session()
def captcha():
    ans = "CAPCHA_NOT_READY";
    r = s.get("http://sitewherethecaptcha.is/located")
    with open("captcha.png", "wb+") as image:
        image.write(r.content)
        image.close()
    files = {"file":open("captcha.png", "rb")}
    cha = requests.post("http://2captcha.com/in.php", data={"key":"0", "method":"post", "json":1}, files=files).json()
    while (ans == "CAPCHA_NOT_READY"):
        chares = requests.get("http://2captcha.com/res.php?key=0&action=get&json=1&id=" + cha["request"]).json()
        ans = chares["request"].upper()
        time.sleep(5)
    print(ans)
captcha()
