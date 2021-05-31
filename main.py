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

    text_file.write("</apteka>\n")
    text_file.close()


def Praca_w_laboratorium(connection):
    cursor = connection.cursor()
    cursor.execute("""select id_Praca_w_laboratorium from Praca_w_laboratorium""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]
    text_file = open("file.xml", "a")
    text_file.write("<praca_w_laboratorium>\n")
    for i in range(1, last_id + 1):
        convert = str(i)
        id = "select id_praca_w_laboratorium from Praca_w_laboratorium where id_praca_w_laboratorium = "+convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_praca_w_laboratorium>"+result+"</id_praca_w_laboratorium>\n")

        id = "select przygotowywany_lek from Praca_w_laboratorium where id_praca_w_laboratorium = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<przygotowywany_lek>" + result + "</przygotowywany_lek>\n")

    text_file.write("</praca_w_laboratorium>\n")
    text_file.close()


def Hurtownia(connection):
    cursor = connection.cursor()
    cursor.execute("""select id_hurtownia from Hurtownia""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]
    text_file = open("file.xml", "a")
    text_file.write("<hurtownia>\n")
    for i in range(1, last_id + 1):
        convert = str(i)
        id = "select id_hurtownia from Hurtownia where id_hurtownia = "+convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_hurtownia>"+result+"</id_hurtownia>\n")

        id = "select nazwa_hurtownii from Hurtownia where id_hurtownia = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<nazwa_hurtownii>" + result + "</nazwa_hurtownii>\n")

        id = "select imie from Hurtownia where id_hurtownia = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<imie>" + result + "</imie>\n")

        id = "select nazwisko from Hurtownia where id_hurtownia = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<nazwisko>" + result + "</nazwisko>\n")

        id = "select miasto from Hurtownia where id_hurtownia = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<miasto>" + result + "</miasto>\n")

        id = "select kod_pocztowy from Hurtownia where id_hurtownia = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<kod_pocztowy>" + result + "</kod_pocztowy>\n")

    text_file.write("</hurtownia>\n")
    text_file.close()


def Producenci(connection):
    cursor = connection.cursor()
    cursor.execute("""select id_producenci from Producenci""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]
    text_file = open("file.xml", "a")
    text_file.write("<producenci>\n")
    for i in range(1, last_id + 1):
        convert = str(i)
        id = "select id_producenci from Producenci where id_producenci = "+convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_producenci>"+result+"</id_producenci>\n")

        id = "select nazwa_producenta from Producenci where id_producenci = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<nazwa_producenta>" + result + "</nazwa_producenta>\n")

        id = "select kraj_pochodzenia from Producenci where id_producenci = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<kraj_pochodzenia>" + result + "</kraj_pochodzenia>\n")

    text_file.write("</producenci>\n")
    text_file.close()


def Pracownicy(connection):
    cursor = connection.cursor()
    cursor.execute("""select id_pracownicy from Pracownicy""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]
    text_file = open("file.xml", "a")
    text_file.write("<pracownicy>\n")
    for i in range(1, last_id + 1):
        convert = str(i)
        id = "select id_pracownicy from Pracownicy where id_pracownicy = "+convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_pracownicy>"+result+"</id_pracownicy>\n")

        id = "select imie from Pracownicy where id_pracownicy = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<imie>" + result + "</imie>\n")

        id = "select nazwisko from Pracownicy where id_pracownicy = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<nazwisko>" + result + "</nazwisko>\n")

        id = "select data_urodzenia from Pracownicy where id_pracownicy = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        result = result[:10]
        text_file.write("<data_urodzenia>" + result + "</data_urodzenia>\n")

        id = "select wynagrodzenie from Pracownicy where id_pracownicy = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<wynagrodzenie>" + result + "</wynagrodzenie>\n")

        id = "select data_dolaczenia_do_firmy from Pracownicy where id_pracownicy = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        result = result[:10]
        text_file.write("<data_dolaczenia_do_firmy>" + result + "</data_dolaczenia_do_firmy>\n")

        id = "select stanowisko from Pracownicy where id_pracownicy = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<stanowisko>" + result + "</stanowisko>\n")


    text_file.write("</pracownicy>\n")
    text_file.close()


