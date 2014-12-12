#coding:utf-8
#coding:cp1252
import time
import os
import random
#********************************************************************
#********* IMPRESIONES DE TABLERO UNO CON Y SIN VISTA DE BARCOS******

def oculto1():
	print""

def musica():
	try:
		import pygame
		pygame.init()
		pygame.display.set_mode((1,1))
		pygame.mixer.music.load("musica.mp3")
		pygame.mixer.music.play()
	except ImportError:
		"No se Encontro Libreria"
def disparo():
	try:
		import pygame
		pygame.init()
		pygame.display.set_mode((1,1))
		pygame.mixer.music.load("disparo.mp3")
		pygame.mixer.music.play()
	except ImportError:
		"No se Encontro Libreria"


def print_tablero_jugador1():
    print u"\t\t\t\t\t      ******   OCEANO JUGADOR UNO   ******"
    print u"\t\t\t\t\t\t",
    for x in range(10):
    	print str(x+1)+" |",
    print u"\n"    
    indice=1
    for fila in tablero1:
        print u"\t\t\t\t\t"+str(indice)+"|\t",
        print u" | ".join(fila)
        indice=indice+1
def print_tablero_nuevo_jugador1():
    print u"\t\t\t\t\t ******   OCEANO JUGADOR UNO   ******"
    print u"\t\t\t\t\t",
    for x in range(10):
    	print str(x+1)+" |",
    print u"\n"    
    indice=1
    for fila in tablero1:
        print u"\t\t\t\t"+str(indice)+"|\t",
        print u" | ".join(fila)
        indice=indice+1    
                
def print_tablero_jugador1_sin_vista():

    print u"\t\t\t\t\t      ******   OCEANO JUGADOR UNO   ******"
    print u"\t\t\t\t\t\t",
    for x in range(10):
    	print str(x+1)+" |",
    print u"\n"    
    indice=1
    for fila in tablero1_sin_vista:
        print u"\t\t\t\t\t"+str(indice)+"|\t",
        print u" | ".join(fila)
        indice=indice+1
def print_tablero_jugador1_sin_vista2():
		
	
    print u"\t\t\t\t\t      ******   OCEANO JUGADOR UNO   ******"
    print u"\t\t\t\t\t\t",
    for x in range(10):
    	print str(x+1)+" |",
    print u"\n"    
    indice=1
    for fila in tablero1_sin_vista:
        print u"\t\t\t\t\t"+str(indice)+"|\t",
        print u" | ".join(fila)
        indice=indice+1
#*****************************************************************************
#********* IMPRESIONES DE TABLERO DOS CON Y SIN VISTA DE BARCOS***************
def print_tablero_jugador2():
    print u"\t\t\t\t\t      ******   OCEANO JUGADOR DOS   ******"
    print u"\t\t\t\t\t\t",
    for x in range(10):
    	print str(x+1)+" |",
    print u"\n"    
    indice=1
    for fila in tablero2:
        print u"\t\t\t\t\t"+str(indice)+"|\t",
        print u" | ".join(fila)
        indice=indice+1
def print_tablero_jugador2_sin_vista():
    print u"\t\t\t\t\t      ******   OCEANO JUGADOR DOS   ******"
    print u"\t\t\t\t\t\t",
    for x in range(10):
    	print str(x+1)+" |",
    print u"\n"    
    indice=1
    for fila in tablero2_sin_vista:
        print u"\t\t\t\t\t"+str(indice)+"|\t",
        print u" | ".join(fila)
        indice=indice+1
def print_tablero_jugador2_sin_vista2():
    print u"\t\t\t\t\t      ******   OCEANO JUGADOR DOS   ******"
    print u"\t\t\t\t\t\t",
    for x in range(10):
    	print str(x+1)+" |",
    print u"\n"    
    indice=1
    for fila in tablero2_sin_vista:
        print u"\t\t\t\t\t"+str(indice)+"|\t",
        print u" | ".join(fila)
        indice=indice+1
    
#*******************************************************************************
#********* IMPRESIONES DE TABLERO PC CON Y SIN VISTA DE BARCOS******************
def print_tablero_jugadorpc():

    print u"\t\t\t\t\t            ******   OCEANO PC   ******"
    print u"\t\t\t\t\t\t",
    for x in range(10):
    	print str(x+1)+" |",
    print u"\n"    
    indice=1
    for fila in tableropc:
        print u"\t\t\t\t\t"+str(indice)+"|\t",
        print u" | ".join(fila)
        indice=indice+1
def print_tablero_jugadorpc_sin_vista():

    print u"\t\t\t\t\t            ******   OCEANO PC   ******"
    print u"\t\t\t\t\t\t",
    for x in range(10):
    	print str(x+1)+" |",
    print u"\n"    
    indice=1
    for fila in tableropc_sin_vista:
        print u"\t\t\t\t\t"+str(indice)+"|\t",
        print u" | ".join(fila)
        indice=indice+1
def print_tablero_jugadorpc_sin_vista2():
    
    print u""
    print u"\t\t\t\t\t            ******   OCEANO PC   ******"
    print u"\t\t\t\t\t\t",
    for x in range(10):
    	print str(x+1)+" |",
    print u"\n"    
    indice=1
    for fila in tableropc_sin_vista:
        print u"\t\t\t\t\t"+str(indice)+"|\t",
        print u" | ".join(fila)
        indice=indice+1
#*********************************************************************************    	            
#**************PRIMER BARCO ******************************************************
#******HUBICACIONES ALEATORIAS ***************************************************
def jugador_uno():
	fila1=random.randint(0,9)
	columna1=random.randint(0,9)
	#*** hubicacion aleatoria del segundo barco ***
	fila2=random.randint(0,8)
	columna2=random.randint(0,8)
	#*** hubicacion aleatoria del tercer barco ***
	fila3=random.randint(0,7)
	columna3=random.randint(0,7)
	#*** hubicacion aleatoria del cuarto barco ***
	fila4=random.randint(0,6)
	columna4=random.randint(0,6)	

#********** VALIDACION HUBICACION *************************************************
#******* HUBICACION BARCO NIVEL 1 *************************************************
	tablero1[fila1][columna1]=u"O"
	tablero1_sin_vista[fila1][columna1]
#************************************************************************************	
#****** HUBICACION Y ORIENTACION BARCO NIVEL 2*************************************
	orientacion_barco2=random.randint(0,1)
	if orientacion_barco2==1:
		barco2=True
		while barco2==True:
			if tablero1[fila2][columna2]==u"-" and tablero1[fila2+1][columna2]==u"-":                                
				tablero1[fila2][columna2]=u"O"
				tablero1[fila2+1][columna2]=u"O"
#***************************TABLERO CON BARCOS OCULTOS*******************************
				tablero1_sin_vista[fila2][columna2]
				tablero1_sin_vista[fila2+1][columna2]
				break
			elif tablero1[fila2][columna2]==u"O" or tablero1[fila2+1][columna2]==u"O":
				fila2=random.randint(0,8)
				columna2=random.randint(0,8)
				barco2==True
	elif orientacion_barco2==0:
		barco2=True
		while barco2==True:
			if tablero1[fila2][columna2]==u"-" and tablero1[fila2][columna2+1]==u"-":                                
				tablero1[fila2][columna2]=u"O"
				tablero1[fila2][columna2+1]=u"O"
#***************TABLERO CON BARCOS OCULTOS*****************************************
				tablero1_sin_vista[fila2][columna2]
				tablero1_sin_vista[fila2][columna2+1]
				break
			elif tablero1[fila2][columna2]==u"O" or tablero1[fila2][columna2+1]==u"O":
				fila2=random.randint(0,8)
				columna2=random.randint(0,8)
				barco2==True
#************************************************************************************				
#******* HUBICACION Y ORIENTACION BARCO NIVEL 3*****************************************
	orientacion_barco3=random.randint(0,1)
	if orientacion_barco3==1:
		barco3=True		
		while barco3==True:
			if tablero1[fila3][columna3]==u"-" and tablero1[fila3+1][columna3]==u"-" and tablero1[fila3+2][columna3]==u"-" :                                                                                                             
				tablero1[fila3][columna3]=u"O"
				tablero1[fila3+1][columna3]=u"O"
				tablero1[fila3+2][columna3]=u"O"
#***************TABLERO CON BARCOS OCULTOS*****************************************************
				tablero1_sin_vista[fila3][columna3]
				tablero1_sin_vista[fila3+1][columna3]
				tablero1_sin_vista[fila3+2][columna3]


				break
			elif tablero1[fila3][columna3]==u"O" or tablero1[fila3+1][columna3]==u"O" or tablero1[fila3+2][columna3]==u"O":
				fila3=random.randint(0,7)
				columna3=random.randint(0,7)
				barco3==True
	elif orientacion_barco3==0:
		barco3=True		
		while barco3==True:
			if tablero1[fila3][columna3]==u"-" and tablero1[fila3][columna3+1]==u"-" and tablero1[fila3][columna3+2]==u"-" :                                                                                                             
				tablero1[fila3][columna3]=u"O"
				tablero1[fila3][columna3+1]=u"O"
				tablero1[fila3][columna3+2]=u"O"
#***************TABLERO CON BARCOS OCULTOS*****************************************************
				tablero1_sin_vista[fila3][columna3]
				tablero1_sin_vista[fila3][columna3+1]
				tablero1_sin_vista[fila3][columna3+2]

				break
			elif tablero1[fila3][columna3]==u"O" or tablero1[fila3][columna3+1]==u"O" or tablero1[fila3][columna3+2]==u"O":
				fila3=random.randint(0,7)
				columna3=random.randint(0,7)
				barco3==True
#************************************************************************************************				
#********************************* HUBICACION Y ORIENTACION BARCO NIVEL 4 **********************************************************
	orientacion_barco4=random.randint(0,1)
	if orientacion_barco4==1:
		barco4=True		
		while barco4==True:
			if tablero1[fila4][columna4]==u"-" and tablero1[fila4][columna4+1]==u"-" and tablero1[fila4][columna4+2]==u"-" and tablero1[fila4][columna4+3]==u"-":                                                                                                             
				tablero1[fila4][columna4]=u"O"
				tablero1[fila4][columna4+1]=u"O"
				tablero1[fila4][columna4+2]=u"O"
				tablero1[fila4][columna4+3]=u"O"
#***************TABLERO CON BARCOS OCULTOS*****************************************************
				tablero1_sin_vista[fila4][columna4]
				tablero1_sin_vista[fila4][columna4+1]
				tablero1_sin_vista[fila4][columna4+2]
				tablero1_sin_vista[fila4][columna4+3]
				break
			elif tablero1[fila4][columna4]==u"O" or tablero1[fila4][columna4+1]==u"O" or tablero1[fila4][columna4+2]==u"O" or tablero1[fila4][columna4+3]==u"O":
				fila4=random.randint(0,6)
				columna4=random.randint(0,6)
				barco4==True	
	elif orientacion_barco4==0:
		barco4=True		
		while barco4==True:
			if tablero1[fila4][columna4]==u"-" and tablero1[fila4+1][columna4]==u"-" and tablero1[fila4+2][columna4]==u"-" and tablero1[fila4+3][columna4]==u"-":                                                                                                             
				tablero1[fila4][columna4]=u"O"
				tablero1[fila4+1][columna4]=u"O"
				tablero1[fila4+2][columna4]=u"O"
				tablero1[fila4+3][columna4]=u"O"
#***************************TABLERO CON BARCOS OCULTOS*****************************************************************
				tablero1_sin_vista[fila4][columna4]
				tablero1_sin_vista[fila4+1][columna4]
				tablero1_sin_vista[fila4+2][columna4]
				tablero1_sin_vista[fila4+3][columna4]
				break
			elif tablero1[fila4][columna4]==u"O" or tablero1[fila4+1][columna4]==u"O" or tablero1[fila4+2][columna4]==u"O" or tablero1[fila4+3][columna4]==u"O":
				fila4=random.randint(0,6)
				columna4=random.randint(0,6)
				barco4==True	
#************************************************************************************************************************************				
#****************************HUBICACION DE BARCOS JUGADOR DOS***********************************************************************************
def jugador_dos():
	fila1=random.randint(0,9)
	columna1=random.randint(0,9)
	#*** hubicacion aleatoria del segundo barco ***
	fila2=random.randint(0,8)
	columna2=random.randint(0,8)
	#*** hubicacion aleatoria del tercer barco ***
	fila3=random.randint(0,7)
	columna3=random.randint(0,7)
	#*** hubicacion aleatoria del cuarto barco ***
	fila4=random.randint(0,6)
	columna4=random.randint(0,6)	
#********************** VALIDACION HUBICACION *************************************
#******************* HUBICACION BARCO NIVEL 1 *************************************
	tablero2[fila1][columna1]=u"O"
	tablero2_sin_vista[fila1][columna1]
#************************************************************************************	
#****** HUBICACION Y ORIENTACION BARCO NIVEL 2*************************************
	orientacion_barco2=random.randint(0,1)
	if orientacion_barco2==1:
		barco2=True
		while barco2==True:
			if tablero2[fila2][columna2]==u"-" and tablero2[fila2+1][columna2]==u"-":                                
				tablero2[fila2][columna2]=u"O"
				tablero2[fila2+1][columna2]=u"O"
