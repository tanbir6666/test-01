from twilio.rest import TwilioRestClient

from credentials import account_sid , author_token, my_cell ,my_twilio

client=TwilioRestClient(account_sid,auth_token)

my_msg="Hi i have a massage . What  you have for me? "

massage = client.massage.create(to=my_cell,from_=my_twilio,body=my_msg)

C