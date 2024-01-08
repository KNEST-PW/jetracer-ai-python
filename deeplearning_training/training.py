from time import sleep
import pygame
import sys
sys.path.insert(1,'../utils')
from nvidia_racecar import NvidiaRacecar
from camera import CameraJet


car = NvidiaRacecar()
pygame.init()
cam = CameraJet()

# joystick
while True:
    if pygame.joystick.get_count() > 0:
        break   
    print("No controller detected")
    sleep(0.5)
print(f"Found {pygame.joystick.get_count()} joystick")
js = pygame.joystick.Joystick(0)
name = js.get_name()
js.init()
print(f"connected to {name}")

licznik = 0
car = NvidiaRacecar()
skret, silnik = 0, 0
loop = True
plik = open("skret_silnik.txt", 'w')
while loop:
    for event in pygame.event.get():
        skret = round(js.get_axis(0),1)
        silnik = round(js.get_axis(3),1)*-1
        if js.get_button(1) == 1:
            print('STOP')
            loop = False
    car.steering = skret
    car.throttle = silnik
    print(licznik, skret, silnik, sep=";", file=plik)
    frame = cam.read_frame()
    with open(f"zdj/zdj{licznik}.jpg", "wb") as file:
        file.write(cam.read_frame_jpg())
    licznik += 1
    sleep(0.2)

plik.close()