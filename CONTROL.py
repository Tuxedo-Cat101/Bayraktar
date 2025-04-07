from djitellopy import tello
from time import sleep
import threading

drone = tello.Tello()
drone.connect()
sleep(3)  
drone.takeoff()
sleep(4)
drone.move_up(60)
sleep(4)
drone.flip("f")
sleep(4)
drone.flip("b")
sleep(4)
drone.land()
sleep(4)
drone.end()
