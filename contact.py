import requests 
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxc1b5654ea9174aacac1ae49a7fa28664.mailgun.org/messages",
        auth=("api", "key-82cfa1084f619d1cbb2c312843438be8"),
        data={"from": "Excited User <mailgun@sandboxc1b5654ea9174aacac1ae49a7fa28664.mailgun.org>",
              "to": ["ernestina-marfo@hotmail.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})