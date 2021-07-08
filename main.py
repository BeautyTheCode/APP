
#from pyfirmata import Arduino, SERVO
from time import sleep
#from pyfirmata.pyfirmata import Board
#port = '/dev/ttyACM0'

#board = Arduino(port)
#pin = 10
#board.digital[pin].mode = SERVO

#def rotateServo(pin, angle):
    board.digital[pin].write(angle)

#while True:
    rotateServo(pin,100)

    #on and off
    rotateServo(pin,100)