#***************TABLERO CON BARCOS OCULTOS*****************************************************
				tablero2_sin_vista[fila2][columna2]
				tablero2_sin_vista[fila2+1][columna2]
				break
			elif tablero2[fila2][columna2]==u"O" or tablero2[fila2+1][columna2]==u"O":
				fila2=random.randint(0,8)
				columna2=random.randint(0,8)
				barco2==True
	elif orientacion_barco2==0:
		barco2=True
		while barco2==True:
			if tablero2[fila2][columna2]==u"-" and tablero2[fila2][columna2+1]==u"-":                                
				tablero2[fila2][columna2]=u"O"
				tablero2[fila2][columna2+1]=u"O"

#***************************TABLERO CON BARCOS OCULTOS*****************************
				tablero2_sin_vista[fila2][columna2]
				tablero2_sin_vista[fila2][columna2+1]
				break
			elif tablero2[fila2][columna2]==u"O" or tablero2[fila2][columna2+1]==u"O":
				fila2=random.randint(0,8)
				columna2=random.randint(0,8)
				barco2==True
#************************************************************************************				
#******* HUBICACION Y ORIENTACION BARCO NIVEL 3*****************************************
	orientacion_barco3=random.randint(0,1)
	if orientacion_barco3==1:
		barco3=True		
		while barco3==True:
			if tablero2[fila3][columna3]==u"-" and tablero2[fila3+1][columna3]==u"-" and tablero2	[fila3+2][columna3]==u"-" :                                                                                                             
				tablero2[fila3][columna3]=u"O"
				tablero2[fila3+1][columna3]=u"O"
				tablero2[fila3+2][columna3]=u"O"

#***************TABLERO CON BARCOS OCULTOS*****************************************************
				tablero2_sin_vista[fila3][columna3]
				tablero2_sin_vista[fila3+1][columna3]
				tablero2_sin_vista[fila3+2][columna3]


				break
			elif tablero2[fila3][columna3]==u"O" or tablero2[fila3+1][columna3]==u"O" or tablero2[fila3+2][columna3]==u"O":
				fila3=random.randint(0,7)
				columna3=random.randint(0,7)
				barco3==True
	elif orientacion_barco3==0:
		barco3=True		
		while barco3==True:
			if tablero2[fila3][columna3]==u"-" and tablero2[fila3][columna3+1]==u"-" and tablero2[fila3][columna3+2]==u"-" :                                                                                                             
				tablero2[fila3][columna3]=u"O"
				tablero2[fila3][columna3+1]=u"O"
				tablero2[fila3][columna3+2]=u"O"

#***************************TABLERO CON BARCOS OCULTOS*****************************************
				tablero2_sin_vista[fila3][columna3]
				tablero2_sin_vista[fila3][columna3+1]
				tablero2_sin_vista[fila3][columna3+2]

				break
			elif tablero2[fila3][columna3]==u"O" or tablero2[fila3][columna3+1]==u"O" or tablero2[fila3][columna3+2]==u"O":
				fila3=random.randint(0,7)
				columna3=random.randint(0,7)
				barco3==True
#************************************************************************************************************				
#********************************* HUBICACION Y ORIENTACION BARCO NIVEL 4 **********************************************************
	orientacion_barco4=random.randint(0,1)
	if orientacion_barco4==1:
		barco4=True		
		while barco4==True:
			if tablero2[fila4][columna4]==u"-" and tablero2[fila4][columna4+1]==u"-" and tablero2[fila4][columna4+2]==u"-" and tablero2[fila4][columna4+3]==u"-":                                                                                                             
				tablero2[fila4][columna4]=u"O"
				tablero2[fila4][columna4+1]=u"O"
				tablero2[fila4][columna4+2]=u"O"
				tablero2[fila4][columna4+3]=u"O"

#***************TABLERO CON BARCOS OCULTOS*****************************************************
				tablero2_sin_vista[fila4][columna4]
				tablero2_sin_vista[fila4][columna4+1]
				tablero2_sin_vista[fila4][columna4+2]
				tablero2_sin_vista[fila4][columna4+3]
				break
			elif tablero2[fila4][columna4]==u"O" or tablero2[fila4][columna4+1]==u"O" or tablero2[fila4][columna4+2]==u"O" or tablero2[fila4][columna4+3]==u"O":
				fila4=random.randint(0,6)
				columna4=random.randint(0,6)
				barco4==True	
	elif orientacion_barco4==0:
		barco4=True		
		while barco4==True:
			if tablero2[fila4][columna4]==u"-" and tablero2[fila4+1][columna4]==u"-" and tablero2[fila4+2][columna4]==u"-" and tablero2[fila4+3][columna4]==u"-":                                                                                                             
				tablero2[fila4][columna4]=u"O"
				tablero2[fila4+1][columna4]=u"O"
				tablero2[fila4+2][columna4]=u"O"
				tablero2[fila4+3][columna4]=u"O"

#***************************TABLERO CON BARCOS OCULTOS*****************************************************
				tablero2_sin_vista[fila4][columna4]
				tablero2_sin_vista[fila4+1][columna4]
				tablero2_sin_vista[fila4+2][columna4]
				tablero2_sin_vista[fila4+3][columna4]
				break
			elif tablero2[fila4][columna4]==u"O" or tablero2[fila4+1][columna4]==u"O" or tablero2[fila4+2][columna4]==u"O" or tablero2[fila4+3][columna4]==u"O":
				fila4=random.randint(0,6)
				columna4=random.randint(0,6)
				barco4==True	
#*********************************************************************************************************************************
#*************************HUBICACION DE BARCOS PC********************************************************************************
def jugador_pc():
	fila1=random.randint(0,9)
	columna1=random.randint(0,9)
	#*** hubicacion aleatoria del segundo barco ***
	fila2=random.randint(0,8)
	columna2=random.randint(0,8)
	#*** hubicacion aleatoria del tercer barco ***
	fila3=random.randint(0,7)
	columna3=random.randint(0,7)
	#*** hubicacion aleatoria del cuarto barco ***
	fila4=random.randint(0,6)
	columna4=random.randint(0,6)	
#********** VALIDACION HUBICACION *************************************************************
#******* HUBICACION BARCO NIVEL 1 *************************************************************
	tableropc[fila1][columna1]=u"O"
	tableropc_sin_vista[fila1][columna1]
#************************************************************************************************	
#****** HUBICACION Y ORIENTACION BARCO NIVEL 2*************************************************
	orientacion_barco2=random.randint(0,1)
	if orientacion_barco2==1:
		barco2=True
		while barco2==True:
			if tableropc[fila2][columna2]==u"-" and tableropc[fila2+1][columna2]==u"-":                                
				tableropc[fila2][columna2]=u"O"
				tableropc[fila2+1][columna2]=u"O"

#***************************TABLERO CON BARCOS OCULTOS*****************************************
				tableropc_sin_vista[fila2][columna2]
				tableropc_sin_vista[fila2+1][columna2]
				break
			elif tableropc[fila2][columna2]==u"O" or tableropc[fila2+1][columna2]==u"O":
				fila2=random.randint(0,8)
				columna2=random.randint(0,8)
				barco2==True
	elif orientacion_barco2==0:
		barco2=True
		while barco2==True:
			if tableropc[fila2][columna2]==u"-" and tableropc[fila2][columna2+1]==u"-":                                
				tableropc[fila2][columna2]=u"O"
				tableropc[fila2][columna2+1]=u"O"

#***************************TABLERO CON BARCOS OCULTOS*****************************************
				tableropc_sin_vista[fila2][columna2]
				tableropc_sin_vista[fila2][columna2+1]
				break
			elif tableropc[fila2][columna2]==u"O" or tableropc[fila2][columna2+1]==u"O":
				fila2=random.randint(0,8)
				columna2=random.randint(0,8)
				barco2==True
#************************************************************************************************				
#******* HUBICACION Y ORIENTACION BARCO NIVEL 3*****************************************************
	orientacion_barco3=random.randint(0,1)
	if orientacion_barco3==1:
		barco3=True		
		while barco3==True:
			if tableropc[fila3][columna3]==u"-" and tableropc[fila3+1][columna3]==u"-" and tableropc[fila3+2][columna3]==u"-" :                                                                                                             
				tableropc[fila3][columna3]=u"O"
				tableropc[fila3+1][columna3]=u"O"
				tableropc[fila3+2][columna3]=u"O"

#***************************TABLERO CON BARCOS OCULTOS*****************************************************
				tableropc_sin_vista[fila3][columna3]
				tableropc_sin_vista[fila3+1][columna3]
				tableropc_sin_vista[fila3+2][columna3]


				break
			elif tableropc[fila3][columna3]==u"O" or tableropc[fila3+1][columna3]==u"O" or tableropc[fila3+2][columna3]==u"O":
				fila3=random.randint(0,7)
				columna3=random.randint(0,7)
				barco3==True
	elif orientacion_barco3==0:
		barco3=True		
		while barco3==True:
			if tableropc[fila3][columna3]==u"-" and tableropc[fila3][columna3+1]==u"-" and tableropc[fila3][columna3+2]==u"-" :                                                                                                             
				tableropc[fila3][columna3]=u"O"
				tableropc[fila3][columna3+1]=u"O"
				tableropc[fila3][columna3+2]=u"O"

#***************************TABLERO CON BARCOS OCULTOS*****************************************
				tableropc_sin_vista[fila3][columna3]
				tableropc_sin_vista[fila3][columna3+1]
				tableropc_sin_vista[fila3][columna3+2]

				break
			elif tableropc[fila3][columna3]==u"O" or tableropc[fila3][columna3+1]==u"O" or tableropc[fila3][columna3+2]==u"O":
				fila3=random.randint(0,7)
				columna3=random.randint(0,7)
				barco3==True
#************************************************************************************************************				
#********************************* HUBICACION Y ORIENTACION BARCO NIVEL 4 **********************************************************
	orientacion_barco4=random.randint(0,1)
	if orientacion_barco4==1:
		barco4=True		
		while barco4==True:
			if tableropc[fila4][columna4]==u"-" and tableropc[fila4][columna4+1]==u"-" and tableropc[fila4][columna4+2]==u"-" and tableropc[fila4][columna4+3]==u"-":                                                                                                             
				tableropc[fila4][columna4]=u"O"
				tableropc[fila4][columna4+1]=u"O"
				tableropc[fila4][columna4+2]=u"O"
				tableropc[fila4][columna4+3]=u"O"

#***************************TABLERO CON BARCOS OCULTOS*****************************************
				tableropc_sin_vista[fila4][columna4]
				tableropc_sin_vista[fila4][columna4+1]
				tableropc_sin_vista[fila4][columna4+2]
				tableropc_sin_vista[fila4][columna4+3]
				break
			elif tableropc[fila4][columna4]==u"O" or tableropc[fila4][columna4+1]==u"O" or tableropc[fila4][columna4+2]==u"O" or tableropc[fila4][columna4+3]==u"O":
				fila4=random.randint(0,6)
				columna4=random.randint(0,6)
				barco4==True	
	elif orientacion_barco4==0:
		barco4=True		
		while barco4==True:
			if tableropc[fila4][columna4]==u"-" and tableropc[fila4+1][columna4]==u"-" and tableropc[fila4+2][columna4]==u"-" and tableropc[fila4+3][columna4]==u"-":                                                                                                             
				tableropc[fila4][columna4]=u"O"
				tableropc[fila4+1][columna4]=u"O"
				tableropc[fila4+2][columna4]=u"O"
				tableropc[fila4+3][columna4]=u"O"

#***************************TABLERO CON BARCOS OCULTOS*****************************************
				tableropc_sin_vista[fila4][columna4]
				tableropc_sin_vista[fila4+1][columna4]
				tableropc_sin_vista[fila4+2][columna4]
				tableropc_sin_vista[fila4+3][columna4]
				break
			elif tableropc[fila4][columna4]==u"O" or tableropc[fila4+1][columna4]==u"O" or tableropc[fila4+2][columna4]==u"O" or tableropc[fila4+3][columna4]==u"O":
				fila4=random.randint(0,6)
				columna4=random.randint(0,6)
				barco4==True	
#**********************************************************************************************************************
#************************************* FUNCION LIMPIAR ****************************************************************
def limpiar():
	for x in tablero1:
		del tablero1[x]
	for x in tablero1_sin_vista:
		del tablero1_sin_vista[x]

	for x in tableropc:
		del tableropc[x]
	for x in tableropc_sin_vista:
		del tableropc_sin_vista[x]
#************************************************************************************************************************
#************************ FUNCIONES NOMBRES DE JUGADORES ************************************************************************
def nombre_jugador_1():
	print u"\t\t     ██╗██╗   ██╗ ██████╗  █████╗ ██████╗  ██████╗ ██████╗     ██╗   ██╗███╗   ██╗ ██████╗ "
	print u"\t\t     ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    ██║   ██║████╗  ██║██╔═══██╗"
	print u"\t\t     ██║██║   ██║██║  ███╗███████║██║  ██║██║   ██║██████╔╝    ██║   ██║██╔██╗ ██║██║   ██║"
	print u"\t\t██   ██║██║   ██║██║   ██║██╔══██║██║  ██║██║   ██║██╔══██╗    ██║   ██║██║╚██╗██║██║   ██║"
	print u"\t\t╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██████╔╝╚██████╔╝██║  ██║    ╚██████╔╝██║ ╚████║╚██████╔╝"
	print u"\t\t ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ "
	print u""
