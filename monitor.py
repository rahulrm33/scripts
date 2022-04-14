import requests

def sendSMS():
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message=Your site is DOWN . Please reboot the server :)&language=english&route=p&numbers=your_mobile_number"
    headers = {
    'authorization': "your_app_key",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

if __name__ == "__main__":
    r= requests.get('your_site_to_check',timeout=5)
    if r.status_code != 200 : 
        sendSMS()
