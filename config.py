import sqlite3
import os
from pathlib import Path

#Find and Connect to SQLite Database
p = Path(os.getcwd())
chatPath = p.parts[0]+p.parts[1]+'/'+ p.parts[2]+'/Library/Messages/chat.db'
sqlLiteConnection = sqlite3.connect(chatPath)