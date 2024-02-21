#python

""" PROBADOR DE DBF A CSV STUDIO AVG"""
import sys
import csv
from dbfread import DBF


def test_reading_dbf_txtplane():
    #encoding latin_1 , utf-8, cp1252, iso-8859-1
    table = DBF('PADFIS.DBF',encoding='latin_1')
    writer = csv.writer(sys.stdout)
    #nombredelascolumnas
    #writer.writerow(table.field_names)
    #print("hola"  + ' ' + "echo")
    for record in table:
        writer.writerow(list(record.values()))
        #go=str(record["DOMICILIO"])
        #print( str(record["CLAVE5"]) + ' ' + (go).encode('utf8') )
        #if str(record["DOMICILIO"]) == '"':
            #print( str(record["DOMICILIO"]) )


def conversor_dbf_csv():
    path=str('PADFIS.DBF')
    csv_path = "archovresultante.csv"
    print(csv_path)
    dbf = DBF(path,encoding='latin_1')
    with open(csv_path, 'w', newline = '',encoding="latin_1") as f:
        writer = csv.writer(f)
        #writer.writerow(dbf.field_names)
        for record in dbf:
            #muestra los datos en forma de lista
            writer.writerow(list(record.values()))
            csv_path


#test_reading_dbf_txtplane()
conversor_dbf_csv()
