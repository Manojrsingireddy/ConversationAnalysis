from config import sqlLiteConnection
import pandas as pd
from statistics import mean, median
import shutil as sh
import os
#TODO: Test Mean, Adjusted Mean, Median, and Slope

def TimeDiffAnalysis():
    #Phone Number for Analysis
    number = input('What number do you want to compare with for Time Difference Analysis')
    phoneNumber = "'+" + number + "'"

    #SQLite Querying
    ids = pd.read_sql_query("select ROWID from handle where id = " + phoneNumber, sqlLiteConnection)
    handle_id = ids['ROWID'].get(0)

    messages = pd.read_sql_query("select date, is_from_me FROM message WHERE handle_id="+str(handle_id)+" AND group_title IS NULL AND type = 0 ORDER BY date", sqlLiteConnection)

    # Calculate Time Between Messages
    messageTimes = messages['date']
    timeBtwnMssgs = []
    prevDate = messageTimes[0]
    for i in range(1, len(messageTimes)):
        if(messages['is_from_me'].get(i) != messages['is_from_me'].get(i-1)):
            timeBtwnMssgs.append(messageTimes[i] - prevDate)
            prevDate = messages['date'].get(i)
    slope = 0
    for i in range(1, len(timeBtwnMssgs)):
        slope += timeBtwnMssgs[i] - timeBtwnMssgs[i-1]
    avg = slope/len(timeBtwnMssgs)
    timeBtwnMssgs.sort()

    # Print Results to console
    print("Time Difference Analysis Results for " + str(phoneNumber))
    print("Average: " + str(mean(timeBtwnMssgs)/(3.6*10**12)))
    print("Median: " + str(median(timeBtwnMssgs)/(3.6*10**12)))
    print("Adjusted Average: " + str(mean(timeBtwnMssgs[int(len(timeBtwnMssgs)/10):int(len(timeBtwnMssgs)/10*9)])/(3.6*10**12)))
    print("Slope: "+ str(avg/(3.6*10**12)))





