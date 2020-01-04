from twilio.rest import Client
# put your own credentials here
account_sid = "account sid from dash"
auth_token = "auth token from dashboard"
client = Client(account_sid, auth_token)
client.messages.create(
  to="+enter number with country code that you are sending it to",
  from_="+enter twilio phone number",
  body="Woah!! The Twilio API is working!!!",)
