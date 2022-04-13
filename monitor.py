import requests
from time import sleep
from sinchsms import SinchSMS

def sendSMS():
    number = 'your_mobile_number'
    app_key = 'your_app_key'
    app_secret = 'your_app_secret'
    message = 'Your Site is DOWN!!'
 
    client = SinchSMS(app_key, app_secret)
    print("Sending '%s' to %s" % (message, number))
 
    response = client.send_message(number, message)
    message_id = response['messageId']
    response = client.check_status(message_id)
 
    # keep trying unless the status returned is Successful
    while response['status'] != 'Successful':
        print(response['status'])
        time.sleep(1)
        response = client.check_status(message_id)
 
    print(response['status'])
 
if __name__ == "__main__":
    r= requests.get(Site_to_check,timeout=5)
    if r.status_code != 200 : 
        sendSMS()
