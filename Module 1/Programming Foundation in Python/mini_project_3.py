from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = 'AC88c3c521ee0d2a725c8f5843721ae8fe'
auth_token = 'c762ce7422ff19da7f59416748cd785e'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='A class is a blueprint of something which has information of the building',
    to ='+2349030643902', #Replace with your phone number
    from_ = '+14432031069'#replace with twilio number
)
print(message.sid)