def Laboratorium(connection):
    cursor = connection.cursor()
    cursor.execute("""select id_laboratorium from Laboratorium""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]
    text_file = open("file.xml", "a")
    text_file.write("<laboratorium>\n")
    for i in range(1, last_id + 1):
        convert = str(i)
        id = "select id_laboratorium from Laboratorium where id_laboratorium = "+convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_laboratorium>"+result+"</id_laboratorium>\n")

        id = "select dzien_dostepu from Laboratorium where id_laboratorium = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        result = result[:10]
        text_file.write("<dzien_dostepu>" + result + "</dzien_dostepu>\n")

        id = "select czas_w_laboratorium_w_godz from Laboratorium where id_laboratorium = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<czas_w_laboratorium_w_godz>" + result + "</czas_w_laboratorium_w_godz>\n")

        id = "select godzina_rozpoczecia from Laboratorium where id_laboratorium = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<godzina_rozpoczecia>" + result + "</godzina_rozpoczecia>\n")

        id = "select id_pracownicy from Laboratorium where id_laboratorium = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_pracownicy>" + result + "</id_pracownicy>\n")

        id = "select id_praca_w_laboratorium from Laboratorium where id_laboratorium = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_praca_w_laboratorium>" + result + "</id_praca_w_laboratorium>\n")

    text_file.write("</laboratorium>\n")
    text_file.close()


def Klienci(connection):
    cursor = connection.cursor()
    cursor.execute("""select id_klienci from Klienci""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]
    text_file = open("file.xml", "a")
    text_file.write("<klienci>\n")
    for i in range(1, last_id + 1):
        convert = str(i)
        id = "select id_klienci from Klienci where id_klienci = "+convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_klienci>"+result+"</id_klienci>\n")

        id = "select imie from Klienci where id_klienci = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<imie>" + result + "</imie>\n")

        id = "select nazwisko from Klienci where id_klienci = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<nazwisko>" + result + "</nazwisko>\n")

        id = "select pesel from Klienci where id_klienci = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<pesel>" + result + "</pesel>\n")

        id = "select nr_telefonu from Klienci where id_klienci = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<nr_telefonu>" + result + "</nr_telefonu>\n")

        id = "select id_adres_klienta from Klienci where id_klienci = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_adres_klienta>" + result + "</id_adres_klienta>\n")

    text_file.write("</klienci>\n")
    text_file.close()


def Leki(connection):
    cursor = connection.cursor()
    cursor.execute("""select id_leki from Leki""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]
    text_file = open("file.xml", "a")
    text_file.write("<leki>\n")
    for i in range(1, last_id + 1):
        convert = str(i)
        id = "select id_leki from Leki where id_leki = "+convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_leki>"+result+"</id_leki>\n")

        id = "select nazwa_leku from Leki where id_leki = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<nazwa_leku>" + result + "</nazwa_leku>\n")

        id = "select kategoria_leku from Leki where id_leki = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<kategoria_leku>" + result + "</kategoria_leku>\n")

        id = "select cena_oferowana from Leki where id_leki = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<cena_oferowana>" + result + "</cena_oferowana>\n")

        id = "select id_hurtownia from Leki where id_leki = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_hurtownia>" + result + "</id_hurtownia>\n")

        id = "select id_producenci from Leki where id_leki = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_producenci>" + result + "</id_producenci>\n")

    text_file.write("</leki>\n")
    text_file.close()


def Partia_leku(connection):
    cursor = connection.cursor()
    cursor.execute("""select id_partia_leku from Partia_leku""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]
    text_file = open("file.xml", "a")
    text_file.write("<partia_leku>\n")
    for i in range(1, last_id + 1):
        convert = str(i)
        id = "select id_partia_leku from Partia_leku where id_partia_leku = "+convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_partia_leku>"+result+"</id_partia_leku>\n")

        id = "select partia from Partia_leku where id_partia_leku = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<partia>" + result + "</partia>\n")

        id = "select data_waznosci from Partia_leku where id_partia_leku = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        result = result[:10]
        text_file.write("<data_waznosci>" + result + "</data_waznosci>\n")

        id = "select ilosc_sztuk from Partia_leku where id_partia_leku = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<ilosc_sztuk>" + result + "</ilosc_sztuk>\n")

        id = "select cena_kupna from Partia_leku where id_partia_leku = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<cena_kupna>" + result + "</cena_kupna>\n")

        id = "select id_leki from Partia_leku where id_partia_leku = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_leki>" + result + "</id_leki>\n")

        id = "select id_apteka from Partia_leku where id_partia_leku = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_apteka>" + result + "</id_apteka>\n")

    text_file.write("</partia_leku>\n")
    text_file.close()


