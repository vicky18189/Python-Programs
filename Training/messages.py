# from twilio.rest import Client 
 
# account_sid = 'AC61b5653f50545a0022e59ac8fa121c23' 
# auth_token = '042dc2fcdbaad97835ad62dba49cd6e5' 
# client = Client(account_sid, auth_token) 
 
# message = client.messages.create(  
#                               messaging_service_sid='MGe231fdbd19412b060ae889500ee5bd4b', 
#                               body='Hello from Python!',      
#                             #   from_='+917990908251',
#                               to='+917990908251' 
#                           ) 
 
# print(message.sid)

from twilio.rest import Client 
 
account_sid = 'AC61b5653f50545a0022e59ac8fa121c23' 
auth_token = '042dc2fcdbaad97835ad62dba49cd6e5' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to='whatsapp:+919426532819' 
                          ) 
 
print(message.sid)