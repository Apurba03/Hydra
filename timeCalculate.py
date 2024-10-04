import time
import datetime
from speak import Speak
from datetime import date

 
list=["January","February","March","April","May","Jun","July","August","September","October","November","December"]

def Time_calculate(Data):

    if "time" in Data:
        now=datetime.datetime.now()
        now=now.strftime("%H:%M")
        Speak(f"The time is {now}.")

    elif "date" in Data:
        now=datetime.datetime.now()
        date=now.strftime("%d")
        month=now.strftime("%m")
        month=int(month)
        year=now.strftime("%y")
        month=list[month-1]
        Speak(f"The date is {date} {month} 20{year}.")

    elif "month" in Data:
        now=datetime.datetime.now()
        month=now.strftime("%m")
        n=month
        month=int(month)
        month=list[month-1]
        Speak(f"The month is {month}.")
        Speak(f"Month no. {n}")
    
    elif "day" in Data:
        day_name={"Monday":1,"Tuesday":2,"Wednesday":3,"Thusday":4,"Friday":5,"Saturday":6,"Sunday":7}
        day=datetime.datetime.now()
        day=day.strftime("%A")
        k=day_name[day]        
        Speak(f"The day is {day}.")
        Speak(f"The no. of day is {day}.")

    else:
        now=datetime.datetime.now()
        year=now.strftime("%y")
        Speak(f"The year is 20{year}.")