def Zamowienia(connection):
    cursor = connection.cursor()
    cursor.execute("""select id_zamowienia from Zamowienia""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]
    text_file = open("file.xml", "a")
    text_file.write("<zamowienia>\n")
    for i in range(1, last_id + 1):
        convert = str(i)
        id = "select id_zamowienia from Zamowienia where id_zamowienia = "+convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_zamowienia>"+result+"</id_zamowienia>\n")

        id = "select nr_recepty from Zamowienia where id_zamowienia = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<nr_recepty>" + result + "</nr_recepty>\n")

        id = "select data_zamowienia from Zamowienia where id_zamowienia = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        result = result[:10]
        text_file.write("<data_zamowienia>" + result + "</data_zamowienia>\n")

        id = "select id_klienci from Zamowienia where id_zamowienia = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_klienci>" + result + "</id_klienci>\n")

        id = "select id_pracownicy1 from Zamowienia where id_zamowienia = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_pracownicy1>" + result + "</id_pracownicy1>\n")

        id = "select id_apteka1 from Zamowienia where id_zamowienia = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_apteka1>" + result + "</id_apteka1>\n")

    text_file.write("</zamowienia>\n")
    text_file.close()


def Informacje_o_zamowieniu(connection):
    cursor = connection.cursor()
    cursor.execute("""select id_informacje_o_zamowieniu from Informacje_o_zamowieniu""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]
    text_file = open("file.xml", "a")
    text_file.write("<informacje_o_zamowieniu>\n")
    for i in range(1, last_id + 1):
        convert = str(i)
        id = "select id_informacje_o_zamowieniu from Informacje_o_zamowieniu where id_informacje_o_zamowieniu = "+convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<informacje_o_zamowieniu>"+result+"</informacje_o_zamowieniu>\n")

        id = "select cena_sprzedazy from Informacje_o_zamowieniu where id_informacje_o_zamowieniu = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<cena_sprzedazy>" + result + "</cena_sprzedazy>\n")

        id = "select mozliwa_znizka_refundacja from Informacje_o_zamowieniu where id_informacje_o_zamowieniu = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<mozliwa_znizka_refundacja>" + result + "</mozliwa_znizka_refundacja>\n")

        id = "select id_zamowienia from Informacje_o_zamowieniu where id_informacje_o_zamowieniu = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_zamowienia>" + result + "</id_zamowienia>\n")

        id = "select id_leki1 from Informacje_o_zamowieniu where id_informacje_o_zamowieniu = " + convert
        cursor.execute(id)
        result = cursor.fetchone()[0]
        result = str(result)
        text_file.write("<id_leki1>" + result + "</id_leki1>\n")

    text_file.write("</informacje_o_zamowieniu>\n")
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
    columns = 5
    length = len(h) / columns
    convert = int(length)
    g = 0
    for j in range(convert):
        cursor = connection.cursor()
        cursor.execute(
            "insert into Adres_klienta values(" + h[g] + ",\'" + h[g + 1] + "\',\'" + h[g + 2] + "\',\'" + h[
                g + 3] + "\',\'" + h[g + 4] + "\')")
        connection.commit()
        g += columns


def Insert_Apteka(connection):
    mytree = ET.parse('file.xml')
    myroot = mytree.getroot()
    print(myroot[1].tag)
    h = []
    for x in myroot[1]:
        h.append(x.text)
    for i in range(len(h)):
        print(h[i])
    columns = 5
    length = len(h) / columns
    convert = int(length)
    g = 0
    for j in range(convert):
        cursor = connection.cursor()
        cursor.execute("insert into Apteka values("+h[g]+",\'"+h[g+1]+"\',\'"+h[g+2]+"\',\'"+h[g+3]+"\',\'"+h[g+4]+"\')")
        connection.commit()
        g += columns


