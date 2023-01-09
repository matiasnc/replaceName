"""
Descripcion del script:
En un proyecto laboral, me toco automatizar una serie de web service's, los cuales eran aproximadamente 400. 
Contabamos con los nombres de cada servicio, asi que para agilizar el armado de las url cree un script en 
Python del cual se leen los nombres de los servicios y que me devuelva un archivo de texto con las url ya armadas.
"""

__author__ = "Matias Nahuel Calderon"
__version__ = "1.0"
__email__ = "mn.calderon97@gmail.com"
__status__ = ""

import os, csv

path = 'C:\\Users\\Matias\\Desktop\\Programacion\\Python\\replace\\serv_name.txt'
link = 'http://sts.bancopython.com:8080/WST_name_t10/services?wsdl'
underscore = '_'

with open(path) as csv_file:

    cantFilas = sum(1 for line in csv_file)
    csv_file.seek(0)
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)

    for index in range(cantFilas):
        indexes = [i for i, u in enumerate(link) if u == underscore]
        a = indexes[0]+1
        b = indexes[1]
        replaced=link[a:b]
        newlink=link.replace(replaced, rows[index][0])
        print(newlink)

        newpath = 'C:\\Users\\Matias\\Desktop\\Programacion\\Python\\replace\\new_serv_name.txt'
        f = open(newpath, "a+")
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow([newlink])
        filename = os.path.abspath(newpath)
print(filename)