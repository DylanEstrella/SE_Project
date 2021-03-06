# !/usr/bin/env python3
# Generated by Proteus Visual Designer for Raspberry Pi

from functions import *

GPIO.setmode(GPIO.BCM) #puede cambiar a BOARD
global led1
led1 = 4  #si cambiar de BCM a Board defina el n?mero del pin acorde a los pines de la raspberry
global led2
led2 = 5 #si cambiar de BCM a Board defina el n?mero del pin acorde a los pines de la raspberry

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

nombre="camiones.csv"
if(not checkFileExistance(nombre)):
    datos = [["0"] * 10 ]
    crearArchivo(nombre, ";", datos)

camiones= leerArchivo(nombre, ";")


def checkCamiones(lista):
 num=0
 for camion in lista:
  if camion==1:
   num+=1
 if num<len(lista):
  return True
 else:
  return False
  
# Main function
def main () :
# Infinite loop
 while True :
      global camiones
      global num
      print(camiones)
      vals=get_data()
      if len(vals)==2 and checkCamiones(camiones[0]):
       enviar_Thing(1,vals[ 0 ],vals[ 1 ])
       printsln("Enviado!")
       ap=selCamion(vals[1],camiones)
       crearArchivo(nombre,";",ap)

# Command line execution
if __name__ == '__main__' :
 main()