#oiracis
import requests
from time import sleep

def recaptcha():
    apikey = "0" # Your 2Captcha API Key
    key = "0" # Website Key
    website = "https://sitewherethecaptcha.is/located" #URL of the website
    captcha_id = requests.get("http://2captcha.com/in.php?key=" + apikey + "&method=userrecaptcha&googlekey=" + key + "&pageurl=" + website).text 
    captcha_id = captcha_id.split("|")[1] 
    answer = requests.get("http://2captcha.com/res.php?key=" + apikey + "&action=get&id=" + captcha_id).text
    while "CAPCHA_NOT_READY" in answer: 
        answer = requests.get("http://2captcha.com/res.php?key=" + apikey + "&action=get&id=" + captcha_id).text
        sleep(5) #you may change this
    answer = answer.split("|")[1]
    print(answer)



recaptcha()



