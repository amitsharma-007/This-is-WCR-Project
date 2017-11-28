/* 
This section section involves python script for controlling a mobile robot using xbox 360. This is a subpart of a WCR for industrial 
inspection project in TLC under the guidance of Dr. S. R. pandian and is being done by Amit Sharma, M.Des EDS 2016 batch, roll no. 
eds16m007.   
*/

# This program uses python script to control amobile robot using Microsoft xbox 360 remote.
# It uses BCM configuration of the raspberry pi pins. 
# Four DC motors have been used to control the motion of the robot.
# For the four motors we need 8 pins for 8 different terminals of the used motors and one more pin for PWM for controlling the speed
# of the motors. 
# Below pin declaration m1p1 denotes the motor 1 and teminal 1 and per se
# It also require two L298N motor driver. Connect the raspberry pi pins to the input terminals of the motor driver
# To use XBOX 360 remote control, You will be having one XBOX 360 USB receiver and one remote control itself.
# Connect USB receiver to the one of the USB jack given in raspberry pi and power on the remote.
# See the green light appearing on both. If it so, remote is paired.
# You can control the speed right trigger. 
# "Y" button on the remote indicates froward movement, "A" button the remote indicates backward movement, "X" indicates left turn and 
# "B" indicates right turn
# After everything done siccessfully, run this python script in your raspberry pi and you are good to go.





import RPi.GPIO as GPIO
import time
import xbox


m1p1 = 5
m1p2 = 6
m2p1 = 13
m2p2 = 19
m3p1 = 26
m3p2 = 12
m4p1 = 16
m4p2 = 20
pwm = 21



def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(m1p1, GPIO.OUT)
    GPIO.setup(m1p2, GPIO.OUT)
    GPIO.setup(m2p1, GPIO.OUT)
    GPIO.setup(m2p2, GPIO.OUT)
    GPIO.setup(m3p1, GPIO.OUT)
    GPIO.setup(m3p2, GPIO.OUT)
    GPIO.setup(m4p1, GPIO.OUT)
    GPIO.setup(m4p2, GPIO.OUT)
    GPIO.setup(pwm, GPIO.OUT)
    

def move_back():
    GPIO.output(m1p1, True)
    GPIO.output(m1p2, False)
    GPIO.output(m2p1, False)
    GPIO.output(m2p2, True)
    GPIO.output(m3p1, False)
    GPIO.output(m3p2, True)
    GPIO.output(m4p1, False)
    GPIO.output(m4p2, True)

def stop():
    GPIO.output(m1p1, True)
    GPIO.output(m1p2, True)
    GPIO.output(m2p1, True)
    GPIO.output(m2p2, True)
    GPIO.output(m3p1, True)
    GPIO.output(m3p2, True)
    GPIO.output(m4p1, True)
    GPIO.output(m4p2, True)

def move_front():
    GPIO.output(m1p1, False)
    GPIO.output(m1p2, True)
    GPIO.output(m2p1, True)
    GPIO.output(m2p2, False)
    GPIO.output(m3p1, True)
    GPIO.output(m3p2, False)
    GPIO.output(m4p1, True)
    GPIO.output(m4p2, False)


def turn_left():
    GPIO.output(m1p1, True)
    GPIO.output(m1p2, False)
    GPIO.output(m2p1, True)
    GPIO.output(m2p2, False)
    GPIO.output(m3p1, False)
    GPIO.output(m3p2, True)
    GPIO.output(m4p1, True)
    GPIO.output(m4p2, False)

def turn_right():
    GPIO.output(m1p1, False)
    GPIO.output(m1p2, True)
    GPIO.output(m2p1, False)
    GPIO.output(m2p2, True)
    GPIO.output(m3p1, True)
    GPIO.output(m3p2, False)
    GPIO.output(m4p1, False)
    GPIO.output(m4p2, True)

def control_all():
    joy = xbox.Joystick()
    while (joy.A()):
        move_front()

GPIO.setwarnings(False)
GPIO.cleanup()
time.sleep(1)
setup()
my_pwm = GPIO.PWM(pwm,50)
my_pwm.start(98)
pwm_v = 98

def fmtFloat(n):
    return '{:6.3f}'.format(n)
    
joy = xbox.Joystick()


print "Press back button on the xbox360 remote to stop the Process"

while not joy.Back():
 
    if joy.connected():
        print "Connected   ",
    else:
        print "Disconnected",
   
    print "Lx,Ly ",fmtFloat(joy.leftX()),fmtFloat(joy.leftY()),
    # Right trigger
    print "Rtrg ",fmtFloat(joy.rightTrigger()),
    # A/B/X/Y buttons
    print "Buttons ",
    if joy.A():
        move_back()
    elif joy.B():
        turn_right()
    elif joy.X():
        turn_left()
    elif joy.Y():
        move_front()
    else:
        stop()
    pwm_v = 100- ((joy.rightTrigger())*100)
        
    my_pwm.ChangeDutyCycle(pwm_v)
   
        
    # Move cursor back to start of line
    print chr(13),
# Close out when done
joy.close()

