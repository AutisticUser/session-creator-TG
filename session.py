#session creator script py @VX_org
import os
if not os.path.exists("session"):
    os.makedirs("session")
try:
    from telethon import TelegramClient, sync, events, functions, types
    import sqlite3
    from time import sleep
    from telethon.errors import *
except:
    os.system("pip install telethon")
def my_session():
    phone = input("/hi VX\ - Enter Telegram login phone number (+123456789) : ")
    try:
        api_id = 12872257
        api_hash = 'c5d976a048c21b21b893736511570f43'
        client = TelegramClient("session/"+phone,api_id,api_hash)
        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone)
                client.sign_in(phone,input("/VX\ - Enter code : "))
                print ("Successful session creation "+phone)
                with open("list.txt","a") as file:
                    file.write(phone+"\n")
                client.disconnect()
            except SessionPasswordNeededError:
                client.start(phone,input('/VX\ - Enter password:'))
                print ("Successful session creation "+phone)
                with open("list.txt","a") as file:
                    file.write(phone+"\n")
                client.disconnect()
            except PhoneNumberBannedError:
                print ("Band account")
                client.disconnect()
        else:
            print("Session already available")
            client.disconnect()
    except (sqlite3.DatabaseError, sqlite3.OperationalError):
        print("Session error, delete old session file and create new one")
    except Exception as e:
        print(e)
print("CTRL C to disable the tool")
while(True):
    my_session()