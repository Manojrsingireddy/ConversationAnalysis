from config import sqlLiteConnection
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path

def TMDAnalysis():
    #SQLite Querying
    messages = pd.read_sql_query("select is_from_me, datetime(date/1000000000 + strftime(\"%s\", \"2001-01-01\") ,\"unixepoch\",\"localtime\")  as date_utc FROM message", sqlLiteConnection)


    # Find Most Popular Time of Day
    messages['hour'] = messages['date_utc'].str.slice(11, 13).astype('int')
    hourcounts = messages['hour'].value_counts()
    morning = 0 #6-12
    afternoon = 0 #12-18
    evening = 0 #18-21
    night = 0 # 21-23 0-6
    hours = []
    counts = []

    for hour, count in hourcounts.items():
        if hour in range(6,12):
            morning += count
        elif hour in range(12, 18):
            afternoon += count
        elif hour in range(18, 21):
            evening += count
        else:
            night += count
        hours.append(hour)
        counts.append(count)
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(hours,counts)
    plt.ylabel('Counts')
    plt.xlabel('Hour')
    plt.title('Time of Day Messages Sent')
    plt.show()



    times = np.array([morning, afternoon, evening, night])
    plt.pie(times,labels = ['morning', 'afternoon','evening','night'], )
    plt.title('Percentage of messages sent at different times of the day')
    plt.show()



    # Print Results to console
    print("Time of Day Analysis Results:")
    print("Messages in the Morning: " + str(morning))
    print("Messages in the Afternoon: "+str(afternoon))
    print("Messages in the Evening: "+ str(evening))
    print("Messages in the Night: "+str(night))






