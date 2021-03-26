import mysql.connector


def readmessages(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT bericht FROM piep")
    rows = cursor.fetchall()
    for i in rows:
        print(i)
    cursor.close()

def placemessages(conn):
    usr_input = input("Welk bericht wil je sturen?")
    usr_nummer = int(input("Wat is je leerlingnummer?"))
    cursor = conn.cursor()
    command = "INSERT INTO piep (bericht, student_nr) VALUES (%s, %s)"
    val = (usr_input, usr_nummer)
    cursor.execute(command, val)
    conn.commit()

def filterhash(conn):
    filt_input = input("Wil je filteren op hashtags? Y/N")
    if filt_input == "Y":
        cursor = conn.cursor()
        cursor.execute("SELECT bericht FROM piep WHERE bericht LIKE '%#%'")
        rows = cursor.fetchall()
        for i in rows:
            print(i)
        cursor.close
    else:
        pass


if __name__ == '__main__':
    conn = mysql.connector.connect(host = "145.74.104.145",
                                    user = "oyszi",
                                   password="Lukasissut123!",
                                   db = "oyszi")
    readmessages(conn)
    filterhash(conn)
    placemessages(conn)
    conn.close()