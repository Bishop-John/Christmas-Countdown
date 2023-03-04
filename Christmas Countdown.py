import datetime, time

print("CHRISTMAS IS COMING IN......")

while True:
    DateTime= datetime.datetime.now()
    Month= 12-DateTime.month
    Day= 25-DateTime.day
    Hour= 23-DateTime.hour
    Min= 60-DateTime.minute
    Sec= 60-DateTime.second

    print (Month, "Months", Day,"Days", Hour,"Hours", Min ,"Minutes", Sec, "Seconds")
    time.sleep(1)
