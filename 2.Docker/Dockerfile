FROM python:3.9
RUN apt-get update
RUN apt-get install -y python3-pip
ENV GROUP_NUMBER 48
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git
RUN sed -i 's/chardet==3.0.4/chardet/g' practica_creativa2/bookinfo/src/productpage/requirements.txt
RUN sed -i 's/gevent==1.4.0/gevent/g' practica_creativa2/bookinfo/src/productpage/requirements.txt
RUN sed -i 's/greenlet==0.4.15/greenlet/g' practica_creativa2/bookinfo/src/productpage/requirements.txt
RUN sed -i 's/urllib3==1.26.5/urllib3/g' practica_creativa2/bookinfo/src/productpage/requirements.txt
RUN pip3 install -r practica_creativa2/bookinfo/src/productpage/requirements.txt
COPY cambiaTitulo.py cambiaTitulo.py
RUN python3 cambiaTitulo.py
EXPOSE 9080
CMD python3 practica_creativa2/bookinfo/src/productpage/productpage_monolith.py 9080

