def p(xg):
    print(xg)

import datetime

today=datetime.date.today()
print(today)

birthday=datetime.date(1999,11,14)


print(repr(birthday))

days_since_birthday=(today-birthday).days
print(days_since_birthday)


# by datetime.timedelta(days=0) we can add days according to the calender


time_Delta=datetime.timedelta(days=500)
# use + for add days
print(today+time_Delta)


time_less=datetime.timedelta(days=-10)
# use - to subtract days
print(today-time_Delta)

print(today.weekday())
print(today.weekday())
# weekday() will give 0-6 numbers where 0 = Monday and 6=Sunday
days=["monday","Tuesday","wednesday","Thursday","Friday","Saturday","Sunday"]

print(days[birthday.weekday()])
print(datetime.time(19,46,15,25))

# datetime.date (Year,Months,Days)
# datetime.time (hours,minutes,seconds,microseconds)
# datetime.datetime (Year,Months,Days, hours,minutes,seconds,microseconds )

print(datetime.datetime(2021,2,23,19,51,12,25))

add_Hours=datetime.timedelta(hours=24)

print(today+add_Hours)


def getbirthday(y,m,d):
    birthdate=datetime.date(y,m,d)
    Now = datetime.date.today()
    days_passed = (Now-birthdate).days
    print(days_passed , " days passed After the Birth ")
    print("weekday was :", days[birthdate.weekday()])


getbirthday(1999, 11, 14)
import pytz
print("without it")
print(datetime.datetime.now())
print("with it")
nowDate_time = datetime.datetime.now(tz=pytz.UTC)
print((nowDate_time))
datetime_pacific =nowDate_time.astimezone(pytz.timezone('Asia/Dhaka'))
print(datetime_pacific)
import re
pattern = re.compile("[a-zA-Z0-9\.\@\#\$\%\^\&\*\_\-]+/Dhaka+[a-zA-Z0-9\.\@\#\$\%\^\&\*\_\-]+")
def  timezoneF():   
            for tz in pytz.all_timezones:
                
                print(tz)
                print(nowDate_time.astimezone(pytz.timezone(tz)))
                dhaka = pattern.search(tz)
                print(dhaka)
                if(tz=="Asia/Dhaka"):
                    print("================Dhaka==========")



time_Dhaka="sd Asia/Dhaka asdasdsaas"

res=pattern.findall(time_Dhaka)
print(res )


post_date = datetime.datetime(2021, 2, 21,9,20,16,51)

view_post_date = datetime.datetime.today()

was_posted = view_post_date-post_date

print("Posted : ",was_posted.days,"Days Ago")

def inEveryTimeStamp():
    for time_zone in pytz.all_timezones:
        specific_time_zone = view_post_date.astimezone(pytz.timezone(time_zone))
        
        print(time_zone, ":", specific_time_zone.day-post_date.day," days ",
              specific_time_zone.hour-post_date.hour, "Hours Ago")


#inEveryTimeStamp()


print(post_date.hour)

# nice view strftime() function
Nice_time= datetime_pacific.strftime('%B %d, %Y')
print(Nice_time)

p(type(Nice_time))
p(repr(Nice_time))
#its a string
# so I can't do time calcululation on  it


date_time_thing=datetime.datetime.strptime("March 09, 2019","%B %d, %Y")
p(date_time_thing.day)
























# nowDate_time = datetime.datetime.now(tz=pytz.UTC)
# print((nowDate_time))
# datetime_pacific = nowDate_time.astimezone(pytz.timezone('Asia/Dhaka'))


# Time_now = datetime.datetime.now()

# p(Time_now)

# another_time_zone = Time_now.astimezone(pytz.timezone("Asia/Dhaka"))
# p(another_time_zone)


