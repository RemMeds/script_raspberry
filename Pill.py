#!/usr/bin/python
# coding=utf-8

# Les modules necessaires sont importes et mis en place
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# La broche d'entree du capteur est declaree. En outre la resistance de Pull-up est activee.
GPIO_PIN = 21  # Senseur Hall branche sur GPIO 24
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Sensor-Test [Appuyez sur Ctrl + C pour terminer le test]")


# Cette fonction de sortie est executee par detection du signal
def fonctionDeSortie(null):
    print("Signal détecté")


# Lors de la detection d'un signal (front descendant du signal) de la fonction de sortie est declenchee
GPIO.add_event_detect(GPIO_PIN, GPIO.RISING, callback=fonctionDeSortie, bouncetime=100)

# Boucle de programme principale
try:
    while True:
        time.sleep(1)

# reinitialisation de tous les GPIO en entrees
except KeyboardInterrupt:
    GPIO.cleanup()