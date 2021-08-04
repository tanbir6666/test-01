import datetime as da
myBirthDate=da.date(1999,11,14)
def p(ffff):
    print(ffff)

todays_date=da.date.today()

def age(birth):
    age_in_days = todays_date-birth
    age_in_days_int=age_in_days.days
    in_timedelta_format= da.timedelta(days=age_in_days_int)
    # print(in_timedelta_format)
    zero_time_Delta=da.timedelta(days=(366+30))
    zero_date=da.date(1,1,1)
    how_many_Y_M_D = zero_date+in_timedelta_format
    my_absulute_age=how_many_Y_M_D-zero_time_Delta
    #p(my_absulute_age)
    # '#' used for remove '0' before  years and others . in linux "-" used to remove zero like '#'
    nice_date= my_absulute_age.strftime("%m %d, %Y")
    nice_Date_in_date_format = da.datetime.strptime(nice_date , "%m %d, %Y")
    #p((nice_date,type(nice_date)))
    months=nice_Date_in_date_format.month
    days = nice_Date_in_date_format.day
    year = nice_Date_in_date_format.year
    print(year, "Years", months,"Months",days,"days")


age(myBirthDate)
age(da.date(2010,4,12))
age(da.date(2010,1,1))