def nombre_jugador_2():
	print u"\t\t     ██╗██╗   ██╗ ██████╗  █████╗ ██████╗  ██████╗ ██████╗     ██████╗  ██████╗ ███████╗"
	print u"\t\t     ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    ██╔══██╗██╔═══██╗██╔════╝"
	print u"\t\t     ██║██║   ██║██║  ███╗███████║██║  ██║██║   ██║██████╔╝    ██║  ██║██║   ██║███████╗"
	print u"\t\t██   ██║██║   ██║██║   ██║██╔══██║██║  ██║██║   ██║██╔══██╗    ██║  ██║██║   ██║╚════██║"
	print u"\t\t╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██████╔╝╚██████╔╝██║  ██║    ██████╔╝╚██████╔╝███████║"
	print u"\t\t ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝"
	print u""
def nombre_jugador_pc():
	print u"\t\t\t     ██╗██╗   ██ ████████╗ ██████╗██████╗  ██████╗ ██████╗     ██████   ██████ "
	print u"\t\t\t     ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    ██╔══██╗██╔════╝"
	print u"\t\t\t     ██║██║   ██║██║  ███╗███████║██║  ██║██║   ██║██████╔╝    ██████╔╝██║     "
	print u"\t\t\t██   ██║██║   ██║██║   ██║██╔══██║██║  ██║██║   ██║██╔══██╗    ██╔═══╝ ██║     "
	print u"\t\t\t╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██████╔╝╚██████╔╝██║  ██║    ██║     ╚██████╗"
	print u"\t\t\t ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═╝      ╚═════╝"
	print u""
#************************************************************************************************************************
#************************ FUNCION INICIO DE JUEGO JUGADOR UNO ************************************************************
def inicio():
	print u"\t\t\t\t\t   UN JUGADOR"
	nombre_jugador1=raw_input("\t\t\t\t\t   INGRESE EL NOMBRE DEL JUGADOR: ")
	print u"\t\t\t\t\tEXELENTE, BIENVENIDO (%s) "%(nombre_jugador1)
	print u"\t\t\t\t\tPORFAVOR ESPERE UNOS SEGUNDO MIENTRAS COLOCAMOS TU FLOTA:"
	time.sleep(1)
	os.system("cls")
	print u"\t\t███████╗██╗      ██████╗ ████████╗ █████╗      █████╗ ██╗     ██╗ █████╗ ██████╗  █████╗ "
	print u"\t\t██╔════╝██║     ██╔═══██╗╚══██╔══╝██╔══██╗    ██╔══██╗██║     ██║██╔══██╗██╔══██╗██╔══██╗"
	print u"\t\t█████╗  ██║     ██║   ██║   ██║   ███████║    ███████║██║     ██║███████║██║  ██║███████║"
	print u"\t\t██╔══╝  ██║     ██║   ██║   ██║   ██╔══██║    ██╔══██║██║     ██║██╔══██║██║  ██║██╔══██║"
	print u"\t\t██║     ███████╗╚██████╔╝   ██║   ██║  ██║    ██║  ██║███████╗██║██║  ██║██████╔╝██║  ██║"
	print u"\t\t╚═╝     ╚══════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═"
	print u"""   				                     ___#_#___|__
	\t                              _  |____________|  _
	\t                       _=====| | |            | | |==== _
	\t                 =====| |.---------------------------. | |====
	\t   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
	\t     \                                                             /
	\t      \_______________________________________________WWS_________/
	\t  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"""
	print u"\t\tAQUI SE ENCUENTRA TU FLOTA ALIADA, TU TIENES COMO ALIADOS 4 TIPOS DE BARCOS "
	print u"\t\tPORTA AVIONES (nivel 4):  Es un buque de guerra capaz de transportar aviones,  "
	print u"\t\tACORAZADO     (nivel 3):  Buque de guerra de gran tonelaje, fuertemente blindado y artillado. "
	print u"\t\tFRAGATA       (nivel 2):. Buque de tamaño inferior al crucero, destinado para escoltar a otras embarcaciones "
	print u"\t\tCORBETA       (nivel 1):  Embarcación destinada a la defensa y vigilancia de aguas. Dragaminas"
	print u"\t\tLOS BARCOS SE ENCUENTRAN ESCONDIDOS EL OCEANO"
	print u""
	print u"\t\t\t\tTU FLOTA SE HA COLOCADO DE LA SIGUIENTE MANERA: "
	print u"\t\t\t\tPERO NO TE PREOCUPES EL ENEMIGO NO PODRA VER TUS POSICIONES...!!"
	print u""
	print_tablero_nuevo_jugador1()
	print u""
#************************************************************************************************************************************
#*****************************************************************************************************************************************************
#**************************** SINGLE PLAYER *****************************************************************************************
class un_jugador(object):
	def single_player(self):
		inicio()
		self.pausa2=raw_input(u"\t\t\t\tAHORA ESTAMOS LISTOS PARA LA BATALLA, VAMOS POR ELLOS: ")
		os.system("cls")
#*******************************************************************************************************************************
#************************************** TURNOS JUGADOR UNO *********************************************************************
		total_pc=0
		vidas=2

		total_jugador1=0
		while vidas>0:
			disparo_repetido=True
			while disparo_repetido==True:
				nombre_jugador_1()
				print_tablero_jugador1()
				
				print u""
				print_tablero_jugadorpc_sin_vista2()
				print u""
#************************ DISPARO DE FILA JUGADOR UNO ************************************************************				
				validar_disparo_jugador1_fila=True
				while validar_disparo_jugador1_fila==True:
					try:
						self.disparo_jugador1_fila=int(raw_input(u"    \t\t\t\t\t\tingrese fila: "))
						if self.disparo_jugador1_fila>10 or self.disparo_jugador1_fila<1:
							print "\t\t\t\t\t\tEsto esta fuera del oceano"
							print "\t\t\t\t\t\tSeria mejor si lo vuelves a intentar"
							self.pase6=raw_input("")
							os.system("cls")
							nombre_jugador_1()
							print_tablero_jugador1()
							print u""
							print_tablero_jugadorpc_sin_vista2()
						
						else:
							self.disparo_jugador1_fila=self.disparo_jugador1_fila
							break	
					except:
						print "\t\t\t\t\t\tAs ingresado letras"		
						print "\t\t\t\t\t\tSeria mejor si lo vuelves a intentar"
						self.pause5=raw_input("")
						os.system("cls")
						nombre_jugador_1()
						print_tablero_jugador1()
						print u""
						print_tablero_jugadorpc_sin_vista2()
#*************************DISPARO COLUMNA JUGADOR UNO ************************************************************
				
				validar_disparo_jugador1_columna=True
				while validar_disparo_jugador1_columna==True:
					try:
						self.disparo_jugador1_columna=int(raw_input(u"    \t\t\t\t\t\tingrese columna: "))
						if self.disparo_jugador1_columna>10 or self.disparo_jugador1_columna<1:
							print "\t\t\t\t\t\tEsto esta fuera del oceano"
							print "\t\t\t\t\t\tSeria mejor si lo vuelves a intentar"
							pase6=raw_input("")
							os.system("cls")
							nombre_jugador_1()
							print_tablero_jugador1()
							print u""
							print_tablero_jugadorpc_sin_vista2()
							print u"    \t\t\t\t\t\tIngrese fila: %s"%(self.disparo_jugador1_fila)
						else:
							self.disparo_jugador1_columna=self.disparo_jugador1_columna
							break	
					except:
						print ""
						print "\t\t\t\t\t\tAs ingresado letras"		
						print "\t\t\t\t\t\tSeria mejor si lo vuelves a intentar"
						pause5=raw_input("")
						os.system("cls")
						nombre_jugador_1()
						print_tablero_jugador1()
						print u""
						print_tablero_jugadorpc_sin_vista2()
						print u"    \t\t\t\t\t\tIngrese fila: %s"%(self.disparo_jugador1_fila)
#*********************************************************************************************************
#****************************VALIDACION DISPARO REPETIDO JUGADOR UNO*****************************************
				validar_disparo=tableropc[self.disparo_jugador1_fila-1][self.disparo_jugador1_columna-1]
				if validar_disparo==u"#" or validar_disparo==u"*":
					print u"    \t\t\t\t\t\tVAYA CAPITAN YA HEMOS DISPARADO EN ESTA POSICION"
					print u"    \t\t\t\t\t\tSeria mejor si lo vuelve a intentar"
					pausa7=raw_input("")
					os.system("cls")
					disparo_repetido=True
				else:
					disparo_repetido=False
#*********************************************************************************************
#********************************DISPARO ACERTADO JUGADOR UNO******************************************
			validar=tableropc[self.disparo_jugador1_fila-1][self.disparo_jugador1_columna-1]
			if validar==u"O":
				tableropc_sin_vista[self.disparo_jugador1_fila-1][self.disparo_jugador1_columna-1]=u"#"
				tableropc[self.disparo_jugador1_fila-1][self.disparo_jugador1_columna-1]=u"#"
				print u"    \t\t\t\t\t\tEXELENTE CAPITAN... Hemos impactado el barco enemigo...!!"
			  	print u""
			  	total_jugador1=total_jugador1+1
#************************ DISPARO FALLIDO JUGADOR UNO ************************************************			
			else:
			   	print u"    \t\t\t\t\t\tVAYA.. estuvimos bastante cerca pero no hemos logrado impactar..!!"
			   	tableropc_sin_vista[self.disparo_jugador1_fila-1][self.disparo_jugador1_columna-1]=u"*"
				tableropc[self.disparo_jugador1_fila-1][self.disparo_jugador1_columna-1]=u"*"
				
			   	
			vidas=vidas-1
			print u"\t\t\tt***************************** VIDAS RESTANTES %s *******************************"%(vidas)
			pausa4=raw_input(u"")
			os.system("cls")
			
#************************************************************************************************************************************
#******************************************************************************************************************************
#************************************ TURNOS PC ******************************************************************************
			nombre_jugador_pc()
			print_tablero_jugadorpc()
			print ""
			print_tablero_jugador1_sin_vista2()
			fila_pc=random.randint(0,9)
			columna_pc=random.randint(0,9)
			print u""
			print u"    \t\t\t\t\t\tEl jugador pc esta disparando"
			time.sleep(2)
			print "    \t\t\t\t\t\tEl jugador pc ha disparado en la posicion ( %s : %s )"%(fila_pc, columna_pc)
#************************ DISPARO ACERTADO JUGADOR PC ************************************************************
			validar=tablero1[fila_pc][columna_pc]
			if validar ==u"O":
				tablero1[fila_pc-1][columna_pc-1]=u"#"
				tablero1_sin_vista[fila_pc-1][columna_pc-1]=u"#"
				print "    \t\t\t\t\t\tEXELENTE CAPITAN... Hemos impactado el barco enemigo...!! le diste"
				total_pc=total_pc+1
#************************ DISPARO FALLIDO JUGADOR PC ************************************************************
			else:
				tablero1[fila_pc-1][columna_pc-1]=u"*" 
				tablero1_sin_vista[fila_pc-1][columna_pc-1]=u"*" 
				print "    \t\t\t\t\t\tVAYA.. estuvimos bastante cerca pero no hemos logrado impactar..!!"

			print u"\t\t\tt***************************** VIDAS RESTANTES %s *******************************"%(vidas)
			
			pausa4=raw_input(u"")
			os.system("cls")
#************************************************************************************************************************
#************************ RESULTADOS SINGLE PLAYER ************************************************************
#************************ GANADOR JUGADOR UNO ************************************************************************
			
		if total_jugador1>total_pc:
			ganador_jugador_1()
#************************ GANADOR JUGADOR PC ************************************************************************************

		elif total_jugador1<total_pc:
			perdedor()
#************************ EMPATE ************************************************************************************
			
		elif total_jugador1==total_pc:
			print u"""
	██╗  ██╗ █████╗     ███████╗██╗██████╗  ██████╗     ██╗   ██╗███╗   ██╗    ███████╗███╗   ███╗██████╗  █████╗ ████████╗███████╗
	██║  ██║██╔══██╗    ██╔════╝██║██╔══██╗██╔═══██╗    ██║   ██║████╗  ██║    ██╔════╝████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
	███████║███████║    ███████╗██║██║  ██║██║   ██║    ██║   ██║██╔██╗ ██║    █████╗  ██╔████╔██║██████╔╝███████║   ██║   █████╗  
	██╔══██║██╔══██║    ╚════██║██║██║  ██║██║   ██║    ██║   ██║██║╚██╗██║    ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██╔══██║   ██║   ██╔══╝  
	██║  ██║██║  ██║    ███████║██║██████╔╝╚██████╔╝    ╚██████╔╝██║ ╚████║    ███████╗██║ ╚═╝ ██║██║     ██║  ██║   ██║   ███████╗
	╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝╚═╝╚═════╝  ╚═════╝      ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚══════╝"""
			 	
			print_tablero_jugador1_sin_vista2()
			print u""
			print_tablero_jugadorpc_sin_vista2()
			print total_jugador1
			print total_pc
			time.sleep(2)
