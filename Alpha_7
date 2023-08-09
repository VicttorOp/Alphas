#!/usr/bin/env python3

# ---------- Importa as bibliotecas necessarias
import time # importando o tempo para a logica de programacao
import math # importando a matematica para a logica de programaaao
from ev3dev2.motor import * # importando tudo da biblioteca ev3dev2.motor
from ev3dev2.sound import Sound # importando o som da biblioteca ev3dev2.sound
from ev3dev2.button import Button # importando os botoes da biblioteca ev3dev2.button
from ev3dev2.sensor import * # importando tudo da biblioteca ev3dev2.sensor
from ev3dev2.sensor.lego import * # importando tudo da biblioteca ev3dev2.sensor.lego
#from ev3dev2.sensor.virtual import * # importando tudo da biblioteca ev3dev2.sensor.virtual

# ---------- Cria os motores do objeto
motorA = LargeMotor(OUTPUT_A) # Setando o motor na saida A como motorA
motorB = LargeMotor(OUTPUT_B) # Setando o motor na saida B como motorB
#motorC = LargeMotor(OUTPUT_C) # setando o motor na saída C como motorC
#motorD = LargeMotor(OUTPUT_D) # setando o motor na saída D como motorD

left_motor = motorA # Traduzindo que o motorA como motor da esquerda
right_motor = motorB # Traduzindo que o motorB como motor da direita
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B) # Setando o comando Tank_drive para utilizar os motores A e B juntos
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B) # Setando o comando steering_drive para utilizar a curva com os motores A e B

#spkr = Sound() # Setando a variavel som
#btn = Button() # Setando a variavel botao
#radio = Radio()  # Setando a variavel radio

CS1 = ColorSensor(INPUT_1)  # setando sensor de cor na entrada 
CS2 = ColorSensor(INPUT_2) # setando sensor de cor na entrada 
IS = InfraredSensor(INPUT_4)
##US = UltrasonicSensor(INPUT_4)  # setando sensor ultrasonico na entrada 
GS = GyroSensor(INPUT_3) # setando o sensor de giro na entra 
#TS = TouchSensor(INPUT_4) # setando o sensor de toque na entrada 
#color_sensor_in5 = ColorSensor(INPUT_5) # setando sensor de cor na entrada
SEM_COR = 0
PRETO = 1
AZUL = 2
VERDE = 3
AMARELO = 4
VERMELHO = 5
BRANCO = 6
MARROM = 7

x = 0

CS1.mode = 'COL-COLOR'
CS2.mode = 'COL-COLOR'
#US.mode = 'US-DIST-CM'
IS.mode = 'IR-PROX'
GS.mode = 'GYRO-ANG'
#TS.mode = 'TOUCH'



# ---------- Aqui é onde seus codigos começam

# ---------- Funções
rotina = 0
def comeco():
    global rotina
    if IS.proximity <= 10:
        GS.reset()
        time.sleep(.5)
        rotina += 1
    else:
        print("aguardando")

def procurando_azul():
    global rotina
    if (CS1.color and CS2.color) == 6:
        tank_drive.on(10,10)
    elif CS1.color and CS2.color == 2:
        print("achei!!!!")
        print(CS1.color)
        print(CS2.color)
        tank_drive.on(-10, -10)
    elif (CS1.color or CS2.color) != 6 or (CS1.color or CS2.color) != 2:
        print("parede a frente")
        time.sleep(0.1)
        rotina += 1


def parede():
    global rotina
    if CS1.color != CS2.color:
        if (CS1.color == 1 or 4 or 5) and (CS2.color == 6 or 2):
            print("A")      
            tank_drive.on(-1,3)
        elif (CS1.color == 6 or 2) and (CS2.color == 1 or 4 or 5):
            print("B")
            tank_drive.on(3,-1)
    elif (CS1.color == CS2.color) and (CS1.color and CS2.color) != 2 or 6:
        print("ta arrumado pai")
        time.sleep(.5)
        tank_drive.on_for_seconds(-5,-5, 4)
        time.sleep(.3)
        rotina += 1

def volta90():
    print('90')
    tank_drive.on_for_seconds(-5,-5, 5)
    time.sleep(.2)
    while GS.angle <= 90 and -90:
        tank_drive.on(-5,5)
    time.sleep(.2)
    tank_drive.on(0,0)

def volta180():
    print('180')
    tank_drive.on_for_seconds(-5,-5, 5)
    time.sleep(.2)
    while GS.angle <= 180 and -180:
        tank_drive.on(5,-5)
    time.sleep(.2)
    tank_drive.on(0,0)


# --------- COMEÇO DO CÓDIGO

while rotina == 0:
    print("comeco")
    comeco()
    
    
while rotina == 1:
    print("mim de")
    procurando_azul()

    
while rotina == 2:
    print("parede")
    parede()

while rotina == 3:
    if (CS1.color == 1 or 4) and (CS2.color == 1 or 4):
        volta90()
        time.sleep(.2)
        rotina == 1
    elif (CS1.color and CS2.color) == 5:
        volta180()
        time.sleep(.2)
        rotina == 1
    
