import mysql.connector
from mysql.connector import Error
conn = mysql.connector.connect(host='localhost',
                                         database='library_management',
                                         user='root',
                                         password='1234')