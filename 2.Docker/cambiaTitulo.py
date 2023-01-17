#!usr/bin/python3

import os

#Obtenemos el valor de la variable de entorno
group_number = "" if (os.environ.get("GROUP_NUMBER") is None) else os.environ.get("GROUP_NUMBER")
print("hola" + str(group_number))

#Cambiamos el título de la página
fin = open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "r")
fout = open("productpage.html", "w")
for line in fin: 
  if "Simple Bookstore App" in line:
    fout.write("{% block title %}Simple Bookstore App Grupo:" + str(group_number) + "{% endblock %}")
  else: 
    fout.write(line)
fin.close()
fout.close()
os.system("mv productpage.html practica_creativa2/bookinfo/src/productpage/templates/productpage.html")