#************************************************************************************************************************************			
#************************ FUNCION GANADOR JUGADOR UNO SINGLE PLAYER ************************************************************			
def ganador_jugador_1():
	print u""" 
			 ██████╗  █████╗ ███╗   ██╗ █████╗ ██████╗  ██████╗ ██████╗     
			██╔════╝ ██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    
			██║  ███╗███████║██╔██╗ ██║███████║██║  ██║██║   ██║██████╔╝    
			██║   ██║██╔══██║██║╚██╗██║██╔══██║██║  ██║██║   ██║██╔══██╗    
			╚██████╔╝██║  ██║██║ ╚████║██║  ██║██████╔╝╚██████╔╝██║  ██║    
			 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝"""
	nombre_jugador_1()
	print u"""
		                       .'             \__/               (  )
		                     ( )               ||          _      ||
		                     /|\               ||       .-` \     ||
		                   .' | '              ||   _.-'    |     ||
		                  /   |\ \             || .'   `.__.'     ||   _.-..
		                .'   /| `.            _.-'   _.-'       _.-.`-'`._`.`
		                \  .' |  |        .-.`    `./      _.-`.    `._.-'
		                 |.   |  `.   _.-'   `.   .'     .'  `._.`---`
		                .'    |   |  :   `._..-'.'        `._..'  ||
		               /      |   \  `-._.'    ||                 ||
		              |     .'|`.  |           ||_.--.-._         ||
		              '    /  |  \ \       __.--'\    `. :        ||
		               \  .'  |   \|   ..-'   \   `._-._.'        ||
		`.._            |/    |    `.  \  \    `._.-              ||
		    `-.._       /     |      \  `-.'_.--'                 ||
		         `-.._.'      |      |        | |         _ _ _  _'_ _ _ _ _
		              `-.._   |      \        | |        |_|_|_'|_|_|_|_|_|_|
		                  [`--^-..._.'        | |       /....../|  __   __  |
		                   \`---.._|`--.._    | |      /....../ | |__| |__| |
		                    \__  _ `-.._| `-._|_|_ _ _/_ _ _ /  | |__| |__| |
		                     \   _o_   _`-._|_|_|_|_|_|_|_|_/   '-----------/
		                      \_`.|.'  _  - .--.--.--.--.--.`--------------'
		      .```-._ ``-.._   \__   _    _ '--'--'--'--'--'  - _ - _  __/
		 .`-.```-._ ``-..__``.- `.      _     -  _  _  _ -    _-   _  __/(.``-._"""
	
	time.sleep(2)
#************************************************************************************************************************************
#************************ GANADOR JUGADOR PC SINGLE PLAYER ************************************************************************
	
def perdedor():
	print u"""
			██╗  ██╗ █████╗ ███████╗    ██████╗ ███████╗██████╗ ██████╗ ██╗██████╗  ██████╗ 
			██║  ██║██╔══██╗██╔════╝    ██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██╔══██╗██╔═══██╗
			███████║███████║███████╗    ██████╔╝█████╗  ██████╔╝██║  ██║██║██║  ██║██║   ██║
			██╔══██║██╔══██║╚════██║    ██╔═══╝ ██╔══╝  ██╔══██╗██║  ██║██║██║  ██║██║   ██║
			██║  ██║██║  ██║███████║    ██║     ███████╗██║  ██║██████╔╝██║██████╔╝╚██████╔╝
			╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝     ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═════╝  ╚═════╝ """
	print u"""
			                                                 ::
			                               .-'`""::..       ::
			                             ,'        `""::..  ::
			                           ,'               `""::..
			                          ,    __                `""::..
			                         :       `.   __              `""::..
			                        :    __,-' ,-'  : --.              `""::.
			                       :    '-._ ,' `:,' /   )                .'
			                      :             ,'  / :,' _             .'
			                      :                '  |  / `.         .'
			     :.              :                    : /   :        '
			     ::              :                     /   /       .'
			     |:             :                      `--'       :
			     ||             :       ____                     :
			     |:.            :   ..""    ""-.                :
			     ||:.           : .'            `.             :
			     || `:.          :                `.          :
			   __||  `""::..     :                 :.         :
			.-"  :| dd    `""::..`:                ::.       :
			     ::            `""::..            ::  .      :
			     `:.                `""::..       ::   :     :           __
			      `:.                    `""::.. ::_____:____:__    _.--'
			   ___.-`::..                  _.-"""""             """"----....
			      `--._`"::.           _.-'
			               `"":: ___.-'
			            ____--
			"""
	
	time.sleep(2)
#************************************************************************************************************************************************
#************************************************************************************************************************************************
#************************ INICIO FUNCION MULTIPLAYER ************************************************************************		
class dos_jugadores(object):
	def multiplayer(self):
		
		os.system("cls")
		print u"\t\t███╗   ███╗██╗   ██╗██╗  ████████╗██╗     ██╗██╗   ██╗ ██████╗  █████╗ ██████╗  ██████╗ ██████╗ "
		print u"\t\t████╗ ████║██║   ██║██║  ╚══██╔══╝██║     ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗"
		print u"\t\t██╔████╔██║██║   ██║██║     ██║   ██║     ██║██║   ██║██║  ███╗███████║██║  ██║██║   ██║██████╔╝"
		print u"\t\t██║╚██╔╝██║██║   ██║██║     ██║   ██║██   ██║██║   ██║██║   ██║██╔══██║██║  ██║██║   ██║██╔══██╗"
		print u"\t\t██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██████╔╝╚██████╔╝██║  ██║"
		print u"\t\t╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝ ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝"
		print u""
		print u"\t\t\t\t               ()"
		print u"\t\t\t\t                    ||q',,'"
		print u"\t\t\t\t                    ||d,~"
		print u"\t\t\t\t         (,---------------------,)"
		print u"\t\t\t\t          ',       q888p       ,'"
		print u"\t\t\t\t            \       986       /"
		print u"\t\t\t\t             \  8p, d8b ,q8  /"
		print u"\t\t\t\t              ) 888a888a888 ("
		print u"\t\t\t\t             /  8b` q8p `d8  \              O"
		print u"\t\t\t\t            /       689       \             |','"
		print u"\t\t\t\t           /       d888b       \      (,---------,)"
		print u"\t\t\t\t         ,'_____________________',     \   ,8,   /"
		print u"\t\t\t\t         (`__________L|_________`)      ) a888a (    _,_"
		print u"\t\t\t\t         [___________|___________]     /___`8`___\   }*{"
		print u"\t\t\t\t           }:::|:::::}::|::::::{      (,=========,)  -=-"
		print u"\t\t\t\t   Samwise  '|::::}::|:::::{:|'  .,.    \:::|:::/    ~`~="
		print u"\t\t\t\t --=~(@)~=-- '|}:::::|::{:::|'          ~""~`~"
		print u"\t\t\t\t               '|:}::|::::|'~`~"""
		print u"\t\t\t\t           ~`~""~`~"                 "~`~""~"
		print u"\t\t\t\t                          ""~`~"
		print u"\t\t-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-."
		print u"\t\t.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-."
		print u"\t\t\t.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-"
		print u"\t\t\t\t.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-"
		print u"\n\n\n"
		pausa=raw_input("")
#********************************************************************************************************
#********************************************************************************************************************
#********************************** INGRESO DE NOMBRES MULTIJUGADOR *************************************************
		os.system("cls")
		print u"\t\t███╗   ███╗██╗   ██╗██╗  ████████╗██╗     ██╗██╗   ██╗ ██████╗  █████╗ ██████╗  ██████╗ ██████╗ "
		print u"\t\t████╗ ████║██║   ██║██║  ╚══██╔══╝██║     ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗"
		print u"\t\t██╔████╔██║██║   ██║██║     ██║   ██║     ██║██║   ██║██║  ███╗███████║██║  ██║██║   ██║██████╔╝"
		print u"\t\t██║╚██╔╝██║██║   ██║██║     ██║   ██║██   ██║██║   ██║██║   ██║██╔══██║██║  ██║██║   ██║██╔══██╗"
		print u"\t\t██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██████╔╝╚██████╔╝██║  ██║"
		print u"\t\t╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝ ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝"
		print u""
		print u""
		print u"\t\t\t\t\t\tBienvenido al modo multijugador"
		multijugador1_nombre=raw_input(u"\t\t\t\t\t\tIngrese el nombre del jugador numero (.1.)?: ")
		print u"\t\t\t\t\t\tExcelente bienvenido %s "%(multijugador1_nombre)
		print u""
		multijugador2_nombre=raw_input(u"\t\t\t\t\t\tIngrese el nombre del jugador numero (.2.)?: ")
		print u"\t\t\t\t\t\tExcelente bienvenido %s"%(multijugador2_nombre)
		print u""
		vidas=input("\t\t\t\t\t\tQue numero de vidas desea tener..??: ")
		os.system("cls")
#*******************************************************************************************************************************
#************************************** TURNOS JUGADOR UNO *********************************************************************
#************************************ VIDAS ************************************************************************
		
#************************************************************************************************************************		
		total_jugador1_multiplayer=0
		total_jugador2_multiplayer=0
		while vidas>0:
			
			
			disparo_repetido=True
			while disparo_repetido==True:
				nombre_jugador_1()
				print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador1_nombre)
				print_tablero_jugador1()
				print u""
				print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador2_nombre)
				print_tablero_jugador2_sin_vista2()
				print u""
#************************ DISPARO FILA JUGADOR UNO MULTIPLAYER ************************************************		
				validar_disparo_jugador1_fila=True
				while validar_disparo_jugador1_fila==True:
					try:
						self.disparo_jugador1_fila=int(raw_input(u"    \t\t\t\t\t\tIngrese fila: "))
						if self.disparo_jugador1_fila>10 or self.disparo_jugador1_fila<1:
							print "\t\t\t\t\t\tEsto esta fuera del oceano"
							print "\t\t\t\t\t\tSeria mejor si lo vuelves a intentar"
							pase6=raw_input("")
							os.system("cls")
							nombre_jugador_1()
							print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador1_nombre)
							print_tablero_jugador1()
							print u""
							print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador2_nombre)
							print_tablero_jugador2_sin_vista2()
							print u""
						
						else:
							self.disparo_jugador1_fila=self.disparo_jugador1_fila
							break	
					except:
						print "\t\t\t\t\t\tAs ingresado letras"		
						print "\t\t\t\t\t\tSeria mejor si lo vuelves a intentar"
						self.pause5=raw_input("")
						os.system("cls")
						nombre_jugador_1()
						print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador1_nombre)
						print_tablero_jugador1()
						print u""
						print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador2_nombre)
						print_tablero_jugador2_sin_vista2()
						print u""
#************************ DISPARO COLUMNA JUGADOR UNO MULTIPLAYER ************************************************
				
				validar_disparo_jugador1_columna=True
				while validar_disparo_jugador1_columna==True:
					try:
						self.disparo_jugador1_columna=int(raw_input(u"    \t\t\t\t\t\tIngrese columna: "))
						if self.disparo_jugador1_columna>10 or self.disparo_jugador1_columna<1:
							print "\t\t\t\t\t\tEsto esta fuera del oceano"
							print "\t\t\t\t\t\tSeria mejor si lo vuelves a intentar"
							self.pase6=raw_input("")
							os.system("cls")
							nombre_jugador_1()
							print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador1_nombre)
							print_tablero_jugador1()
							print ""
							print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador2_nombre)
							print_tablero_jugador2_sin_vista2()
							print u"    \t\t\t\t\t\tIngrese fila: %s"%(self.disparo_jugador1_fila)
						else:
							self.disparo_jugador1_columna=self.disparo_jugador1_columna
							break	
					except:
						print "\t\t\t\t\t\tAs ingresado letras"		
						print "\t\t\t\t\t\tAeria mejor si lo vuelves a intentar"
						self.pause5=raw_input("")
						os.system("cls")
						nombre_jugador_1()
						print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador1_nombre)
						print_tablero_jugador1()
						print ""
						print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador2_nombre)
						print_tablero_jugador2_sin_vista2()
						print u"    \t\t\t\t\t\tIngrese fila: %s"%(self.disparo_jugador1_fila)
								
#******************************DISPARO REPETIDO JUGADOR UNO MULTIPLAYER*************************************************
				validar_disparo=tablero2[self.disparo_jugador1_fila-1][self.disparo_jugador1_columna-1]
				if validar_disparo==u"#" or validar_disparo==u"*":
					print u"    \t\t\t\t\t\tVAYA CAPITAN YA HEMOS DISPARADO EN ESTA POSICION"
					print u"    \t\t\t\t\t\tSeria mejor si lo vuelve a intentar"
					pausa7=raw_input("")
					os.system("cls")
					disparo_repetido=True
				else:
					disparo_repetido=False
