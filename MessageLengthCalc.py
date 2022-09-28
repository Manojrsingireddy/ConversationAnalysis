import sqlite3
import pandas as pd

#Connect to SQLite DB
sqlLiteConnection = sqlite3.connect('/Users/nihanthattaluri/Library/Messages/chat.db')

#Phone Number for Analysis
phoneNumber = "'+1"+ "3315752217" + "'"


#SQLite Querying
messages = pd.read_sql_query("select text FROM message WHERE is_from_me = 0 ORDER BY date", sqlLiteConnection)

#Close SQLite Connection
if(sqlLiteConnection): sqlLiteConnection.close()


