# Diese Datei dient dazu, über all da wo wir im Code eine Verbindung mit der Datenbank aufbauen wollen, den Code übersichtlicher zu gestalten
# Dadurch können wir über die Variable "conn" die "Zugansdaten" von hier holen und müssen sie nicht jedes mal neu coden
# Zusätzlich gewinnen wir den Vorteil, die Daten hier zentral verwalten zu können

import mysql.connector
from mysql.connector import Error
conn = mysql.connector.connect(host='localhost',
                                         database='library_management',
                                         user='root',
                                         password='3956')