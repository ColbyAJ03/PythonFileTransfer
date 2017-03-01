# DateTime Drill
#
# By Alex Colby
#
# For The Tech Academy
#
#   Purpose: Uses the current time to find the time in NYC and London, and does
#   a comparison to see if the current time is within a store's operating hours.
#   The result of whether a store is Open or Closed is displayed in the shell.

import datetime as dt
from datetime import datetime,timedelta

# get current time and apply time zone changes
def getTime():
    porTime = dt.datetime.now()
    nycTime = porTime + timedelta(hours=3)
    lonTime = porTime + timedelta(hours=8)
    checkTime(nycTime,lonTime)

# receive current time in NYC and London and perform comparison
def checkTime(nycTime,lonTime):
    openTime = dt.time(9,0,0,0)
    closeTime = dt.time(21,0,0,0)
    if nycTime.time() > openTime and nycTime.time() < closeTime:
        nycStatus = "Open"
    else:
        nycStatus = "Closed"
        
    if lonTime.time() > openTime and lonTime.time() < closeTime:
        lonStatus = "Open"
    else:
        lonStatus = "Closed"
    printStatus(nycStatus,lonStatus)

# display results
def printStatus(nycStatus,lonStatus):
    print("The NYC branch is: {}".format(nycStatus))
    print("The London branch is: {}".format(lonStatus))

# begin the program
if __name__ == "__main__":
    getTime()
    