def Insert_Praca_w_laboratorium(connection):
    mytree = ET.parse('file.xml')
    myroot = mytree.getroot()
    print(myroot[2].tag)
    h = []
    for x in myroot[2]:
        h.append(x.text)
    for i in range(len(h)):
        print(h[i])
    columns = 2
    length = len(h) / columns
    convert = int(length)
    g = 0
    for j in range(convert):
        cursor = connection.cursor()
        cursor.execute("insert into Praca_w_laboratorium values("+h[g]+",\'"+h[g+1]+"\')")
        connection.commit()
        g += columns


def Insert_Hurtownia(connection):
    mytree = ET.parse('file.xml')
    myroot = mytree.getroot()
    print(myroot[3].tag)
    h = []
    for x in myroot[3]:
        h.append(x.text)
    for i in range(len(h)):
        print(h[i])
    columns = 6
    length = len(h) / columns
    convert = int(length)
    g = 0
    for j in range(convert):
        cursor = connection.cursor()
        cursor.execute("insert into Hurtownia values("+h[g]+",\'"+h[g+1]+"\',\'"+h[g+2]+"\',\'"+h[g+3]+"\',\'"+h[g+4]+"\',\'"+h[g+5]+"\')")
        connection.commit()
        g += columns


def Insert_Producenci(connection):
    mytree = ET.parse('file.xml')
    myroot = mytree.getroot()
    print(myroot[4].tag)
    h = []
    for x in myroot[4]:
        h.append(x.text)
    for i in range(len(h)):
        print(h[i])
    columns = 3
    length = len(h) / columns
    convert = int(length)
    g = 0
    for j in range(convert):
        cursor = connection.cursor()
        cursor.execute("insert into Producenci values("+h[g]+",\'"+h[g+1]+"\',\'"+h[g+2]+"\')")
        connection.commit()
        g += columns


def Insert_Pracownicy(connection):
    mytree = ET.parse('file.xml')
    myroot = mytree.getroot()
    print(myroot[5].tag)
    h = []
    for x in myroot[5]:
        h.append(x.text)
    for i in range(len(h)):
        print(h[i])
    columns = 7
    length = len(h) / columns
    convert = int(length)
    g = 0
    for j in range(convert):
        cursor = connection.cursor()
        cursor.execute("insert into Pracownicy values("+h[g]+",\'"+h[g+1]+"\',\'"+h[g+2]+"\', to_date(\'"+h[g+3]+"\',\'RRRR-MM-DD\'),\'"+h[g+4]+"\',to_date(\'"+h[g+5]+"\',\'RRRR-MM-DD\'),\'"+h[g+6]+"\')")
        connection.commit()
        g += columns


def Insert_Laboratorium(connection):
    mytree = ET.parse('file.xml')
    myroot = mytree.getroot()
    print(myroot[6].tag)
    h = []
    for x in myroot[6]:
        h.append(x.text)
    for i in range(len(h)):
        print(h[i])
    columns = 6
    length = len(h) / columns
    convert = int(length)
    g = 0
    for j in range(convert):
        cursor = connection.cursor()
        cursor.execute("insert into Laboratorium values("+h[g]+",to_date(\'"+h[g+1]+"\',\'RRRR-MM-DD\'),\'"+h[g+2]+"\',\'"+h[g+3]+"\',\'"+h[g+4]+"\',\'"+h[g+5]+"\')")
        connection.commit()
        g += columns


def Insert_Klienci(connection):
    mytree = ET.parse('file.xml')
    myroot = mytree.getroot()
    print(myroot[7].tag)
    h = []
    for x in myroot[7]:
        h.append(x.text)
    for i in range(len(h)):
        print(h[i])
    columns = 6
    length = len(h) / columns
    convert = int(length)
    g = 0
    for j in range(convert):
        cursor = connection.cursor()
        cursor.execute("insert into Klienci values("+h[g]+",\'"+h[g+1]+"\',\'"+h[g+2]+"\',\'"+h[g+3]+"\',\'"+h[g+4]+"\',\'"+h[g+5]+"\')")
        connection.commit()
        g += columns