#****************************DISPARO ACERTADO JUGADOR UNO MULTIPLAYER*************************************************************
			validar=tablero2[self.disparo_jugador1_fila-1][self.disparo_jugador1_columna-1]
			if validar==u"O":
				tablero2[self.disparo_jugador1_fila-1][self.disparo_jugador1_columna-1]=u"#"
				tablero2_sin_vista[self.disparo_jugador1_fila-1][self.disparo_jugador1_columna-1]=u"#"
				
				disparo()
				print u"    \t\t\t\t\t\tEXELENTE CAPITAN... Hemos impactado el barco enemigo...!!"
			  	print u""
			  
				print u"\t\t\tt***************************** VIDAS RESTANTES %s *******************************"%(vidas)
				self.pausa4=raw_input(u"")
				os.system("cls")
				musica()
			  	total_jugador1_multiplayer=total_jugador1_multiplayer+1
#************************ DISPARO FALLIDO JUGADOR UNO MULTIPLAYER			  	
			else:
			   	print u"    \t\t\t\t\t\tVAYA.. estuvimos bastante cerca pero no hemos logrado impactar..!!"
			   	tablero2[self.disparo_jugador1_fila-1][self.disparo_jugador1_columna-1]=u"*"
				tablero2_sin_vista[self.disparo_jugador1_fila-1][self.disparo_jugador1_columna-1]=u"*"
			   	print u"\t\t\tt***************************** VIDAS RESTANTES %s *******************************"%(vidas)
				self.pausa4=raw_input(u"")
				os.system("cls")


			vidas=vidas-1
			
			

#******************************************************************************************************************************
#************************************ TURNOS JUGADOR DOS ******************************************************************************
			#total_jugador2_multiplayer=0
			
			
			disparo_repetido=True
			while disparo_repetido==True:
				nombre_jugador_2()
				print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador2_nombre)
				print_tablero_jugador2()
				print u""
				print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador1_nombre)
				print_tablero_jugador1_sin_vista2()
				print u""

#************************ DISPARO FILA JUGADOR DOS MULTIPLAYER ************************************************				
				validar_disparo_jugador2_fila=True
				while validar_disparo_jugador2_fila==True:
					try:
						self.disparo_jugador2_fila=int(raw_input(u"    \t\t\t\t\t\tIngrese fila: "))
						if self.disparo_jugador2_fila>10 or self.disparo_jugador2_fila <1:
							print "\t\t\t\t\t\tEsto esta fuera del oceano"
							print "\t\t\t\t\t\tSeria mejor si lo vuelves a intentar"
							self.pase6=raw_input("")
							os.system("cls")
							nombre_jugador_2()
							print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador2_nombre)
							print_tablero_jugador2()
							print u""
							print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador1_nombre)
							print_tablero_jugador1_sin_vista2()
							print u""
						else:
							self.disparo_jugador2_fila=self.disparo_jugador2_fila
							break	
					except:
						print "\t\t\t\t\t\tAs ingresado letras"		
						print "\t\t\t\t\t\tSeria mejor si lo vuelves a intentar"
						
						self.pause5=raw_input("")
						os.system("cls")
						nombre_jugador_2()
						print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador2_nombre)
						print_tablero_jugador2()
						print u""
						print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador1_nombre)
						print_tablero_jugador1_sin_vista2()
						print u""
#****************************DISPARO COLUMNA JUGADOR DOS MULTIPLAYER***************************************
				validar_disparo_jugador2_columna=True
				while validar_disparo_jugador2_columna==True:
					try:
						self.disparo_jugador2_columna=int(raw_input(u"    \t\t\t\t\t\tIngrese columna: "))
						if self.disparo_jugador2_columna>10 or self.disparo_jugador2_columna <1:
							print "\t\t\t\t\t\tEsto esta fuera del oceano"
							print "\t\t\t\t\t\tSeria mejor si lo vuelves a intentar"
							pase6=raw_input("")
							os.system("cls")
							nombre_jugador_2()
							print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador2_nombre)
							print_tablero_jugador2()
							print u""
							print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador1_nombre)
							print_tablero_jugador1_sin_vista2()
							print u"    \t\t\t\t\t\tIngrese fila: %s"%(self.disparo_jugador2_fila)
						else:
							self.disparo_jugador2_columna=self.disparo_jugador2_columna
							break
					except:
						print "\t\t\t\t\t\tAs ingresado letras"		
						print "\t\t\t\t\t\tSeria mejor si lo vuelves a intentar"
						self.pause5=raw_input("")
						os.system("cls")
						nombre_jugador_2()
						print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador2_nombre)
						print_tablero_jugador2()
						print u""
						print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador1_nombre)
						print_tablero_jugador1_sin_vista2()
						print u"    \t\t\t\t\t\tIngrese fila: %s"%(self.disparo_jugador2_fila)
								
#******************************DISPARO REPETIDO JUGADOR DOS MULTIPLAYER**************************************************
				validar_disparo=tablero1[self.disparo_jugador2_fila-1][self.disparo_jugador2_columna-1]
				if validar_disparo==u"#" or validar_disparo==u"*":
					print u"    \t\t\t\t\t\tVAYA CAPITAN YA HEMOS DISPARADO EN ESTA POSICION"
					print u"    \t\t\t\t\t\tSeria mejor si lo vuelve a intentar"
					pausa7=raw_input("")
					os.system("cls")
					disparo_repetido=True
				else:
					disparo_repetido=False
#*******************************DISPARO ACERTADO JUGADOR DOS MULTIPLAYER*********************************************
			validar=tablero1[self.disparo_jugador2_fila-1][self.disparo_jugador2_columna-1]
			if validar==u"O":
				disparo()
								
				print u"    \t\t\t\t\t\tEXELENTE CAPITAN... Hemos impactado el barco enemigo...!!"
			  	print u""
			  	print u"\t\t\tt***************************** VIDAS RESTANTES %s *******************************"%(vidas)
				self.pausa4=raw_input(u"")
				os.system("cls")
			  
			  	tablero1[self.disparo_jugador2_fila-1][self.disparo_jugador2_columna-1]=u"#"
			  	tablero1_sin_vista[self.disparo_jugador2_fila-1][self.disparo_jugador2_columna-1]=u"#"
			  	os.system("cls")
				musica()
			  	print u""
			  	total_jugador2_multiplayer=total_jugador2_multiplayer+1
#************************ DISPARO FALLIDO JUGADOR DOS MULTPLAYER ************************************************
			else:
			   	print u"    \t\t\t\t\t\tVAYA.. estuvimos bastante cerca pero no hemos logrado impactar..!!"
			   	tablero1[self.disparo_jugador2_fila-1][self.disparo_jugador2_columna-1]=u"*"
			   	tablero1_sin_vista[self.disparo_jugador2_fila-1][self.disparo_jugador2_columna-1]=u"*"
				print u"\t\t\tt***************************** VIDAS RESTANTES %s *******************************"%(vidas)
				self.pausa4=raw_input(u"")
				os.system("cls")		   
			
			
#************************************************************************************************************************
#************************ VALIDACION GANADOR MUTILPLAYER ************************************************		
#************************ GANADOR UNO MULTIPLAYER ************************************************************
		if total_jugador1_multiplayer>total_jugador2_multiplayer:
			print u""" 
						 ██████╗  █████╗ ███╗   ██╗ █████╗ ██████╗  ██████╗ ██████╗     
						██╔════╝ ██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    
						██║  ███╗███████║██╔██╗ ██║███████║██║  ██║██║   ██║██████╔╝    
						██║   ██║██╔══██║██║╚██╗██║██╔══██║██║  ██║██║   ██║██╔══██╗    
						╚██████╔╝██║  ██║██║ ╚████║██║  ██║██████╔╝╚██████╔╝██║  ██║    
						 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝"""
			nombre_jugador_1()
			print u"""
					                       .'             \__/               (  )
					                     ( )               ||          _      ||
					                     /|\               ||       .-` \     ||
					                   .' | '              ||   _.-'    |     ||
					                  /   |\ \             || .'   `.__.'     ||   _.-..
					                .'   /| `.            _.-'   _.-'       _.-.`-'`._`.`
					                \  .' |  |        .-.`    `./      _.-`.    `._.-'
					                 |.   |  `.   _.-'   `.   .'     .'  `._.`---`
					                .'    |   |  :   `._..-'.'        `._..'  ||
					               /      |   \  `-._.'    ||                 ||
					              |     .'|`.  |           ||_.--.-._         ||
					              '    /  |  \ \       __.--'\    `. :        ||
					               \  .'  |   \|   ..-'   \   `._-._.'        ||
					`.._            |/    |    `.  \  \    `._.-              ||
					    `-.._       /     |      \  `-.'_.--'                 ||
					         `-.._.'      |      |        | |         _ _ _  _'_ _ _ _ _
					              `-.._   |      \        | |        |_|_|_'|_|_|_|_|_|_|
					                  [`--^-..._.'        | |       /....../|  __   __  |
					                   \`---.._|`--.._    | |      /....../ | |__| |__| |
					                    \__  _ `-.._| `-._|_|_ _ _/_ _ _ /  | |__| |__| |
					                     \   _o_   _`-._|_|_|_|_|_|_|_|_/   '-----------/
					                      \_`.|.'  _  - .--.--.--.--.--.`--------------'
					      .```-._ ``-.._   \__   _    _ '--'--'--'--'--'  - _ - _  __/
					 .`-.```-._ ``-..__``.- `.      _     -  _  _  _ -    _-   _  __/(.``-._
					 _.-` ``--..  ..    _.-` ``--..  .. .._ _. __ __ _ __ ..--.._ / .( _..``
					"""
			pausa=raw_input("")
			os.system("cls")
			nombre_jugador_1()
			print_tablero_jugador1()
			pausa=raw_input("")
			os.system("cls")
			nombre_jugador_2()
			print_tablero_jugador2()
			pausa=raw_input("")
			
#************************************************************************************************************			
#************************ GANADOR DOS MULTIPLAYER ************************************************************
		elif total_jugador1_multiplayer<total_jugador2_multiplayer:
			print u""" 
						 ██████╗  █████╗ ███╗   ██╗ █████╗ ██████╗  ██████╗ ██████╗     
						██╔════╝ ██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    
						██║  ███╗███████║██╔██╗ ██║███████║██║  ██║██║   ██║██████╔╝    
						██║   ██║██╔══██║██║╚██╗██║██╔══██║██║  ██║██║   ██║██╔══██╗    
						╚██████╔╝██║  ██║██║ ╚████║██║  ██║██████╔╝╚██████╔╝██║  ██║    
						 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝"""
			nombre_jugador_2()
			print u"""
						  _____|\.
						                  _.--| SSt |:
						                 <____|.----||
						                        .---''---,
						                         ;..__..'    _...
						                       ,'/  ;|/..--''    \.
						                     ,'_/.-/':            :
						                _..-'''/  /  |  \    \   _|/|
						               \      /-./_ \;   \    \,;'   \.
						               ,\    / \:  `:\    \   //    `:`.
						             ,'  \  /-._;   | :    : ::    ,.   .
						           ,'     ::   /`-._| |    | || ' :  `.`.)
						        _,'       |;._:: |  | |    | `|   :    `'
						      ,'   `.     /   |`-:_ ; |    |  |  : \.
						      `--.   )   /|-._:    :          |   \ \.
						         /  /   :_|   ;`-._;   __..--';    : :
						        /  (    ;|;-./_  _/.-:'o |   /     ' |
						       /  , \._/_/_./--''/_|:|___|_,'        |
						      :  /   `'-'--'----'---------'          |
						      | :     O ._O   O_. O ._O   O_.      ; ;
						      : `.      //    //    //    //     ,' /
						    ~~~`.______//____//____//____//_______,'~
						              //    //~   //    //
						       ~~   _//   _//   _// ~ _//     ~
						     ~     / /   / /   / /   / /  ~      ~~
						          ~~~   ~~~   ~~~   ~~~
						"""
			pausa=raw_input("")
			os.system("cls")
			nombre_jugador_1()
			print_tablero_jugador1()
			pausa=raw_input("")
			os.system("cls")
			nombre_jugador_2()
			print_tablero_jugador2()
			pausa=raw_input("")
