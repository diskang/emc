import pymssql

HOST="202.120.38.227"
DB_USER = "icare-PC\icare"
DB_PW = "qwert"
DB_NAME="EMC"
conn= pymssql.connect(HOST,DB_USER,DB_PW,DB_NAME)
cursor = conn.cursor()