def Insert_Leki(connection):
    mytree = ET.parse('file.xml')
    myroot = mytree.getroot()
    print(myroot[8].tag)
    h = []
    for x in myroot[8]:
        h.append(x.text)
    for i in range(len(h)):
        print(h[i])
    columns = 6
    length = len(h) / columns
    convert = int(length)
    g = 0
    for j in range(convert):
        cursor = connection.cursor()
        cursor.execute("insert into Leki values("+h[g]+",\'"+h[g+1]+"\',\'"+h[g+2]+"\',\'"+h[g+3]+"\',\'"+h[g+4]+"\',\'"+h[g+5]+"\')")
        connection.commit()
        g += columns


def Insert_Partia_leku(connection):
    mytree = ET.parse('file.xml')
    myroot = mytree.getroot()
    print(myroot[9].tag)
    h = []
    for x in myroot[9]:
        h.append(x.text)
    for i in range(len(h)):
        print(h[i])
    columns = 7
    length = len(h) / columns
    convert = int(length)
    g = 0
    for j in range(convert):
        cursor = connection.cursor()
        cursor.execute("insert into Partia_leku values("+h[g]+",\'"+h[g+1]+"\',to_date(\'"+h[g+2]+"\',\'RRRR-MM-DD\'),\'"+h[g+3]+"\',\'"+h[g+4]+"\',\'"+h[g+5]+"\',\'"+h[g+6]+"\')")
        connection.commit()
        g += columns


def Insert_Zamowienia(connection):
    mytree = ET.parse('file.xml')
    myroot = mytree.getroot()
    print(myroot[10].tag)
    h = []
    for x in myroot[10]:
        h.append(x.text)
    for i in range(len(h)):
        print(h[i])
    columns = 6
    length = len(h) / columns
    convert = int(length)
    g = 0
    for j in range(convert):
        cursor = connection.cursor()
        cursor.execute("insert into Zamowienia values("+h[g]+",\'"+h[g+1]+"\',to_date(\'"+h[g+2]+"\',\'RRRR-MM-DD\'),\'"+h[g+3]+"\',\'"+h[g+4]+"\',\'"+h[g+5]+"\')")
        connection.commit()
        g += columns


def Insert_Informacje_o_zamowieniu(connection):
    mytree = ET.parse('file.xml')
    myroot = mytree.getroot()
    print(myroot[11].tag)
    h = []
    for x in myroot[11]:
        h.append(x.text)
    for i in range(len(h)):
        print(h[i])
    columns = 5
    length = len(h) / columns
    convert = int(length)
    g = 0
    for j in range(convert):
        cursor = connection.cursor()
        cursor.execute("insert into Informacje_o_zamowieniu values("+h[g]+",\'"+h[g+1]+"\',\'"+h[g+2]+"\',\'"+h[g+3]+"\',\'"+h[g+4]+"\')")
        connection.commit()
        g += columns


ip = '217.173.198.135'
port = 1522
SID = 'orcltp'
dsn_tns = cx_Oracle.makedsn(ip, port, SID)
connection = cx_Oracle.connect('s97628', 'lukluk12', dsn_tns)

print('1 - eksport z bazy 2 - import z pliku do bazy')
x = int(input())

if x == 1:
    Prepare_file()
    Adres_klienta(connection)
    Apteka(connection)
    Praca_w_laboratorium(connection)
    Hurtownia(connection)
    Producenci(connection)
    Pracownicy(connection)
    Laboratorium(connection)
    Klienci(connection)
    Leki(connection)
    Partia_leku(connection)
    Zamowienia(connection)
    Informacje_o_zamowieniu(connection)
    End_file()
elif x == 2:
    Insert_Adres_klienta(connection)
    Insert_Apteka(connection)
    Insert_Praca_w_laboratorium(connection)
    Insert_Hurtownia(connection)
    Insert_Producenci(connection)
    Insert_Pracownicy(connection)
    Insert_Laboratorium(connection)
    Insert_Klienci(connection)
    Insert_Leki(connection)
    Insert_Partia_leku(connection)
    Insert_Zamowienia(connection)
    Insert_Informacje_o_zamowieniu(connection)
