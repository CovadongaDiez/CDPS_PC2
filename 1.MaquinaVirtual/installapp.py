#!usr/bin/python3

import os

#Clonamos el repositorio para la práctica
os.system("git clone https://github.com/CDPS-ETSIT/practica_creativa2.git")

#Instalamos pip
os.system("sudo apt-get update")
os.system("sudo apt-get install -y python3-pip")

#Instalamos las dependencias
os.system("sed -i 's/chardet==3.0.4/chardet/g' practica_creativa2/bookinfo/src/productpage/requirements.txt")
os.system("sed -i 's/gevent==1.4.0/gevent/g' practica_creativa2/bookinfo/src/productpage/requirements.txt")
os.system("sed -i 's/greenlet==0.4.15/greenlet/g' practica_creativa2/bookinfo/src/productpage/requirements.txt")
os.system("sed -i 's/urllib3==1.26.5/urllib3/g' practica_creativa2/bookinfo/src/productpage/requirements.txt")

os.system("sudo pip3 install -r practica_creativa2/bookinfo/src/productpage/requirements.txt")

#Creamos una variable de entorno con el número de grupo
os.environ["GROUP_NUMBER"] = "48"

#Cambiamos le título de la pagina para que muestre el número de grupo
group_number = os.environ.get("GROUP_NUMBER")

fin = open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "r")
fout = open("productpage.html", "w")
for line in fin: 
  if "Simple Bookstore App" in line:
    fout.write("{% block title %}Simple Bookstore App Grupo:" + group_number + "{% endblock %}")
  else: 
  	fout.write(line)
fin.close()
fout.close()
os.system("mv productpage.html practica_creativa2/bookinfo/src/productpage/templates/productpage.html")


#Ejecutamos la aplicación en el puerto 9080
os.system("python3 practica_creativa2/bookinfo/src/productpage/productpage_monolith.py 9080")