#************************************************************************************************************************************************
#************************ EMPATE MULTPLAYER ************************************************************************************ 			
		else:
			print u"""
	██╗  ██╗ █████╗     ███████╗██╗██████╗  ██████╗     ██╗   ██╗███╗   ██╗    ███████╗███╗   ███╗██████╗  █████╗ ████████╗███████╗
	██║  ██║██╔══██╗    ██╔════╝██║██╔══██╗██╔═══██╗    ██║   ██║████╗  ██║    ██╔════╝████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
	███████║███████║    ███████╗██║██║  ██║██║   ██║    ██║   ██║██╔██╗ ██║    █████╗  ██╔████╔██║██████╔╝███████║   ██║   █████╗  
	██╔══██║██╔══██║    ╚════██║██║██║  ██║██║   ██║    ██║   ██║██║╚██╗██║    ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██╔══██║   ██║   ██╔══╝  
	██║  ██║██║  ██║    ███████║██║██████╔╝╚██████╔╝    ╚██████╔╝██║ ╚████║    ███████╗██║ ╚═╝ ██║██║     ██║  ██║   ██║   ███████╗
	╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝╚═╝╚═════╝  ╚═════╝      ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚══════╝"""
			print u"""
					                       .'             \__/               (  )
					                     ( )               ||          _      ||
					                     /|\               ||       .-` \     ||
					                   .' | '              ||   _.-'    |     ||
					                  /   |\ \             || .'   `.__.'     ||   _.-..
					                .'   /| `.            _.-'   _.-'       _.-.`-'`._`.`
					                \  .' |  |        .-.`    `./      _.-`.    `._.-'
					                 |.   |  `.   _.-'   `.   .'     .'  `._.`---`
					                .'    |   |  :   `._..-'.'        `._..'  ||
					               /      |   \  `-._.'    ||                 ||
					              |     .'|`.  |           ||_.--.-._         ||
					              '    /  |  \ \       __.--'\    `. :        ||
					               \  .'  |   \|   ..-'   \   `._-._.'        ||
					`.._            |/    |    `.  \  \    `._.-              ||
					    `-.._       /     |      \  `-.'_.--'                 ||
					         `-.._.'      |      |        | |         _ _ _  _'_ _ _ _ _
					              `-.._   |      \        | |        |_|_|_'|_|_|_|_|_|_|
					                  [`--^-..._.'        | |       /....../|  __   __  |
					                   \`---.._|`--.._    | |      /....../ | |__| |__| |
					                    \__  _ `-.._| `-._|_|_ _ _/_ _ _ /  | |__| |__| |
					                     \   _o_   _`-._|_|_|_|_|_|_|_|_/   '-----------/
					                      \_`.|.'  _  - .--.--.--.--.--.`--------------'
					      .```-._ ``-.._   \__   _    _ '--'--'--'--'--'  - _ - _  __/
					 .`-.```-._ ``-..__``.- `.      _     -  _  _  _ -    _-   _  __/(.``-._
					 _.-` ``--..  ..    _.-` ``--..  .. .._ _. __ __ _ __ ..--.._ / .( _..``
					"""

			pausa=raw_input("")
			os.system("cls")
			nombre_jugador_1()
			print_tablero_jugador1()
			pausa=raw_input("")
			os.system("cls")
			nombre_jugador_2()
			print_tablero_jugador2()
			pausa=raw_input("")		
#************************************************************************************************************************************************
#************************************************************************************************************************************************
#************************************ MULTIJUGADOR MODO OCULTO**************************************************************************************
class dos_jugadores_oculto(object):
	def multiplayer_oculto(self):
		os.system("cls")
		print u"\t\t███╗   ███╗██╗   ██╗██╗  ████████╗██╗     ██╗██╗   ██╗ ██████╗  █████╗ ██████╗  ██████╗ ██████╗ "
		print u"\t\t████╗ ████║██║   ██║██║  ╚══██╔══╝██║     ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗"
		print u"\t\t██╔████╔██║██║   ██║██║     ██║   ██║     ██║██║   ██║██║  ███╗███████║██║  ██║██║   ██║██████╔╝"
		print u"\t\t██║╚██╔╝██║██║   ██║██║     ██║   ██║██   ██║██║   ██║██║   ██║██╔══██║██║  ██║██║   ██║██╔══██╗"
		print u"\t\t██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██████╔╝╚██████╔╝██║  ██║"
		print u"\t\t╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝ ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝"
		print u""
		print u"\t\t\t\t               ()"
		print u"\t\t\t\t                    ||q',,'"
		print u"\t\t\t\t                    ||d,~"
		print u"\t\t\t\t         (,---------------------,)"
		print u"\t\t\t\t          ',       q888p       ,'"
		print u"\t\t\t\t            \       986       /"
		print u"\t\t\t\t             \  8p, d8b ,q8  /"
		print u"\t\t\t\t              ) 888a888a888 ("
		print u"\t\t\t\t             /  8b` q8p `d8  \              O"
		print u"\t\t\t\t            /       689       \             |','"
		print u"\t\t\t\t           /       d888b       \      (,---------,)"
		print u"\t\t\t\t         ,'_____________________',     \   ,8,   /"
		print u"\t\t\t\t         (`__________L|_________`)      ) a888a (    _,_"
		print u"\t\t\t\t         [___________|___________]     /___`8`___\   }*{"
		print u"\t\t\t\t           }:::|:::::}::|::::::{      (,=========,)  -=-"
		print u"\t\t\t\t   Samwise  '|::::}::|:::::{:|'  .,.    \:::|:::/    ~`~="
		print u"\t\t\t\t --=~(@)~=-- '|}:::::|::{:::|'          ~""~`~"
		print u"\t\t\t\t               '|:}::|::::|'~`~"""
		print u"\t\t\t\t           ~`~""~`~"                 "~`~""~"
		print u"\t\t\t\t                          ""~`~"
		print u"\t\t-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-."
		print u"\t\t.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-."
		print u"\t\t\t.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-"
		print u"\t\t\t\t.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-"
		print u"\n\n\n"
		pausa=raw_input("")
#********************************************************************************************************
#********************************************************************************************************************
#********************************** INGRESO DE NOMBRES MULTIJUGADOR *************************************************
		os.system("cls")
		print u"\t\t███╗   ███╗██╗   ██╗██╗  ████████╗██╗     ██╗██╗   ██╗ ██████╗  █████╗ ██████╗  ██████╗ ██████╗ "
		print u"\t\t████╗ ████║██║   ██║██║  ╚══██╔══╝██║     ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗"
		print u"\t\t██╔████╔██║██║   ██║██║     ██║   ██║     ██║██║   ██║██║  ███╗███████║██║  ██║██║   ██║██████╔╝"
		print u"\t\t██║╚██╔╝██║██║   ██║██║     ██║   ██║██   ██║██║   ██║██║   ██║██╔══██║██║  ██║██║   ██║██╔══██╗"
		print u"\t\t██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██████╔╝╚██████╔╝██║  ██║"
		print u"\t\t╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝ ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝"
		print u""
		print u""
		print u"\t\t\t\t\t\tBienvenido al modo multijugador"
		multijugador1_nombre=raw_input(u"\t\t\t\t\t\tIngrese el nombre del jugador numero (.1.)?: ")
		print u"\t\t\t\t\t\tExcelente bienvenido %s "%(multijugador1_nombre)
		print u""
		multijugador2_nombre=raw_input(u"\t\t\t\t\t\tIngrese el nombre del jugador numero (.2.)?: ")
		print u"\t\t\t\t\t\tExcelente bienvenido %s"%(multijugador2_nombre)
		print u""
		vidas=input("\t\t\t\t\t\tQue numero de vidas desea tener..??: ")
		os.system("cls")
#*******************************************************************************************************************************
#************************************** TURNOS JUGADOR UNO *********************************************************************
#************************************ VIDAS ************************************************************************
		
#************************************************************************************************************************		
		total_jugador1_multiplayer=0
		total_jugador2_multiplayer=0
		while vidas>0:
			
			
			disparo_repetido=True
			while disparo_repetido==True:
				nombre_jugador_1()
				print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador1_nombre)
				print_tablero_jugador1_sin_vista()
				print u""
				print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador2_nombre)
				print_tablero_jugador2_sin_vista2()
				print u""
#************************ DISPARO FILA JUGADOR UNO MULTIPLAYER ************************************************		
				validar_disparo_jugador1_fila=True
				while validar_disparo_jugador1_fila==True:
					try:
						self.disparo_jugador1_fila=int(raw_input(u"    \t\t\t\t\t\tIngrese fila: "))
						if self.disparo_jugador1_fila>10 or self.disparo_jugador1_fila<1:
							print "\t\t\t\t\t\tEsto esta fuera del oceano"
							print "\t\t\t\t\t\tSeria mejor si lo vuelves a intentar"
							pase6=raw_input("")
							os.system("cls")
							nombre_jugador_1()
							print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador1_nombre)
							print_tablero_jugador1_sin_vista()
							print u""
							print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador2_nombre)
							print_tablero_jugador2_sin_vista2()
							print u""
						
						else:
							self.disparo_jugador1_fila=self.disparo_jugador1_fila
							break	
					except:
						print "\t\t\t\t\t\tAs ingresado letras"		
						print "\t\t\t\t\t\tSeria mejor si lo vuelves a intentar"
						self.pause5=raw_input("")
						os.system("cls")
						nombre_jugador_1()
						print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador1_nombre)
						print_tablero_jugador1_sin_vista()
						print u""
						print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador2_nombre)
						print_tablero_jugador2_sin_vista2()
						print u""
#************************ DISPARO COLUMNA JUGADOR UNO MULTIPLAYER ************************************************
				
				validar_disparo_jugador1_columna=True
				while validar_disparo_jugador1_columna==True:
					try:
						self.disparo_jugador1_columna=int(raw_input(u"    \t\t\t\t\t\tIngrese columna: "))
						if self.disparo_jugador1_columna>10 or self.disparo_jugador1_columna<1:
							print "\t\t\t\t\t\tEsto esta fuera del oceano"
							print "\t\t\t\t\t\tSeria mejor si lo vuelves a intentar"
							self.pase6=raw_input("")
							os.system("cls")
							nombre_jugador_1()
							print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador1_nombre)
							print_tablero_jugador1_sin_vista()
							print ""
							print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador2_nombre)
							print_tablero_jugador2_sin_vista2()
							print u"    \t\t\t\t\t\tIngrese fila: %s"%(self.disparo_jugador1_fila)
						else:
							self.disparo_jugador1_columna=self.disparo_jugador1_columna
							break	
					except:
						print "\t\t\t\t\t\tAs ingresado letras"		
						print "\t\t\t\t\t\tAeria mejor si lo vuelves a intentar"
						self.pause5=raw_input("")
						os.system("cls")
						nombre_jugador_1()
						print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador1_nombre)
						print_tablero_jugador1_sin_vista()
						print ""
						print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador2_nombre)
						print_tablero_jugador2_sin_vista2()
						print u"    \t\t\t\t\t\tIngrese fila: %s"%(self.disparo_jugador1_fila)
								
#******************************DISPARO REPETIDO JUGADOR UNO MULTIPLAYER*************************************************
				validar_disparo=tablero2[self.disparo_jugador1_fila-1][self.disparo_jugador1_columna-1]
				if validar_disparo==u"#" or validar_disparo==u"*":
					print u"    \t\t\t\t\t\tVAYA CAPITAN YA HEMOS DISPARADO EN ESTA POSICION"
					print u"    \t\t\t\t\t\tSeria mejor si lo vuelve a intentar"
					pausa7=raw_input("")
					os.system("cls")
					disparo_repetido=True
				else:
					disparo_repetido=False
#****************************DISPARO ACERTADO JUGADOR UNO MULTIPLAYER*************************************************************
			validar=tablero2[self.disparo_jugador1_fila-1][self.disparo_jugador1_columna-1]
			if validar==u"O":
				tablero2[self.disparo_jugador1_fila-1][self.disparo_jugador1_columna-1]=u"#"
				tablero2_sin_vista[self.disparo_jugador1_fila-1][self.disparo_jugador1_columna-1]=u"#"
				
				disparo()
				print u"    \t\t\t\t\t\tEXELENTE CAPITAN... Hemos impactado el barco enemigo...!!"
			  	print u""
			  
				print u"\t\t\tt***************************** VIDAS RESTANTES %s *******************************"%(vidas)
				self.pausa4=raw_input(u"")
				os.system("cls")
				musica()
			  	total_jugador1_multiplayer=total_jugador1_multiplayer+1
#************************ DISPARO FALLIDO JUGADOR UNO MULTIPLAYER			  	
			else:
			   	print u"    \t\t\t\t\t\tVAYA.. estuvimos bastante cerca pero no hemos logrado impactar..!!"
			   	tablero2[self.disparo_jugador1_fila-1][self.disparo_jugador1_columna-1]=u"*"
				tablero2_sin_vista[self.disparo_jugador1_fila-1][self.disparo_jugador1_columna-1]=u"*"
			   	print u"\t\t\tt***************************** VIDAS RESTANTES %s *******************************"%(vidas)
				self.pausa4=raw_input(u"")
				os.system("cls")


			vidas=vidas-1
			
			

#******************************************************************************************************************************
#************************************ TURNOS JUGADOR DOS ******************************************************************************
			#total_jugador2_multiplayer=0
			
			
			disparo_repetido=True
			while disparo_repetido==True:
				nombre_jugador_2()
				print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador2_nombre)
				print_tablero_jugador2_sin_vista()
				print u""
				print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador1_nombre)
				print_tablero_jugador1_sin_vista2()
				print u""

