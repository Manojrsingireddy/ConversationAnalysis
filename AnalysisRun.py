import sqlite3
from TimeOfDay import TMDAnalysis
from ProfanityUsage import PFAnalysis
from TimeDifference import TimeDiffAnalysis
from config import sqlLiteConnection


TMDAnalysis()
TimeDiffAnalysis()
PFAnalysis()

# Close Connection to SQLite Database
if(sqlLiteConnection): sqlLiteConnection.close()