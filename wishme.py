import datetime

def wish():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<=4:

        n="Sir, you need to go to sleep it's to late to wake up\n take care of your health"

    elif hour>=5 and hour<=12:
        
        n="good morning"

    elif hour>12 and hour<18:

        n="good afternoon"

    else:

        n="good evening"

    return n
