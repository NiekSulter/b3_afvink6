import mysql.connector
from flask import Markup

def load_messages(username, password, zoekterm):
    conn = mysql.connector.connect(host='hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com',
                                   user=username + '@hannl-hlo-bioinformatica-mysqlsrv',
                                   password= password,
                                   db='bioinfadmin')


    cursor = conn.cursor()
    cursor.execute('select bericht, datum, tijd, voornaam from piep join student s on piep.student_nr = s.student_nr '
                   'where bericht like \'%{}%\''.format(zoekterm))


    messages = []
    dates = []
    time = []
    user = []
    for i in cursor:
        messages.append(i[0])
        dates.append(i[1])
        time.append(i[2])
        user.append(i[3])

    return messages, dates, time, user


def insert_message(username, password, bericht):
    conn = mysql.connector.connect(host='hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com',
                                   user=username + '@hannl-hlo-bioinformatica-mysqlsrv',
                                   password=password,
                                   db='bioinfadmin')
    cursor = conn.cursor()
    SQL = "insert into piep (bericht, datum, tijd, student_nr) values (%s, current_date, current_time , %s)"
    val = (bericht, password)
    cursor.execute(SQL, val)

    conn.commit()
