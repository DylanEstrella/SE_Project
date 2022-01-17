# Modules
from time import sleep
from wiringpi import Serial
import os
import urllib.request
import RPi.GPIO as GPIO
import requests
import math
import random
import threading
import json

KEY="RHA78DSIXGIWND1V"#Poner aqui su Key de escritura
KEYREAD="1633255"#Poner aqui el IDchannel
baud = 9600
ser  = Serial("/dev/serial0",baud)
sleep(0.3)

def enviar_Thing(value_1,value_2,value_3):

   lista=[value_1,value_2,value_3]
   enviar = requests.get("https://api.thingspeak.com/update?api_key="+KEY+"&field1="+str(lista[0])+"&field2="+str(lista[1])
				   +"&field3="+str(lista[2]))  #cuando se quiere enviar dos o mas datos
   #enviar = requests.get("https://api.thingspeak.com/update?api_key=B3ZRHNV2DUMV48XB&field1="+str(lista[0]))
   if enviar.status_code == requests.codes.ok:
     if enviar.text != '0':
      print("[ INFO ]Datos enviados correctamente a ThingSpeak")
     else:
      print("[ INFO ] Tiempo de espera insuficiente (>15seg)")
   else:
     print("Error en el request: ",enviar.status_code)
	 #else:
	 #print("La cadena recibida no contiene 2 elementos, sino:",len(lista),"elementos")

def enviar_Thing2(value_1,value_2,value_3):

   lista=[value_1,value_2,value_3]
   enviar = requests.get("https://api.thingspeak.com/update?api_key="+KEY+"&field1="+str(lista[0])+"&field2="+str(lista[1])
		       +"&field3="+str(lista[2])+"&field4="+str(lista[3])+"&field5="+str(lista[4])+"&field6="+str(lista[5])+"&field7="+str(lista[6])+"&field8="+str(lista[7])) 
   #enviar = requests.get("https://api.thingspeak.com/update?api_key=B3ZRHNV2DUMV48XB&field1="+str(lista[0]))
   if enviar.status_code == requests.codes.ok:
     if enviar.text != '0':
      print("[ INFO ]Datos enviados correctamente a ThingSpeak")
     else:
      print("[ INFO ] Tiempo de espera insuficiente (>15seg)")
   else:
     print("Error en el request: ",enviar.status_code)
	 #else:
	 #print("La cadena recibida no contiene 2 elementos, sino:",len(lista),"elementos")
	 
	 
def recibir(echo = True):
 data = ""
 while True:
  input = ser.getchar()
  if echo:
   ser.putchar(input)
  if input == "\r":
   return (data)
  data += input
 sleep(0.2)
  
def printsln(menss):
 ser.puts(menss+"\r")
 sleep(0.2)

def prints(menss):
 ser.puts(menss)
 sleep(0.2)
def get_data():
      mensaje = recibir()
      vals = mensaje.split(',')
      return vals
      
def thingspeak_post():
    threading.Timer(15,thingspeak_post).start()
    val=random.randint(1,3)
    KEY= '4N20EH8EPV4HSGKE'
    URL='https://api.thingspeak.com/update?api_key='+KEY+'&field1=0'    
    HEADER='&field1={}&field2={}&field3'.format(val,val)
    NEW_URL = URl+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)

def leerArchivo (archivo,separator):
    datos = []
    f = open(archivo, "r+")
    linea1=f.readline()
    while linea1 != "":
        linea1 = linea1.strip("\n")
        datos.append(linea1.split(separator))
        linea1 = f.readline()
    f.close()
    return datos

def crearArchivo (archivo,separator,lista):
    datos = []
    f = open(archivo, "w",encoding="UTF-8")
    for i in range(len(lista)):
        f.write(separator.join(lista[i]))
        f.write("\n")
    f.close()
    return datos
 
def checkFileExistance(filePath):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False
	
def getThingSpeak():
   req=requests.get("https://api.thingspeak.com/channels/1633255/feeds.json?results=2")
   data = json.loads(req.content)
   res=data
   return res

def selCamion(peso,camiones):
 camion=camiones[0:10]
 vals=int(peso)
 mss=""
 num=0
 while(mss==""):
    if 0<vals<=5000:
     for k in range(2):
      if camion[0][k] =="0" :
       camion[0][k]="1"
       num=k
       mss="Asignado Camion de 5T"
       print(mss)
       break 
    elif 5000<vals<=7000:
     for k in range(2,4):
      if camion[0][ k ] =="0" :
       camion[0][k]="1"
       num=k
       mss="Asignado Camion de 7T"
       print(mss)
       break
    elif 7000<vals<=10000:
     for k in range(4,6):
      if camion[0][ k ] =="0" :
       camion[0][k]="1"
       num=k
       mss="Asignado Camion de 10T"
       print(mss)
       break
    elif 10000<vals<=15000:
     for k in range(6,8):
      if camion[0][ k ] =="0" :
       camion[0][ k ]="1"
       num=k
       mss="Asignado Camion de 15T"
       print(mss)
       break
    elif 15000<vals<=22000:
     for k in range(8,10):
      if camion[0][ k ] =="0" :
       camion[0][ k ]="1"
       num=k
       mss="Asignado Camion de 22T"
       print(mss)
       break
    if mss=="":
     if  0<vals<=5000:
      vals=6000
     elif  5000<vals<=7000:
      vals=8000
     elif  7000<vals<=10000:
      vals=13000
     elif  10000<vals<=15000:
      vals=21000
    #camion.append(str(num))    
 return camion
  
