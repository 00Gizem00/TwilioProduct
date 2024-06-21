from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

def send_sms(to, message):
    account_sid = os.getenv("ACCOUNT_SID")
    auth_token = os.getenv("AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_=os.getenv("TW_NUMBER"),
        to=to
    )
    return message.sid
