import cx_Oracle
import xml.etree.ElementTree as ET
cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle_cx")


def Prepare_file():
    text_file = open("file.xml", "w")
    text_file.write("<?xml version=\"1.0\"?>\n")
    text_file.write("<metadata>\n")
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
    text_file.write("</metadata>\n")
    text_file.close()


def Insert_Adres_klienta(connection):
    mytree = ET.parse('file.xml')
    myroot = mytree.getroot()
    print(myroot[0].tag)
    h = []
    for x in myroot[0]:
        h.append(x.text)
    for i in range(len(h)):
        print(h[i])
    length = len(h) / 5
    convert = int(length)
    print(convert)
    g = 0
    for j in range(convert):
        cursor = connection.cursor()
        cursor.execute(
            "insert into Adres_klienta values(" + h[g] + ",\'" + h[g + 1] + "\',\'" + h[g + 2] + "\',\'" + h[
                g + 3] + "\',\'" + h[g + 4] + "\')")
        connection.commit()
        g += 5


def Insert_Apteka(connection):
    mytree = ET.parse('file.xml')
    myroot = mytree.getroot()
    print(myroot[1].tag)
    h = []
    for x in myroot[1]:
        h.append(x.text)
    for i in range(len(h)):
        print(h[i])
    length = len(h) / 5
    convert = int(length)
    print(convert)
    g = 0
    for j in range(convert):
        cursor = connection.cursor()
        cursor.execute("insert into Apteka values("+h[g]+",\'"+h[g+1]+"\',\'"+h[g+2]+"\',\'"+h[g+3]+"\',\'"+h[g+4]+"\')")
        connection.commit()
        g += 5


ip = '217.173.198.135'
port = 1522
SID = 'orcltp'
dsn_tns = cx_Oracle.makedsn(ip, port, SID)
connection = cx_Oracle.connect('s97628', 'lukluk12', dsn_tns)

# Prepare_file()
# Adres_klienta(connection)
# Apteka(connection)
# End_file()

Insert_Adres_klienta(connection)
Insert_Apteka(connection)