#************************ DISPARO FILA JUGADOR DOS MULTIPLAYER ************************************************				
				validar_disparo_jugador2_fila=True
				while validar_disparo_jugador2_fila==True:
					try:
						self.disparo_jugador2_fila=int(raw_input(u"    \t\t\t\t\t\tIngrese fila: "))
						if self.disparo_jugador2_fila>10 or self.disparo_jugador2_fila <1:
							print "\t\t\t\t\t\tEsto esta fuera del oceano"
							print "\t\t\t\t\t\tSeria mejor si lo vuelves a intentar"
							self.pase6=raw_input("")
							os.system("cls")
							nombre_jugador_2()
							print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador2_nombre)
							print_tablero_jugador2_sin_vista()
							print u""
							print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador1_nombre)
							print_tablero_jugador1_sin_vista2()
							print u""
						else:
							self.disparo_jugador2_fila=self.disparo_jugador2_fila
							break	
					except:
						print "\t\t\t\t\t\tAs ingresado letras"		
						print "\t\t\t\t\t\tSeria mejor si lo vuelves a intentar"
						
						self.pause5=raw_input("")
						os.system("cls")
						nombre_jugador_2()
						print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador2_nombre)
						print_tablero_jugador2_sin_vista()
						print u""
						print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador1_nombre)
						print_tablero_jugador1_sin_vista2()
						print u""
#****************************DISPARO COLUMNA JUGADOR DOS MULTIPLAYER***************************************
				validar_disparo_jugador2_columna=True
				while validar_disparo_jugador2_columna==True:
					try:
						self.disparo_jugador2_columna=int(raw_input(u"    \t\t\t\t\t\tIngrese columna: "))
						if self.disparo_jugador2_columna>10 or self.disparo_jugador2_columna <1:
							print "\t\t\t\t\t\tEsto esta fuera del oceano"
							print "\t\t\t\t\t\tSeria mejor si lo vuelves a intentar"
							pase6=raw_input("")
							os.system("cls")
							nombre_jugador_2()
							print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador2_nombre)
							print_tablero_jugador2_sin_vista()
							print u""
							print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador1_nombre)
							print_tablero_jugador1_sin_vista2()
							print u"    \t\t\t\t\t\tIngrese fila: %s"%(self.disparo_jugador2_fila)
						else:
							self.disparo_jugador2_columna=self.disparo_jugador2_columna
							break
					except:
						print "\t\t\t\t\t\tAs ingresado letras"		
						print "\t\t\t\t\t\tSeria mejor si lo vuelves a intentar"
						self.pause5=raw_input("")
						os.system("cls")
						nombre_jugador_2()
						print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador2_nombre)
						print_tablero_jugador2_sin_vista()
						print u""
						print u"\t\t\t\t\t        ******    OCEANO JUGADOR %s   ******"%(multijugador1_nombre)
						print_tablero_jugador1_sin_vista2()
						print u"    \t\t\t\t\t\tIngrese fila: %s"%(self.disparo_jugador2_fila)
								
#******************************DISPARO REPETIDO JUGADOR DOS MULTIPLAYER**************************************************
				validar_disparo=tablero1[self.disparo_jugador2_fila-1][self.disparo_jugador2_columna-1]
				if validar_disparo==u"#" or validar_disparo==u"*":
					print u"    \t\t\t\t\t\tVAYA CAPITAN YA HEMOS DISPARADO EN ESTA POSICION"
					print u"    \t\t\t\t\t\tSeria mejor si lo vuelve a intentar"
					pausa7=raw_input("")
					os.system("cls")
					disparo_repetido=True
				else:
					disparo_repetido=False
#*******************************DISPARO ACERTADO JUGADOR DOS MULTIPLAYER*********************************************
				validar=tablero1[self.disparo_jugador2_fila-1][self.disparo_jugador2_columna-1]
			if validar==u"O":
				disparo()
								
				print u"    \t\t\t\t\t\tEXELENTE CAPITAN... Hemos impactado el barco enemigo...!!"
			  	print u""
			  	print u"\t\t\tt***************************** VIDAS RESTANTES %s *******************************"%(vidas)
				self.pausa4=raw_input(u"")
				os.system("cls")
			  
			  	tablero1[self.disparo_jugador2_fila-1][self.disparo_jugador2_columna-1]=u"#"
			  	tablero1_sin_vista[self.disparo_jugador2_fila-1][self.disparo_jugador2_columna-1]=u"#"
			  	os.system("cls")
				musica()
			  	print u""
			  	total_jugador2_multiplayer=total_jugador2_multiplayer+1
#************************ DISPARO FALLIDO JUGADOR DOS MULTPLAYER ************************************************
			else:
			   	print u"    \t\t\t\t\t\tVAYA.. estuvimos bastante cerca pero no hemos logrado impactar..!!"
			   	tablero1[self.disparo_jugador2_fila-1][self.disparo_jugador2_columna-1]=u"*"
			   	tablero1_sin_vista[self.disparo_jugador2_fila-1][self.disparo_jugador2_columna-1]=u"*"
				print u"\t\t\tt***************************** VIDAS RESTANTES %s *******************************"%(vidas)
				self.pausa4=raw_input(u"")
				os.system("cls")		   
			
			
#************************************************************************************************************************
#************************ VALIDACION GANADOR MUTILPLAYER ************************************************		
#************************ GANADOR UNO MULTIPLAYER ************************************************************
		if total_jugador1_multiplayer>total_jugador2_multiplayer:
			print u""" 
						 ██████╗  █████╗ ███╗   ██╗ █████╗ ██████╗  ██████╗ ██████╗     
						██╔════╝ ██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    
						██║  ███╗███████║██╔██╗ ██║███████║██║  ██║██║   ██║██████╔╝    
						██║   ██║██╔══██║██║╚██╗██║██╔══██║██║  ██║██║   ██║██╔══██╗    
						╚██████╔╝██║  ██║██║ ╚████║██║  ██║██████╔╝╚██████╔╝██║  ██║    
						 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝"""
			nombre_jugador_1()
			print u"""
					                       .'             \__/               (  )
					                     ( )               ||          _      ||
					                     /|\               ||       .-` \     ||
					                   .' | '              ||   _.-'    |     ||
					                  /   |\ \             || .'   `.__.'     ||   _.-..
					                .'   /| `.            _.-'   _.-'       _.-.`-'`._`.`
					                \  .' |  |        .-.`    `./      _.-`.    `._.-'
					                 |.   |  `.   _.-'   `.   .'     .'  `._.`---`
					                .'    |   |  :   `._..-'.'        `._..'  ||
					               /      |   \  `-._.'    ||                 ||
					              |     .'|`.  |           ||_.--.-._         ||
					              '    /  |  \ \       __.--'\    `. :        ||
					               \  .'  |   \|   ..-'   \   `._-._.'        ||
					`.._            |/    |    `.  \  \    `._.-              ||
					    `-.._       /     |      \  `-.'_.--'                 ||
					         `-.._.'      |      |        | |         _ _ _  _'_ _ _ _ _
					              `-.._   |      \        | |        |_|_|_'|_|_|_|_|_|_|
					                  [`--^-..._.'        | |       /....../|  __   __  |
					                   \`---.._|`--.._    | |      /....../ | |__| |__| |
					                    \__  _ `-.._| `-._|_|_ _ _/_ _ _ /  | |__| |__| |
					                     \   _o_   _`-._|_|_|_|_|_|_|_|_/   '-----------/
					                      \_`.|.'  _  - .--.--.--.--.--.`--------------'
					      .```-._ ``-.._   \__   _    _ '--'--'--'--'--'  - _ - _  __/
					 .`-.```-._ ``-..__``.- `.      _     -  _  _  _ -    _-   _  __/(.``-._
					 _.-` ``--..  ..    _.-` ``--..  .. .._ _. __ __ _ __ ..--.._ / .( _..``
					"""
			pausa=raw_input("")
			os.system("cls")
			nombre_jugador_1()
			print_tablero_jugador1()
			pausa=raw_input("")
			os.system("cls")
			nombre_jugador_2()
			print_tablero_jugador2()
			pausa=raw_input("")
#************************************************************************************************************			
#************************ GANADOR DOS MULTIPLAYER ************************************************************
		elif total_jugador1_multiplayer<total_jugador2_multiplayer:
			print u""" 
						 ██████╗  █████╗ ███╗   ██╗ █████╗ ██████╗  ██████╗ ██████╗     
						██╔════╝ ██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    
						██║  ███╗███████║██╔██╗ ██║███████║██║  ██║██║   ██║██████╔╝    
						██║   ██║██╔══██║██║╚██╗██║██╔══██║██║  ██║██║   ██║██╔══██╗    
						╚██████╔╝██║  ██║██║ ╚████║██║  ██║██████╔╝╚██████╔╝██║  ██║    
						 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝"""
			nombre_jugador_2()
			print u"""
						  _____|\.
						                  _.--| SSt |:
						                 <____|.----||
						                        .---''---,
						                         ;..__..'    _...
						                       ,'/  ;|/..--''    \.
						                     ,'_/.-/':            :
						                _..-'''/  /  |  \    \   _|/|
						               \      /-./_ \;   \    \,;'   \.
						               ,\    / \:  `:\    \   //    `:`.
						             ,'  \  /-._;   | :    : ::    ,.   .
						           ,'     ::   /`-._| |    | || ' :  `.`.)
						        _,'       |;._:: |  | |    | `|   :    `'
						      ,'   `.     /   |`-:_ ; |    |  |  : \.
						      `--.   )   /|-._:    :          |   \ \.
						         /  /   :_|   ;`-._;   __..--';    : :
						        /  (    ;|;-./_  _/.-:'o |   /     ' |
						       /  , \._/_/_./--''/_|:|___|_,'        |
						      :  /   `'-'--'----'---------'          |
						      | :     O ._O   O_. O ._O   O_.      ; ;
						      : `.      //    //    //    //     ,' /
						    ~~~`.______//____//____//____//_______,'~
						              //    //~   //    //
						       ~~   _//   _//   _// ~ _//     ~
						     ~     / /   / /   / /   / /  ~      ~~
						          ~~~   ~~~   ~~~   ~~~
						"""
			pausa=raw_input("")
			os.system("cls")
			nombre_jugador_1()
			print_tablero_jugador1()
			pausa=raw_input("")
			os.system("cls")
			nombre_jugador_2()
			print_tablero_jugador2()
			pausa=raw_input("")
#************************************************************************************************************************************************
#************************ EMPATE MULTPLAYER ************************************************************************************ 			
		else:
			print u"""
	██╗  ██╗ █████╗     ███████╗██╗██████╗  ██████╗     ██╗   ██╗███╗   ██╗    ███████╗███╗   ███╗██████╗  █████╗ ████████╗███████╗
	██║  ██║██╔══██╗    ██╔════╝██║██╔══██╗██╔═══██╗    ██║   ██║████╗  ██║    ██╔════╝████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
	███████║███████║    ███████╗██║██║  ██║██║   ██║    ██║   ██║██╔██╗ ██║    █████╗  ██╔████╔██║██████╔╝███████║   ██║   █████╗  
	██╔══██║██╔══██║    ╚════██║██║██║  ██║██║   ██║    ██║   ██║██║╚██╗██║    ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██╔══██║   ██║   ██╔══╝  
	██║  ██║██║  ██║    ███████║██║██████╔╝╚██████╔╝    ╚██████╔╝██║ ╚████║    ███████╗██║ ╚═╝ ██║██║     ██║  ██║   ██║   ███████╗
	╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝╚═╝╚═════╝  ╚═════╝      ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚══════╝"""
			print u"""
					                       .'             \__/               (  )
					                     ( )               ||          _      ||
					                     /|\               ||       .-` \     ||
					                   .' | '              ||   _.-'    |     ||
					                  /   |\ \             || .'   `.__.'     ||   _.-..
					                .'   /| `.            _.-'   _.-'       _.-.`-'`._`.`
					                \  .' |  |        .-.`    `./      _.-`.    `._.-'
					                 |.   |  `.   _.-'   `.   .'     .'  `._.`---`
					                .'    |   |  :   `._..-'.'        `._..'  ||
					               /      |   \  `-._.'    ||                 ||
					              |     .'|`.  |           ||_.--.-._         ||
					              '    /  |  \ \       __.--'\    `. :        ||
					               \  .'  |   \|   ..-'   \   `._-._.'        ||
					`.._            |/    |    `.  \  \    `._.-              ||
					    `-.._       /     |      \  `-.'_.--'                 ||
					         `-.._.'      |      |        | |         _ _ _  _'_ _ _ _ _
					              `-.._   |      \        | |        |_|_|_'|_|_|_|_|_|_|
					                  [`--^-..._.'        | |       /....../|  __   __  |
					                   \`---.._|`--.._    | |      /....../ | |__| |__| |
					                    \__  _ `-.._| `-._|_|_ _ _/_ _ _ /  | |__| |__| |
					                     \   _o_   _`-._|_|_|_|_|_|_|_|_/   '-----------/
					                      \_`.|.'  _  - .--.--.--.--.--.`--------------'
					      .```-._ ``-.._   \__   _    _ '--'--'--'--'--'  - _ - _  __/
					 .`-.```-._ ``-..__``.- `.      _     -  _  _  _ -    _-   _  __/(.``-._
					 _.-` ``--..  ..    _.-` ``--..  .. .._ _. __ __ _ __ ..--.._ / .( _..``
					"""
			pausa=raw_input("")
			os.system("cls")
			nombre_jugador_1()
			print_tablero_jugador1()
			pausa=raw_input("")
			os.system("cls")
			nombre_jugador_2()
			print_tablero_jugador2()
			pausa=raw_input("")

