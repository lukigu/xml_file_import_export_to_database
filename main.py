import cx_Oracle
import xml.dom.minidom
cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle_cx")


def Prepare_file():
    text_file = open("file.xml", "w")
    text_file.write("<?xml version=\"1.0\"?>\n")
    # text_file.write("<apteka>\n")
    text_file.close()


def Adres_klienta(connection):
    cursor = connection.cursor()
    cursor.execute("""select id_Adres_klienta from Adres_Klienta""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]
    text_file = open("file.xml", "a")
    text_file.write("<adres_klienta>\n")
    for i in range(1, last_id + 1):
        convert = str(i)
        id = "select id_adres_klienta from adres_klienta where id_adres_klienta = "+convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_adres_klienta>"+result+"</id_adres_klienta>\n")

        id = "select ulica from adres_klienta where id_adres_klienta = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<ulica>" + result + "</ulica>\n")

        id = "select nr_domu from adres_klienta where id_adres_klienta = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<nr_domu>" + result + "</nr_domu>\n")

        id = "select miejscowosc from adres_klienta where id_adres_klienta = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<miejscowosc>" + result + "</miejscowosc>\n")

        id = "select kod_pocztowy from adres_klienta where id_adres_klienta = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<kod_pocztowy>" + result + "</kod_pocztowy>\n")

    text_file.write("</adres_klienta>\n")
    text_file.close()


def Apteka(connection):
    cursor = connection.cursor()
    cursor.execute("""select id_Apteka from Apteka""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]
    text_file = open("file.xml", "a")
    text_file.write("<apteka>\n")
    for i in range(1, last_id + 1):
        convert = str(i)
        id = "select id_apteka from apteka where id_apteka = "+convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_apteka>"+result+"</id_apteka>\n")

        id = "select nazwa from apteka where id_apteka = "+convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<nazwa>" + result + "</nazwa>\n")

        id = "select miejscowosc from apteka where id_apteka = "+convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<miejscowosc>" + result + "</miejscowosc>\n")

        id = "select imie_kierownika from apteka where id_apteka = "+convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<imie_kierownika>" + result + "</imie_kierownika>\n")

        id = "select nazwisko_kierownika from apteka where id_apteka = "+convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<nazwisko_kierownika>" + result + "</nazwisko_kierownika>\n")

    text_file.write("</apteka\n>")
    text_file.close()


def End_file():
    text_file = open("file.xml", "a")
    text_file.write("</apteka>\n")
    text_file.close()


ip = '217.173.198.135'
port = 1522
SID = 'orcltp'
dsn_tns = cx_Oracle.makedsn(ip, port, SID)
connection = cx_Oracle.connect('s97628', 'lukluk12', dsn_tns)

Prepare_file()
Adres_klienta(connection)
Apteka(connection)
# End_file()

