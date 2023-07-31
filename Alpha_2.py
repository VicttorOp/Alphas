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

CS1 = ColorSensor(INPUT_1)  # setando sensor de cor na entrada in1
CS2 = ColorSensor(INPUT_2) # setando sensor de cor na entrada in2
US = UltrasonicSensor(INPUT_3)  # setando sensor ultrasonico na entrada in2
GS = GyroSensor(INPUT_4) # setando o sensor de giro na entra in3
#color_sensor_in5 = ColorSensor(INPUT_5) # setando sensor de cor na entrada in5
SEM_COR = 0
PRETO = 1
AZUL = 2
VERDE = 3
AMARELO = 4
VERMELHO = 5
BRANCO = 6
MARROM = 7

rotina = 0

x = 0

CS1.mode = 'COL-COLOR'
CS2.mode = 'COL-COLOR'
US.mode = 'US-DIST-CM'
GS.mode = 'GYRO-ANG'



# ---------- Aqui é onde seus codigos começam

# ---------- Funções

def comeco():
    if US.distance_centimeters <= 5:
        GS.reset()
        time.sleep_ms(500)
        rotina = rotina + 1
    else:
        print("aguardando")

def procurando_azul():
    if (CS1.color and CS2.color) == 6:
        tank_drive.on(10,10,8)
    elif CS1.color or CS2.color == 2:
        print("achei!!!!")
    elif (CS1.color or CS2.color) != 6 or 2:
        printa("parede a frente")
        time.sleep_ms(1000)
        rotina += 1


def parede():
    if (CS1.color == 1 or 4 or 5) and (CS2.color == 6 or 2):       
        tank_drive.on(-2,6)
    elif (CS1.color == 6 or 2) and (CS2.color == 1 or 4 or 5):
        tank_drive.con(6,-2)
    elif (CS1.color == CS2.color) and != 2 or 6:
        print("ta arrumado pai")
        time.sleep_ms(500)
        tank_drive.on_for_seconds(-5,-5, 4)
        time.sleep_ms(300)
        rotina += 1

def volta90():
    tank_drive.on_for_seconds(-5,-5, 5)
    time.sleep_ms(200)
    while GS.angle <= 90 and -90:
        tank_drive.on(-5,5)
    time.sleep_ms(200)
    tank_drive.on(0,0)

def volta180():
    tank_.drive.on_for_seconds(-5,-5, 5)
    time.sleep_ms(200)
    while GS.angle <= 180 and -180:
        tank_drive.on(5,-5)
    time.sleep_ms(200)
    tank_drive.on(0,0)


# --------- COMEÇO DO CÓDIGO

while rotina == 0:
    print("comeco")
    comeco()
    
    
while rotina == 1:
    print("mim dê")
    procurando_azul()

    
while rotina == 2:
    print("parede")
    parede()

    