#************************************************************************************************************************************
#**************************************************************************************************************************************
#********************************************** MENU *******************************************************************************

print u""
print u"""\t\t\t\t 
			                                     |====|              `..
			                                      \__/               (  )
			                     ( )               ||          _      ||
			                     /|\               ||       .-` \     ||
			                   .' | '              ||   _.-'    |     ||
			                  /   |\ \             || .'   `.__.'     ||   _.-..
			                .'   /| `.            _.-'   _.-'       _.-.`-'`._`.`
			                \  .' |  |        .-.`    `./      _.-`.    `._.-'
			                 |.   |  `.   _.-'   `.   .'     .'  `._.`---`
			                .'    |   |  :   `._..-'.'        `._..'  ||
			               /      |   \  `-._.'    ||                 ||
			              |     .'|`.  |           ||_.--.-._         ||
			              '    /  |  \ \       __.--'\    `. :        ||
			               \  .'  |   \|   ..-'   \   `._-._.'        ||
			`.._            |/    |    `.  \  \    `._.-              ||
			    `-.._       /     |      \  `-.'_.--'                 ||
			         `-.._.'      |      |        | |         _ _ _  _'_ _ _ _ _
			              `-.._   |      \        | |        |_|_|_'|_|_|_|_|_|_|
			                  [`--^-..._.'        | |       /....../|  __   __  |
			                   \`---.._|`--.._    | |      /....../ | |__| |__| |
			                    \__  _ `-.._| `-._|_|_ _ _/_ _ _ /  | |__| |__| |
			                     \   _o_   _`-._|_|_|_|_|_|_|_|_/   '-----------/
			                      \_`.|.'  _  - .--.--.--.--.--.`--------------'
			      .```-._ ``-.._   \__   _    _ '--'--'--'--'--'  - _ - _  __/
			 .`-.```-._ ``-..__``.- `.      _     -  _  _  _ -    _-   _  __/(.``-._"""
print u"\t\t██████╗  █████╗ ████████╗ █████╗ ██╗     ██╗      █████╗     ███╗   ██╗ █████╗ ██╗   ██╗ █████╗ ██╗     "
print u"\t\t██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║     ██║     ██╔══██╗    ████╗  ██║██╔══██╗██║   ██║██╔══██╗██║     "
print u"\t\t██████╔╝███████║   ██║   ███████║██║     ██║     ███████║    ██╔██╗ ██║███████║██║   ██║███████║██║     "
print u"\t\t██╔══██╗██╔══██║   ██║   ██╔══██║██║     ██║     ██╔══██║    ██║╚██╗██║██╔══██║╚██╗ ██╔╝██╔══██║██║     "
print u"\t\t██████╔╝██║  ██║   ██║   ██║  ██║███████╗███████╗██║  ██║    ██║ ╚████║██║  ██║ ╚████╔╝ ██║  ██║███████╗"
print u"\t\t╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚══════"
print u""
print u"\t\t   Bienvenido a batalla naval, el juego consiste en colocar una flota propia de barcos escondidos"
print u"   \t\tcon los cuales debes de sobrevivir a la flota enemiga, tu misión es poder hundir la flota enemiga"
print u"       \t\tantes de que hundan la tuya y lo harás adivinando la hubicacion de los barcos enemigos."
print u"           \t\t     los cuales se encontrar ocultos en un tablero de 10X10 cuadros"
print u""
musica()

musica()
pausa=raw_input(u"")
os.system("cls")

#*******************************************************************************************************
validar_menu=True
while validar_menu==True:
#********* LISTAS VACIAS PARA TABLEROS ******************************************************
	tablero1=[]
	tablero1_sin_vista=[]
	tablero2=[]
	tablero2_sin_vista=[]
	tableropc=[]
	tableropc_sin_vista=[]
	validar_menu=True
#********************************************************************************************
#********* COLOCACION DE u"-" EN TABLEROS ****************************************************
	for x in range(0,10):
	    tablero1.append([u"-"] * 10)
	for x in range(0,10):
	    tablero1_sin_vista.append([u"-"] * 10)
	for x in range(0,10):
	    tablero2.append([u"-"] * 10)
	for x in range(0,10):
	    tablero2_sin_vista.append([u"-"] * 10)
	for x in range(0,10):
	    tableropc.append([u"-"] * 10)
	for x in range(0,10):
	    tableropc_sin_vista.append([u"-"] * 10)

#********************************************************************************************************
#************************************************************************************************************
	jugador_pc()
	jugador_dos()
	jugador_uno()
	try:
		os.system("cls")
		print u"\t\t\t\t\t███╗   ███╗███████╗███╗   ██╗██╗   ██╗"
		print u"\t\t\t\t\t████╗ ████║██╔════╝████╗  ██║██║   ██║"
		print u"\t\t\t\t\t██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║"
		print u"\t\t\t\t\t██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║"
		print u"\t\t\t\t\t██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝"
		print u"\t\t\t\t\t╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝"
		print u""
		print u"\t\t\t\t\tJUGADORES"
		print u"\t\t\t\t\t1) Un Jugador    Presione              (.1.): "
		print u"\t\t\t\t\t2) Dos Jugadores Modo Visible Presione (.2.): "
		print u"\t\t\t\t\t3) Dos Jugadores Modo Oculto  Presione (.3.): "
		print u"\t\t\t\t\t4) Salir	                       (.4.): "
		opcion_jugadores=int(raw_input( u"\t\t\t\t\t   Elija la opcion?: "))
		#if opcion_jugadores.isalpha()==False:
		
		if opcion_jugadores==1:
			clace1=un_jugador()
			clace1.single_player()
			
			validacion_volver=True
			while validacion_volver==True:
				try:
					
					regreso_menu=raw_input("\t\t\t\t\t\tDesea volver al menu YES/NO?: ")
					regreso_menu= regreso_menu.lower()
					if regreso_menu=="yes":
						print ""
						validacion_volver=False
						
						break
					elif regreso_menu=="no":
						validar_menu=False
						validacion_volver=False
						break
					else:
						print "\t\t\tOpcion no valida"
						validacion_volver=True
				except:
					print "\t\t\tDato no valido"
		elif opcion_jugadores==2:
			clace2=dos_jugadores()
			clace2.multiplayer()
			validacion_volver=True
			while validacion_volver==True:
				try:

					regreso_menu=raw_input("\t\t\t\t\t\tDesea volver al menu YES/NO?: ")
					regreso_menu= regreso_menu.lower()
					if regreso_menu=="yes":
					
						print ""
						validacion_volver=False
						break
					elif regreso_menu=="no":
						validar_menu=False
						validacion_volver=False
						break
					else:
						print "\t\t\t\t\t\tOpcion no valida"
						validacion_volver=True
				except:
					print "\t\t\t\t\t\tDato no valido"
		
		elif opcion_jugadores==3:
			clace2=dos_jugadores_oculto()
			clace2.multiplayer_oculto()
			validacion_volver=True
			while validacion_volver==True:
				try:

					regreso_menu=raw_input("\t\t\t\t\t\tDesea volver al menu YES/NO?: ")
					regreso_menu= regreso_menu.lower()
					if regreso_menu=="yes":
					
						print ""
						validacion_volver=False
						break
					elif regreso_menu=="no":
						validar_menu=False
						validacion_volver=False
						break
					else:
						print "\t\t\t\t\t\tOpcion no valida"
						validacion_volver=True
				except:
					print "\t\t\t\t\t\tDato no valido"

		elif opcion_jugadores==4:
			break



		else:
			os.system("cls")

			print u"\t\t\t\t\t███╗   ███╗███████╗███╗   ██╗██╗   ██╗"
			print u"\t\t\t\t\t████╗ ████║██╔════╝████╗  ██║██║   ██║"
			print u"\t\t\t\t\t██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║"
			print u"\t\t\t\t\t██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║"
			print u"\t\t\t\t\t██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝"
			print u"\t\t\t\t\t╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝"
			print u""
			print u"\t\t\t\t\tJUGADORES"
			print u"\t\t\t\t\t1) Un Jugador    Presione              (.1.): "
			print u"\t\t\t\t\t2) Dos Jugadores Modo Visible Presione (.2.): "
			print u"\t\t\t\t\t3) Dos Jugadores Modo Oculto  Presione (.3.): "
			print u"\t\t\t\t\t4) Salir	                       (.4.): "
			
			pausa=raw_input(u"\t\t\t\t\t   Dato no valido")

		
	except ValueError:
		os.system("cls")
		print u"\t\t\t\t\t███╗   ███╗███████╗███╗   ██╗██╗   ██╗"
		print u"\t\t\t\t\t████╗ ████║██╔════╝████╗  ██║██║   ██║"
		print u"\t\t\t\t\t██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║"
		print u"\t\t\t\t\t██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║"
		print u"\t\t\t\t\t██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝"
		print u"\t\t\t\t\t╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝"
		print u""
		print u"\t\t\t\t\tJUGADORES"
		print u"\t\t\t\t\t1) Un Jugador    Presione              (.1.): "
		print u"\t\t\t\t\t2) Dos Jugadores Modo Visible Presione (.2.): "
		print u"\t\t\t\t\t3) Dos Jugadores Modo Oculto  Presione (.3.): "
		print u"\t\t\t\t\t4) Salir	                       (.4.): "
		pausa=raw_input (u"\t\t\t\t\t   No se pueden ingresar letras")
#************************************************************************************************************
#*********************************************************************************************************************
os.system("cls")
print u""
print u""
print u"\t\t███████╗██╗███╗   ██╗    ██████╗ ███████╗██╗              ██╗██╗   ██╗███████╗ ██████╗  ██████╗ "
print u"\t\t██╔════╝██║████╗  ██║    ██╔══██╗██╔════╝██║              ██║██║   ██║██╔════╝██╔════╝ ██╔═══██╗"
print u"\t\t█████╗  ██║██╔██╗ ██║    ██║  ██║█████╗  ██║              ██║██║   ██║█████╗  ██║  ███╗██║   ██║"
print u"\t\t██╔══╝  ██║██║╚██╗██║    ██║  ██║██╔══╝  ██║         ██   ██║██║   ██║██╔══╝  ██║   ██║██║   ██║"
print u"\t\t██║     ██║██║ ╚████║    ██████╔╝███████╗███████╗    ╚█████╔╝╚██████╔╝███████╗╚██████╔╝╚██████╔╝"
print u"\t\t╚═╝     ╚═╝╚═╝  ╚═══╝    ╚═════╝ ╚══════╝╚══════╝     ╚════╝  ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ "
print u"""
				                       .'             \__/               (  )
				                     ( )               ||          _      ||
				                     /|\               ||       .-` \     ||
				                   .' | '              ||   _.-'    |     ||
				                  /   |\ \             || .'   `.__.'     ||   _.-..
				                .'   /| `.            _.-'   _.-'       _.-.`-'`._`.`
				                \  .' |  |        .-.`    `./      _.-`.    `._.-'
				                 |.   |  `.   _.-'   `.   .'     .'  `._.`---`
				                .'    |   |  :   `._..-'.'        `._..'  ||
				               /      |   \  `-._.'    ||                 ||
				              |     .'|`.  |           ||_.--.-._         ||
				              '    /  |  \ \       __.--'\    `. :        ||
				               \  .'  |   \|   ..-'   \   `._-._.'        ||
				`.._            |/    |    `.  \  \    `._.-              ||
				    `-.._       /     |      \  `-.'_.--'                 ||
				         `-.._.'      |      |        | |         _ _ _  _'_ _ _ _ _
				              `-.._   |      \        | |        |_|_|_'|_|_|_|_|_|_|
				                  [`--^-..._.'        | |       /....../|  __   __  |
				                   \`---.._|`--.._    | |      /....../ | |__| |__| |
				                    \__  _ `-.._| `-._|_|_ _ _/_ _ _ /  | |__| |__| |
				                     \   _o_   _`-._|_|_|_|_|_|_|_|_/   '-----------/
				                      \_`.|.'  _  - .--.--.--.--.--.`--------------'
				      .```-._ ``-.._   \__   _    _ '--'--'--'--'--'  - _ - _  __/
				 .`-.```-._ ``-..__``.- `.      _     -  _  _  _ -    _-   _  __/(.``-._
				 _.-` ``--..  ..    _.-` ``--..  .. .._ _. __ __ _ __ ..--.._ / .( _..``
				"""
#*********************************************************************************************************************
#*********************************************************************************************************************
#*********************************************************************************************************************
#*********************************************************************************************************************
#halestorm
# Avenged Sevenfold
#five fingers
#https://www.youtube.com/watch?v=o_l4Ab5FRwM&list=RDzIWeIChes5k
#http://www.msnanimal.cl/creador-de-nicks-ascii-msn.html
# Avenged Sevenfold
#five fingers
#https://www.youtube.com/watch?v=o_l4Ab5FRwM&list=RDzIWeIChes5k
#http://www.msnanimal.cl/creador-de-nicks-ascii-msn.html