import datetime as dt
from urllib.request import urlopen
from twilio.rest import Client




def alert():
    # code for inputing date and package(for scheduling date) to be sended
    user_date = input('Enter The Date in yyyy/mm/dd: ')
    date_elemnts = user_date.split('/')
    year = int(date_elemnts[0])
    month = int(date_elemnts[1])
    day = int(date_elemnts[2])
    package = int(input("Enter the package(in month): "))
    updated_month = month + package
    modulated_month = updated_month % 12

    if updated_month > 12:
        year += 1
        month = modulated_month
    else:
        month = modulated_month

    expiry = dt.date(year, month, day)

    # code for matching the user input date and current date, then send sms
    res = urlopen('http://just-the-time.appspot.com/') # gives current date (not system date)
    result = str(res.read()) # read the current date
    lis = result[2:12:1].split("-") # format the date
    current_year = int(lis[0])
    current_month = int(lis[1])
    current_date = int(lis[2])
    today = dt.date(current_year, current_month, current_date) # assigning date 

    if expiry == today:
        account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx' # your twillio account_sid
        auth_token = 'xxxxxxxxxxxxxxxxxxxxxx' # your twillio auth_token
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body="Your Content", # your sms content 
                            from_='xxxxxxxxx', # your twillio number
                            to='xxxxxxxxx' # To number (Must be registerd in twillio for trial)
                        )

        print(message.sid) # print sms status
        print("sented sms")

    else:
        print("dont send")

alert() 
