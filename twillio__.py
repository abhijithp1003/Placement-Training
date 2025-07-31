from twilio.rest import Client

account_sid = ""
auth_token = ""
twilio_number = ""
num = "+1234567890"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hey! Good morning",
    from_=twilio_number,
    to=num
)

print("Message sent. SID:", message.sid)
